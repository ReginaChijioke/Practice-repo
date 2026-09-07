from nlp_utils import clean_input, match_intent
from responses import get_response, RESPONSE_MAP
from intents import INTENT_MAP

exit_phrases = {"exit", "bye", "quit"}
exchange_count = 0
while True:
    raw_input = input("You: ")
    cleaned = clean_input(raw_input)
    if cleaned in exit_phrases:
        print("see ya")
        break

    matched_intent = match_intent(clean_input, INTENT_MAP)
    bot_response = get_response(matched_intent, RESPONSE_MAP)
    print("Bot:", bot_response)
    exchange_count += 1
print(exchange_count)

