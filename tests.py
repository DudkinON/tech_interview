from unittest import TestCase
from question1 import question1
from question2 import question2


class TestSolutions(TestCase):

    def test_question_one(self):
        self.assertEquals(False, question1("ababa", "fa"))
        self.assertEquals(True, question1("udacity", "ad"))

    def test_question_two(self):
        self.assertEquals("aba", question2("abaandaba"))
        self.assertEquals("", question2("dart"))
