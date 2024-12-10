class QuizBrain:

    def __init__(self, q_list):
        self.ques_num = 0
        self.score = 0
        self.question_list = q_list
        


    def still_has_method(self):
        return self.ques_num < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.ques_num]
        self.ques_num += 1
        user_answer = input(f"Q.{self.ques_num}:{current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("You got it right😄!")
        else:
            print("Your answer is wrong🫠")
        print(f"The correct answer was: {current_answer}")
        print(f"Your current score:{self.score}/{self.ques_num}")
        print("\n")