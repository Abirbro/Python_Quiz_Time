import time

def read_questions_from_file(file_path):
    """
    Reads questions and answers from a .txt file and returns them in a structured format.
    """
    questions = []
    with open(file_path, 'r') as file:
        question_data = {}
        options = []
        
        for line in file:
            line = line.strip()
            
            # Detect question line
            if line.endswith('?'):
                if question_data:
                    question_data['options'] = options
                    questions.append(question_data)
                question_data = {'question': line, 'options': [], 'answer': None}
            elif line.startswith('answer:'):
                question_data['answer'] = line.split(':')[1].strip()
            else:
                options.append(line)
        
        # Append the last question
        if question_data:
            question_data['options'] = options
            questions.append(question_data)
    
    return questions

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
    
def start_quiz(file_path):
    """
    Starts the quiz, asks questions, and keeps track of the score.
    """
    score = 0
    start_time = time.time()
    
    questions = read_questions_from_file(file_path)
    
    # Loop through each question
    for question_data in questions:
        question = question_data['question']
        options = question_data['options']
        correct_answer = question_data['answer']
        
        if ask_question(question, options, correct_answer):
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")
    
    # Calculate time taken
    time_taken = round(time.time() - start_time, 2)
    print(f"Quiz finished! You got {score}/{len(questions)} correct!")
    print(f"Time taken: {time_taken} seconds.")

# Start the quiz
if __name__ == "__main__":
    # Make sure the file is in the same directory as your script or provide the correct path
    start_quiz('questions.txt')
