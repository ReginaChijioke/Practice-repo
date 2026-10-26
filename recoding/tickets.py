import json
import os
from dotenv import load_dotenv
from google import genai

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
        print("title and description cannot be empty. ")
        return 
    next_id = generate_ticket_id(tickets)
    ticket = {
        "id": next_id,
        "title": title,
        "description": description
    }
    tickets.append(ticket)
    save_tickets(tickets)
    print("ticket created successfully")
    return next_id



def analyze_ticket(ticket_id):
    saved_tickets = load_tickets()

    matching_ticket = None

    for ticket in saved_tickets:
        if ticket["id"] == ticket_id:
            matching_ticket = ticket
            break

    if matching_ticket is None:
        return False, "Ticket not found."

    description = matching_ticket["description"]

    if not os.getenv("GEMINI_API_KEY"):
        return False, "Gemini API key is missing."

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=(
                "You are a technical support assistant. "
                "Analyze this support ticket. Suggest likely causes "
                "and practical troubleshooting steps. "
                "Be clear when you are uncertain.\n\n"
                f"Ticket description: {description}"
            )
        )

        if not response.text:
            return False, "Gemini returned no suggestions."

        return True, response.text

    except Exception as error:
        print(f"AI analysis failed: {error}")
        return False, "Could not analyze the ticket. The ticket was still saved."




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
            print("\nAI Suggestions:")
            print(result)
        else:
            print(result)
except json.JSONDecodeError:
    print("Invalid json.")

