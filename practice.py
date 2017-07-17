"""
Parts 1-4
Create your classes and class methods here according to the practice instructions.
As you are working on Parts 1, 2, and 4, you can run the test python file
corresponding to that section to verify that you are completing the problem
correctly.
ex: python part_1_tests.py.
"""


class Student(object):
    """Capture personal data about student."""

    def __init__(self, first_name, last_name, address):
        """Define name and address at initialization."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Capture question and correct answer"""

    def __init__(self, question, correct_answer):
        """define question and answer at initialization."""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Ask random question from test; evaluate T/F."""

        # print q to console
        # prompt user for answer
        # return T/F
        ## ex call: e.questions[0].ask_and_evaluate()
        user_i = raw_input('{} > '.format(self.question))
        if user_i == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """Capture exam data"""

    def __init__(self, name):
        """Define exam name and set at initialization."""

        self.name = name
        self.questions = []

    def add_question(self, question_label):
        """Add Question to (type of) exam questions list."""

        # add label to questions list
        self.questions.append((question_label))

    def administer(self):
        """Ask all q's and return score."""

        # assign how many items to count, 0 for score
        # loop over questions, if correct add to score
        # divide score after looping by count
        question_count = len(self.questions)
        score_right = 0
        for i in range(len(self.questions)):
            check = self.questions[i].ask_and_evaluate()
            if check is True:
                score_right += 1
        score = score_right / float(question_count)
        return score


class StudentExam(object):
    """Student to take exam, capture data."""

    def __init__(self, name, exam, score=None):
        """Instantiate name, exam, score for student"""
        self.name = name
        self.exam = exam
        self.score = score

    def take_test(self):
        """Administer exam and set score."""

        score = self.exam.administer()

