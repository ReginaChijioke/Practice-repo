import json
import os
ticket_list = [
    {
        "id": None,
        "title": None,
        "description": None
    }
]

def create_ticket():
    ticket_id = input("Enter ticket id: ").strip()
    title = input("Enter title: ").strip()
    description = input("Enter ticket description: ").strip()
    for ticket in ticket_list:
        if not ticket_id or not title or not description:
            print("id, title and description cannot be empty. ")
        elif ticket_id == ticket["id"]:
            print("Cannot create ticket with duplicate id")
        else:
            ticket = {
                "id": ticket_id,
                "title": title,
                "description": description
            }
            ticket_list.append(ticket)
            print("ticket have been created successfully")
    return
create_ticket()


TICKETS = "tickets.json"
def load_tickets():
    if os.path.exists(TICKETS):
        try:
            with open(TICKETS, "r") as read_file:
                ticket = json.load(read_file)
                return ticket
        except json.JSONDecodeError:
            raise
    else:
        return []
load_tickets()

def save_tickets(ticket):
    with open(TICKETS, "w") as written_file:
        json.dump(ticket_list, written_file,)
save_tickets(ticket_list)