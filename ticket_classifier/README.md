Ticky — Ticket Classifier
WHAT IT DOES

Ticky is a simple rule-based ticket classifier that categorizes user complaints into Billing, Technical, Account, or General and returns an appropriate response.

HOW IT WORKS

The user types a complaint, which is first passed through `clean_text()` to remove punctuation, whitespace, and capitalization differences. The cleaned message is then passed to `classify()`, which checks the words against each category's keywords and scores the matches. The category with the highest score is selected. Finally, `respond()` uses the selected category to return its canned response, or a fallback response if no category matches.

FILE STRUCTURE

* `main.py` — handles user input, the interaction loop, exit commands, ticket counting, and connects the different functions together.
* `text_utils.py` — contains the `clean_text()` function that cleans and normalizes user input.
* `categories.py` — stores the ticket categories, their keywords, and their canned responses.
* `classifier.py` — contains the `classify()` function for categorizing tickets and the `respond()` function for returning the appropriate response.

HOW TO RUN

```bash
python3 main.py
```

EXAMPLE USAGE

```text
how may i help you: i was charged twice
ticky: Your complaints have been sent to our billing team.

how may i help you: the weather is nice today
ticky: Your Complaint doesn't match any category,please try again

how may i help you: exit
thanks for trusting ticky your no.1 ticket classifier
you submitted: 2 ticket(s)
```

CATEGORIES SUPPORTED

* Billing — triggered by words like `charged`, `payment`, `debited`, `money`
* Technical — triggered by words like `error`, `crashed`, `load`, `glitching`, `froze`, `bug`
* Account — triggered by words like `restricted`, `password`, `forgotten`, `locked`
* General — fallback when no keywords match

KNOWN LIMITATIONS

Ticky currently uses exact-word matching for its keywords. For example, the keyword `crashed` will match `crashed`, but `crashing` will not match because it is a different word. This was accepted for now to keep the classifier simple and focus on the core functionality.

POSSIBLE IMPROVEMENTS

* Use substring or word-stemming techniques so related words such as `crashed` and `crashing` can be recognized.
* Add more keywords to improve classification accuracy.
* Add ticket logging so submitted tickets can be stored and reviewed later.