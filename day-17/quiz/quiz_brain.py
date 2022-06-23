class QuizBrain:
    def __init__(self, question_list):
        """ Constructor for QuiZBrain adding a question list to the quiz"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """ Prints the question, handles the user response and updates scores"""
        current_question = self.question_list[self.question_number]
        # Increase the number first, so the Question number display starts from 1 and not zero-
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False)?: ").capitalize()

        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """ Returns true if there are questions left or flase otherwise"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """ Checks if the user's answer matches the data answer for a question. Updates scores and displays progress
        and correct answer to the user"""
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
