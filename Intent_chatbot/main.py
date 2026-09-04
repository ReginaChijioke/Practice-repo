from nlp_utils import clean_input, match_intent
from responses import get_response, RESPONSE_MAP
from intents import INTENT_MAP

exit_phrases = {"exit", "bye", "quit"}

while True:
    raw_input = input("You: ")
    cleaned = clean_input(raw_input)
    if cleaned in exit_phrases:
        print("see ya")
        break

