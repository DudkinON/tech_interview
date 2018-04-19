from unittest import TestCase
from question1 import question1
from question2 import question2
from question3 import question3
from question4 import question4
from question5 import question5, List


class TestSolutions(TestCase):

    def test_question_one(self):
        self.assertEquals(False, question1("ababa", "fa"))
        self.assertEquals(True, question1("udacity", "ad"))

    def test_question_two(self):
        self.assertEquals("aba", question2("abaandaba"))
        self.assertEquals("", question2("dart"))

    def test_question_three(self):
        self.assertEquals(
            {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]},
            question3(
                {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}))
        self.assertEquals(
            {'A': [('B', 2)],
             'B': [('A', 2), ('C', 5)],
             'C': [('B', 5)]},
            question3(
                {'A': [('B', 2), ('C', 6)],
                 'B': [('A', 2), ('C', 5)],
                 'C': [('B', 5), ('A', 6)]}))
        self.assertEquals(
            {'A': [('C', 4)],
             'C': [('B', 2), ('A', 4)], 'B': [('C', 2), ('D', 3)],
             'E': [('F', 1), ('D', 2)], 'D': [('E', 2), ('B', 3), ('G', 6)],
             'G': [('H', 2), ('D', 6)], 'F': [('E', 1)], 'H': [('G', 2)]},
            question3({'A': [('B', 5), ('C', 4)],
                       'B': [('A', 5), ('C', 2), ('D', 3)],
                       'C': [('A', 4), ('B', 2), ('E', 4)],
                       'D': [('B', 3), ('E', 2), ('G', 6)],
                       'E': [('C', 4), ('D', 2), ('F', 1)],
                       'F': [('E', 1), ('G', 8)],
                       'G': [('D', 6), ('F', 8), ('H', 2)], 'H': [('G', 2)]})
        )

    def test_question4(self):
        matrix = [[0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]]
        self.assertEquals(3, question4(matrix, 3, 1, 4))

    def test_question5(self):
        linked_list = List(2)
        linked_list.insert(4)
        linked_list.insert(3)
        linked_list.insert(6)
        linked_list.insert(9)
        linked_list.insert(0)
        self.assertEquals(6, question5(linked_list, 3))
        self.assertEquals(None, question5('linked_list', 2))
        self.assertEquals(None, question5(linked_list, None))
