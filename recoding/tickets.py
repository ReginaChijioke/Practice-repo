import json
import os
import sys
import threading
import itertools
import time

from dotenv import load_dotenv
from google import genai
from groq import Groq
from openai import OpenAI

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

TICKETS = "tickets.json"

load_dotenv()

tickets = []


# ---------- Ticket management ----------

def generate_ticket_id(tickets):
    numbers = [
        int(ticket["id"][1:])
        for ticket in tickets
        if ticket.get("id", "")[1:].isdigit()
    ]

    next_number = max(numbers, default=0) + 1
    return f"T{next_number:03d}"


def save_tickets(tickets):
    with open(TICKETS, "w") as file:
        json.dump(tickets, file, indent=4)


def load_tickets():
    if not os.path.exists(TICKETS):
        return []

    with open(TICKETS, "r") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("tickets.json must contain a list of tickets.")

    return data


def create_ticket():
    title = input("Enter title: ").strip()
    description = input("Enter ticket description: ").strip()

    if not title or not description:
        print(f"{RED}Title and description cannot be empty.{RESET}")
        return None

    ticket_id = generate_ticket_id(tickets)

    ticket = {
        "id": ticket_id,
        "title": title,
        "description": description
    }

    tickets.append(ticket)
    save_tickets(tickets)

    print(f"{GREEN}Ticket {ticket_id} created successfully.{RESET}")
    return ticket_id


# ---------- Shared AI prompt ----------

def get_prompt(description):
    return f"""
You are a friendly technical support assistant helping users
troubleshoot IT problems.

Analyze the support ticket and respond using simple, everyday English.

Include:
1. Up to three likely causes. Make clear these are possibilities,
   not confirmed diagnoses.
2. Up to three practical, safe troubleshooting steps, starting
   with the simplest.
3. One or two focused follow-up questions if more information
   is needed.

Start with checks that do not depend on a particular operating
system. Give operating-system-specific instructions only when
the operating system is known.

Do not claim that a problem has been fixed or that a cause is
confirmed without evidence.

If the problem appears to affect an entire network or requires
specialist attention, recommend contacting IT support.

Ticket description: {description}
"""


# ---------- Standard result format ----------

def make_result(provider, success, analysis=None, error=None):
    return {
        "success": success,
        "analysis": analysis,
        "error": error,
        "provider": provider
    }


# ---------- Provider-specific functions ----------

def analyze_with_gemini(description):
    provider = "Gemini"
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return make_result(
            provider, False,
            error="GEMINI_API_KEY is missing from your .env file."
        )

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
            contents=get_prompt(description)
        )

        if not response.text or not response.text.strip():
            return make_result(
                provider, False,
                error="Gemini returned an empty analysis."
            )

        return make_result(provider, True, analysis=response.text)

    except Exception as error:
        return make_result(
            provider, False,
            error=explain_provider_error(provider, error)
        )


def analyze_with_groq(description):
    provider = "Groq"
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return make_result(
            provider, False,
            error="GROQ_API_KEY is missing from your .env file."
        )

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
            messages=[
                {
                    "role": "user",
                    "content": get_prompt(description)
                }
            ]
        )

        analysis = response.choices[0].message.content

        if not analysis or not analysis.strip():
            return make_result(
                provider, False,
                error="Groq returned an empty analysis."
            )

        return make_result(provider, True, analysis=analysis)

    except Exception as error:
        return make_result(
            provider, False,
            error=explain_provider_error(provider, error)
        )


def analyze_with_openrouter(description):
    provider = "OpenRouter"
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return make_result(
            provider, False,
            error="OPENROUTER_API_KEY is missing from your .env file."
        )

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        response = client.chat.completions.create(
            model=os.getenv("OPENROUTER_MODEL", "openrouter/free"),
            messages=[
                {
                    "role": "user",
                    "content": get_prompt(description)
                }
            ]
        )

        analysis = response.choices[0].message.content

        if not analysis or not analysis.strip():
            return make_result(
                provider, False,
                error="OpenRouter returned an empty analysis."
            )

        return make_result(provider, True, analysis=analysis)

    except Exception as error:
        return make_result(
            provider, False,
            error=explain_provider_error(provider, error)
        )


