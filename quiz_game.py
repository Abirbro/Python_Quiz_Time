import time

# List of questions and answers
questions = [
    {
        "question": "What is the keyword used to define a function in Python?",
        "options": ["a) def", "b) func", "c) function", "d) define"],
        "answer": "a"
    },
    {
        "question": "Which data type is used to store a sequence of characters?",
        "options": ["a) list", "b) string", "c) tuple", "d) dictionary"],
        "answer": "b"
    },
    {
        "question": "Which of the following is NOT a valid variable name?",
        "options": ["a) _variable", "b) variable123", "c) 123variable", "d) variable_123"],
        "answer": "c"
    },
    {
        "question": "Which operator is used to compare two values in Python?",
        "options": ["a) =", "b) =", "c) ==", "d) !="],
        "answer": "c"
    }
]

def ask_question(question, options, correct_answer):
    """
    Displays a question, accepts user input, and checks if the answer is correct.
    """
    print(question)
    for option in options:
        print(option)

    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == correct_answer:
        return True
    else:
        return False