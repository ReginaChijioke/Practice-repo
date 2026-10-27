import json
import os
import sys
import threading
import itertools
import time
from dotenv import load_dotenv
from google import genai
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
TICKETS = "tickets.json"
tickets = []


def generate_ticket_id(tickets):
    if not tickets:
        next_number = 1
    else:
        ticket_numbers = []
        for ticket in tickets:
            ticket_id = ticket["id"]
            numeric_part = int(ticket_id[1:])
            ticket_numbers.append(numeric_part)

        largest_number = ticket_numbers[0]
        for number in ticket_numbers:
            if number > largest_number:
                largest_number = number
        next_number = largest_number + 1
    return f"T{next_number:03d}"
        

def save_tickets(tickets):
    with open(TICKETS, "w") as written_file:
        json.dump(tickets, written_file, indent=4)

def create_ticket():
    title = input("Enter title: ").strip()
    description = input("Enter ticket description: ").strip()
    if not title or not description:
        print(f"{RED}title and description cannot be empty.{RESET} ")
        return 
    next_id = generate_ticket_id(tickets)
    ticket = {
        "id": next_id,
        "title": title,
        "description": description
    }
    tickets.append(ticket)
    save_tickets(tickets)
    print(f"{GREEN}ticket created successfully{RESET}")
    return next_id



def spinner(stop_event):
    symbols = itertools.cycle(["|", "/", "-", "\\"])

    while not stop_event.is_set():
        sys.stdout.write(f"{CYAN}\rGemini is analyzing your ticket... {next(symbols)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()
    print()

def analyze_ticket(ticket_id):
    saved_tickets = load_tickets()

    matching_ticket = None

    for ticket in saved_tickets:
        if ticket["id"] == ticket_id:
            matching_ticket = ticket
            break

    if matching_ticket is None:
        return False, f"{RED}Ticket not found.{RESET}"

    description = matching_ticket["description"]

    if not os.getenv("GEMINI_API_KEY"):
        return False, f"{RED}Gemini API key is missing.{RESET}"

    stop_event = threading.Event()

    spinner_thread = threading.Thread(
        target=spinner,
        args=(stop_event,)
    )

    spinner_thread.start()
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=(
                """
                You are a friendly technical support assistant helping users troubleshoot IT problems.
                Analyze the support ticket and respond using simple, everyday English.
                Structure your response as follows:
                Explain up to three likely causes. Be clear that these are possibilities, not confirmed diagnoses.
                Give up to three practical, safe troubleshooting steps, starting with the simplest.
                Follow-up questions: Ask one or two focused questions if more information is needed to narrow down the cause.
                Keep your response concise but helpful. Explain technical terms when necessary. Start with checks that do not depend on a particular operating system. Only provide operating-system-specific instructions when the operating system is known.
                Do not claim that a problem has been fixed or that a cause is confirmed without evidence. If the problem appears to affect an entire network or requires specialist attention, recommend contacting IT support.
                Be clear when you are uncertain.
                """
                f"Ticket description: {description}"
            )
        )

        if not response.text:
            return False, "Gemini returned no suggestions."
       
        return True, response.text
    except Exception as error:
        error_message = str(error)

        if "Temporary failure in name resolution" in error_message:
            print(f"{RED}AI analysis failed: No internet connection detected.{RESET}")
            return (
                False,
                "Your ticket was saved, but AI analysis requires an internet connection."
            )

        if (
            "API key not valid" in error_message
            or "401 UNAUTHENTICATED" in error_message
        ):
            print(f"{RED}AI analysis failed: The Gemini API key is incorrect.{RESET}")
            return (
                False,
                "Your ticket was saved, but AI analysis could not run because the API key is invalid."
            )

        if (
            "503 UNAVAILABLE" in error_message
            or "high demand" in error_message
        ):
            print(f"{RED}AI analysis failed: Gemini is temporarily unavailable.{RESET}")
            return (
                False,
                "Your ticket was saved, but Gemini is temporarily busy. "
                "Please try the AI analysis again shortly."
            )

        print(f"{RED}AI analysis failed: {error}{RESET}")
        return False, "Could not connect to Gemini. Your ticket was still saved."
    finally:
        stop_event.set()
        spinner_thread.join()
def load_tickets():
    if os.path.exists(TICKETS):
        try:
            with open(TICKETS, "r") as read_file:
                tickets = json.load(read_file)
                return tickets
        except json.JSONDecodeError:
            raise
    else:
        return []


try:
    tickets = load_tickets()
    ticket_id = create_ticket()
    if ticket_id:
        success, result = analyze_ticket(ticket_id)

        if success:
            print(f"{MAGENTA}\nAI Suggestions:{RESET}")
            print(result)
        else:
            print(result)
except json.JSONDecodeError:
    print("Invalid json.")

