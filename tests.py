from unittest import TestCase
from question1 import question1


class TestSolutions(TestCase):

    def test_question_one(self):
        self.assertEquals(False, question1("ababa", "fa"))
        self.assertEquals(True, question1("udacity", "ad"))
