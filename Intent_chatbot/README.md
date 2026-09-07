MyPaddi Chatbot
WHAT IT DOES
MyPaddi is a simple rule-based chatbot that allows users to have a basic conversation through the terminal. It recognizes different types of messages, such as greetings, questions about its name, time-related questions, jokes, and goodbyes, and responds with a randomly selected response.

SUPPORTED INTENTS

* `greetings` — Example: `"hi"`
* `ask_name` — Example: `"what is your name"`
* `ask_time` — Example: `"what is the time"`
* `joke` — Example: `"tell me a joke"`
* `goodbye` — Example: `"bye"`

HOW TO RUN IT
Make sure Python is installed, then run:

```bash
python main.py

```

The project uses only Python's standard library. It uses modules such as `string` and `random`, which are included with Python, so no external packages need to be installed with `pip`.
How to exit
The conversation ends when the user enters:

* `exit`
* `bye`
* `quit`

PROJECT STRUCTURE

* `main.py` — Runs the chatbot conversation loop, handles user input, checks exit phrases, and counts exchanges.
* `nlp_utils.py` — Cleans user input and matches it to an intent.
* `intents.py` — Contains `INTENT_MAP`, which defines the phrases that trigger each intent.
* `responses.py` — Contains `RESPONSE_MAP` and `get_response()`, which selects a random response for the matched intent and provides a fallback when no intent is matched.

KNOWN LIMITATIONS / NEXT STEPS

* Hardcoded time responses: The `ask_time` responses currently contain fixed times such as `"3:30pm"` and `"4pm WAT"`, so the chatbot does not know the actual current time.
* First-match-wins intent matching: `match_intent()` returns the first matching intent it finds. If a message could match multiple intents, the chatbot does not compare the matches to determine which one is most appropriate.
* Limited understanding: The chatbot only recognizes phrases that are included in `INTENT_MAP` or contain those phrases.
* No conversation memory: The chatbot does not remember previous messages or use conversation history to understand later messages.
* Basic fallback: When the chatbot cannot identify an intent, it uses a generic fallback response rather than asking a more context-aware question.

POSSIBLE NEXT STEPS
Future versions could use the actual current time, improve intent matching, handle ambiguous messages, expand the number of recognized phrases, and add conversation memory.