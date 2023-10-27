import random
from quiz_data import quiz_data
from question import Question

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def load_questions(self):
        for card in quiz_data["cards"]:
            question = Question(card["question"], card["good_answers"], card["bad_answers"])
            self.questions.append(question)
            random.shuffle(self.questions)

    def start_quiz(self):
        for i, question in enumerate(self.questions):
            print("==============================")
            print(f"Question {i + 1}: {question.question_text}")
            print("==============================")
            answers = question.good_answers + question.bad_answers
            random.shuffle(answers)

            for j, answer in enumerate(answers, start=1):
                print(f"{j}. {answer}")

            print("==============================")
            
            user_input = input("Choisissez 1, 2, ou 3: ").strip()

            # Use a while loop to keep asking until the user provides a valid input
            while user_input not in ["1", "2", "3"]:
                print("Entrée invalide. Choisissez 1, 2, ou 3.")
                user_input = input("Choisissez 1, 2, ou 3: ").strip()

            correct_answer_index = answers.index(question.good_answers[0]) + 1
            if user_input == str(correct_answer_index):
                self.score += 1

        self.display_score()    


    def display_score(self):
        print(f"Votre score : \033[1m{self.score}/{len(self.questions)}\033[0m")
        print("Corrigé :")
        for i, question in enumerate(self.questions):
            print(f"{i + 1}. {question.question_text}: \033[1m{', '.join(question.good_answers)}\033[0m")
