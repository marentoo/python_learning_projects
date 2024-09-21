import html 

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        length = len(self.question_list)
        return self.question_number < length

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}:{html.unescape(self.current_question.text)}?"


    def check_answer(self, user_answer):
        ground_truth_answer = self.current_question.answer
        if user_answer.lower() == ground_truth_answer.lower():
            self.score += 1
            # print("Correct")
            return True
        else:
            # print("Inccorrect")
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")


