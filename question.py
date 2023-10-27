import random

class Question:
    def __init__(self, question_text, good_answers, bad_answers):
        self.question_text = question_text
        self.good_answers = good_answers
        self.bad_answers = bad_answers

    def shuffle_answers(self):
        combined_answers = self.good_answers + self.bad_answers
        random.shuffle(combined_answers)
        self.good_answers = combined_answers[:len(self.good_answers)]
        self.bad_answers = combined_answers[len(self.good_answers):]
        
        # Call shuffle_answers to shuffle answers during question creation
        self.shuffle_answers()