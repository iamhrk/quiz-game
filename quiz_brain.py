class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """check to see if there are still questions to be asked from the list"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """asks questions one by one from the list and call check_answer() method"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"{self.question_number}. {current_question.question} (True/False)? ")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, u_input, corr_answer):
        """verify if the answer from user is correct or not."""
        if u_input.lower() == corr_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Current Score: {self.score}/{self.question_number}\n\n")
        else:
            print("That's wrong.")
            print(f"The correct answer was {corr_answer}")
            print(f"Current Score: {self.score} / {self.question_number}\n\n")