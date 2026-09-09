from text_utils import clean_text
from categories import categories, general_response
from classifier import classify, respond

exit_commands = ["exit", "quit", "done"]
ticket_count = 0
while True:
    complaint = input("how may i help you: ")
    message = clean_text(complaint)
    if message in exit_commands:
        print("thanks for trusting ticky your no.1 ticket classifier")
        break
    classified = classify(message, categories)
    ticky_response = respond(classified, categories, general_response )
    print("ticky:", ticky_response)
    ticket_count += 1
print(f"you submitted: {ticket_count} ticket(s)")