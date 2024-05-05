from data import question_data2, question_data2
from question_model import Questions
from quiz_brain import QuizBrain

question_bank = []
for question in question_data2:
    q = question["question"]
    a = question["correct_answer"]
    new_question = Questions(q_text = q, q_answer=a)
    question_bank.append(new_question)

new_quiz = QuizBrain(q_list = question_bank)

while new_quiz.still_has_questions() is True:
    answer = new_quiz.next_question()

print("You completed the quiz!")
print(f"You final score is: {new_quiz.score}/{len(question_bank)}")