from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    the_question = question["question"]
    the_answer = question["correct_answer"]
    # print(f"{the_question} \n {the_answer}")
    new_question = Question(the_question, the_answer)
    question_bank.append(new_question)

# print(question_bank[0].question)
# print(question_bank[0].answer)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()













# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
# question_bank = []
#
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
#
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You have completed the quiz")
# print(f"Your final score is: {quiz.score}/{quiz.question_number}")