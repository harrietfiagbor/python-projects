from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    category = question["category"]
    new_question = Question(text, answer, category)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your score is: {quiz.score}/{quiz.question_number}")