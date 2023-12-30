class Question:
    def __init__(self, question_text, options, correct_option_index):
        self.question_text = question_text
        self.options = options
        self.correct_option_index = correct_option_index

    def display_question(self):
        print(self.question_text)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def is_correct(self, selected_option_index):
        return selected_option_index == self.correct_option_index


class Quiz:
    def __init__(self, quiz_name, questions):
        self.quiz_name = quiz_name
        self.questions = questions

    def take_quiz(self, user):
        user_score = 0
        for question in self.questions:
            question.display_question()
            selected_option_index = int(input("Enter your answer (1, 2, 3, ...): ")) - 1

            if 0 <= selected_option_index < len(question.options):
                if question.is_correct(selected_option_index):
                    print("Correct!\n")
                    user_score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.options[question.correct_option_index]}\n")
            else:
                print("Invalid option. Skipping to the next question.\n")

        print(f"Quiz completed! Your score: {user_score}/{len(self.questions)}")
        return user_score


class User:
    def __init__(self, username):
        self.username = username

    def take_quiz(self, quiz):
        return quiz.take_quiz(self)

question1 = Question("What is the capital of India?", ["Mumbai", "Delhi", "London"], correct_option_index=1)
question2 = Question("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars"], correct_option_index=1)

quiz1 = Quiz("General Knowledge Quiz", [question1, question2])

user1 = User("u1")

user1_score = user1.take_quiz(quiz1)

