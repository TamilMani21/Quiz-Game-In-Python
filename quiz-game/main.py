from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    Q_text = i["question"]
    Q_answer = i["correct_answer"]
    n_question = Question(text=Q_text, answer=Q_answer)
    question_bank.append(n_question)

quzi = QuizBrain(question_bank)

while quzi.still_has_method():
    quzi.next_question()

print("You completed the quiz👏")
print(f"Your final score was: {quzi.score}/{quzi.ques_num}")
