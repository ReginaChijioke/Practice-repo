questions = {
    "Q001" : "Q1. Ticket T001 is open and unassigned. A user tries to move it to in_progress.",
    "Q002" : "Q2. The app has zero tickets. What should resolution percentage display?",
    "Q003" : "Q3. Filter title='wifi', category='Network', status='open'. Which records should match?",
    "Q004" : "Q4. A resolved ticket receives 'Add note'. What should happen?",
    "Q005" : "Q5. The JSON file includes two tickets with the same ID. What should load do?",
    "Q006" : "Q6. A PR changes validation but has no negative-case tests. Best review action?"
}


options = {
    "Q001" : ["A. Accept","B. Reject and preserve all data","C. Resolve it automatically","D. Remove ticket"],
    "Q002" : ["A. Crash","B. 100%","C. 0%","D. Divide by one without explanation"],
    "Q003" : ["A. Any record matching one filter","B. Only records matching all supplied filters","C. All network records","D. All open records"],
    "Q004" : ["A. Append anyway","B. Delete old notes","C. Reject until reopened","D. Change status silently"],
    "Q005" : ["A. Keep both","B. Replace memory with duplicates","C. Reject the load without changing current memory","D. Rename IDs silently"],
    "Q006" : ["A. Approve because it runs","B. Request focused tests and reasoning","C. Merge immediately","D. Ask AI to approve it"]
}


answer_key = {
    "Q001" : "B",
    "Q002" : "C",
    "Q003" : "B",
    "Q004" : "C",
    "Q005" : "C",
    "Q006" : "B",
}

submitted_answers = {}

valid_options = ["A","B","C","D"]
for id in questions:
    question = questions[id]
    option = options[id]
    
    print(question)
    print("\n".join(option))

    user_input = input("Input your answer(A,B,C or D): ").strip().upper()
    while user_input not in valid_options:
        print("Invalid option. Please try again")
        user_input = input("Input your answer(A,B,C or D): ").strip().upper()
    
    submitted_answers[id] = user_input

    

def calculate_score(submitted_answers, answer_key):
    score = 0 
    for id in answer_key:
        submitted_answer = submitted_answers[id]
        correct_answer = answer_key[id]

        if submitted_answer == correct_answer:
            score += 1
    return score 
final_score = calculate_score(submitted_answers, answer_key)
print("Quiz complete!")
print(f"You scored {final_score} out of 6.")

def review_answer(submitted_answers, answer_key):
    for id in answer_key:
        submitted_answer = submitted_answers[id]
        correct_answer = answer_key[id]
        if submitted_answer != correct_answer:
            print(id)
            print(submitted_answer)
            print(correct_answer)
