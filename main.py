from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    question_bank.append(Question(question, answer))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You completed the quiz!\nYour final score is : {quiz.score}/{quiz.question_number}\n")

