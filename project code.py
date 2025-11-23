import random
import time

def timed_math_challenge():
    num_questions = 10
    correct_answers = 0
    start_time = time.time()
    results = [] # It is to store problems, user answers, and correct answers

    print(f"You have {num_questions} math questions let's see how fast you can answer. Start!")

    for i in range(num_questions):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])

        problem_string = f"Question {i + 1}: What is {num1} {operator} {num2}? "

        correct_result = 0
        if operator == '+':
            correct_result = num1 + num2
        elif operator == '-':
            correct_result = num1 - num2
        else:                             # for operator == '*'
            correct_result = num1 * num2

        user_answer = None
        try:
            user_answer = int(input(problem_string))
            if user_answer == correct_result:
                correct_answers += 1
        except ValueError:
            print("That's not a valid answer. Skipping this question.")

        results.append({
            'question': problem_string.strip(),
            'user_answer': user_answer,
            'correct_answer': correct_result,
            'is_correct': (user_answer == correct_result)
        })

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print(f"\nChallenge complete! You answered {correct_answers} out of {num_questions} questions correctly in {total_time} seconds.")

    review_choice = input("Do you want to review the answers? (yes/no): ").lower()

    if review_choice == 'yes':
        print("\n---- Answers Review ----")
        for i, res in enumerate(results):
            print(f"Question {i + 1}: {res['question']}")
            print(f"Your answer: {res['user_answer'] if res['user_answer'] is not None else 'No valid answer'}")
            print(f"Correct answer: {res['correct_answer']}")
            if res['is_correct']:
                print("Result: Correct!")
            else:
                print("Result: Incorrect.")
            print("-------------------------")
    else:                                     # If the review choice is No
      print(f"Try again to solve less than {total_time} seconds.")        

timed_math_challenge()
