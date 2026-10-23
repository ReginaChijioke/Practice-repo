import json
import os
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
    create_ticket()
except json.JSONDecodeError:
    print("Invalid json.")