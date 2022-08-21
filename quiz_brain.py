class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        new_question = self.question_list[self.question_number].question
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {new_question} (True/False): ")
        self.check_the_answer(user_answer.lower(), correct_answer.lower())

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_the_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You have got it right")
        else:
            print("You have got it wrong")


















# class QuizBrain:
#
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.score = 0
#         self.question_list = q_list
#
#     def still_has_questions(self):
#         return self.question_number < len(self.question_list)
#
#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         player_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
#         self.check_answer(player_answer, current_question.answer)
#
#     def check_answer(self, player_answer, current_answer):
#         if player_answer.lower() == current_answer.lower():
#             self.score += 1
#             print("You have got it right")
#         else:
#             print("You have got it wrong")
#         print(f"The correct answer was: {current_answer}")
#         print(f"Your current score is {self.score}/{self.question_number}\n")
#
#
#