# ---------- Shared error interpretation ----------

def explain_provider_error(provider, error):
    message = str(error).lower()

    if (
        "temporary failure in name resolution" in message
        or "connection error" in message
        or "connection refused" in message
        or "network is unreachable" in message
    ):
        return (
            f"{provider} could not be reached. "
            "Check your internet connection and try again."
        )

    if (
        "401" in message
        or "403" in message
        or "unauthenticated" in message
        or "invalid api key" in message
        or "authentication" in message
    ):
        return (
            f"{provider} rejected the API credentials. "
            "Check the API key in your .env file."
        )

    if "429" in message or "rate limit" in message:
        return (
            f"{provider} is rate-limited or your quota may be exhausted. "
            "Try again later or choose another provider."
        )

    if (
        "404" in message
        or "model not found" in message
        or "no endpoints found" in message
    ):
        return (
            f"{provider} could not find or access the configured model. "
            "Check the model ID and its availability."
        )

    if "503" in message or "service unavailable" in message:
        return (
            f"{provider} is temporarily unavailable. "
            "Try again later or choose another provider."
        )

    return (
        f"{provider} could not complete the analysis. "
        "Check your configuration and try again."
    )


# ---------- Loading animation ----------

def spinner(stop_event, provider):
    symbols = itertools.cycle(["|", "/", "-", "\\"])
    message = f"{provider} is analysing your ticket..."

    while not stop_event.is_set():
        sys.stdout.write(
            f"\r\033[K{CYAN}{message} {next(symbols)}{RESET}"
        )
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

# ---------- Analysis workflow ----------

PROVIDERS = {
    "1": ("Gemini", analyze_with_gemini),
    "2": ("Groq", analyze_with_groq),
    "3": ("OpenRouter", analyze_with_openrouter)
}


def choose_provider():
    while True:
        print(f"{BLUE}\nChoose an AI provider:{RESET}")
        print(f"{YELLOW}1. Gemini{RESET}")
        print(f"{YELLOW}2. Groq{RESET}")
        print(f"{YELLOW}3. OpenRouter{RESET}")

        choice = input("Enter your choice (1-3): ").strip()

        if choice in PROVIDERS:
            return choice

        print(f"{RED}Invalid choice. Select 1, 2, or 3.{RESET}")


def analyze_ticket(ticket_id):
    try:
        saved_tickets = load_tickets()
    except (json.JSONDecodeError, OSError, ValueError):
        return make_result(
            "None", False,
            error="Could not load tickets. Check tickets.json."
        )

    ticket = next(
        (
            item for item in saved_tickets
            if item.get("id") == ticket_id
        ),
        None
    )

    if ticket is None:
        return make_result(
            "None", False,
            error=f"Ticket {ticket_id} was not found."
        )

    choice = choose_provider()
    provider, provider_function = PROVIDERS[choice]

    stop_event = threading.Event()

    spinner_thread = threading.Thread(
        target=spinner,
        args=(stop_event, provider)
    )

    spinner_thread.start()

    try:
        result = provider_function(ticket["description"])
        return result

    finally:
        stop_event.set()
        spinner_thread.join()


# ---------- Display results and handle retries ----------

def run_analysis(ticket_id):
    while True:
        result = analyze_ticket(ticket_id)

        print(f"\n{MAGENTA}AI Analysis — {result['provider']}{RESET}")

        if result["success"]:
            print(result["analysis"])
            return

        print(f"{RED}{result['error']}{RESET}")

        retry = input(
            "\nWould you like to try again or choose another provider? "
            "(y/n): "
        ).strip().lower()

        if retry != "y":
            return


# ---------- Application entry point ----------

def main():
    global tickets

    try:
        tickets = load_tickets()
    except (json.JSONDecodeError, OSError, ValueError):
        print(
            f"{RED}Could not load tickets.json. "
            f"Check that the file contains valid ticket data.{RESET}"
        )
        return

    ticket_id = create_ticket()

    if ticket_id:
        run_analysis(ticket_id)

if __name__ == "__main__":
    main()
