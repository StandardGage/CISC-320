import unittest
from answer import *


class TestParseText(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(parseLogs(''), '')

    def test_single_empty(self):
        self.assertEqual(parseLogs('1'), '')

    def test_single_valid(self):
        self.assertEqual(parseLogs('1\n1 P 10 10'), [['1', 'P', '10', '10']])

    def test_multi_valid(self):
        self.assertEqual(parseLogs('3\n1 P 10 10\n2 S 3 3\n1 S 10 10'), [
                         ['1', 'P', '10', '10'], ['2', 'S', '3', '3'], ['1', 'S', '10', '10']])


class TestFillStudents(unittest.TestCase):
    def test_empty(self):
        students = {}
        fillStudents('')
        self.assertEqual(students, {})

    def test_single_invalid(self):
        students = fillStudents([['1', 'P', '10', '10']])
        self.assertEqual(students, {1: {
                         'lowestPageID': 10, 'latestPageID': 10, 'totalScore': 0, 'scoresSubmitted': 0, 'averageScore': 0}})

    def test_lowest_page(self):
        students = fillStudents(
            [['1', 'P', '10', '10'], ['1', 'P', '9', '10']])
        self.assertEqual(students, {1: {
                         'lowestPageID': 9, 'latestPageID': 9, 'totalScore': 0, 'scoresSubmitted': 0, 'averageScore': 0}})

    def test_score(self):
        students = fillStudents(
            [['1', 'S', '10', '10'], ['1', 'S', '9', '10']])
        self.assertEqual(students, {1: {
                         'lowestPageID': None, 'latestPageID': None, 'totalScore': 19, 'scoresSubmitted': 2, 'averageScore': 0}})

    def test_full_student(self):
        students = fillStudents([['1', 'P', '10', '10'], [
            '1', 'P', '9', '10'], ['1', 'S', '9', '10']])
        self.assertEqual(students, {1: {
                         'lowestPageID': 9, 'latestPageID': 9, 'totalScore': 9, 'scoresSubmitted': 1, 'averageScore': 0}})

    def test_multi_students(self):
        students = fillStudents([['1', 'P', '10', '10'], ['2', 'P', '20', '5'], [
            '1', 'P', '9', '10'], ['1', 'S', '9', '10'], ['2', 'S', '5', '5'], ['2', 'S', '5', '5'], ['3', 'P', '4', '3']])
        self.assertEqual(students, {1: {'lowestPageID': 9, 'latestPageID': 9, 'totalScore': 9, 'scoresSubmitted': 1, 'averageScore': 0},
                                    2: {'lowestPageID': 20, 'latestPageID': 20, 'totalScore': 10, 'scoresSubmitted': 2, 'averageScore': 0},
                                    3: {'lowestPageID': 4, 'latestPageID': 4, 'totalScore': 0, 'scoresSubmitted': 0, 'averageScore': 0}})


STUDENTS1 = {1: {'lowestPageID': None, 'latestPageID': None,
                 'totalScore': 19, 'scoresSubmitted': 2}}
STUDENTS2 = {1: {'lowestPageID': 9, 'latestPageID': 10,
                 'totalScore': 9, 'scoresSubmitted': 1}}
STUDENTS3 = {1: {'lowestPageID': 9, 'latestPageID': 10, 'totalScore': 9, 'scoresSubmitted': 1},
             2: {'lowestPageID': 20, 'latestPageID': 20, 'totalScore': 10, 'scoresSubmitted': 2},
             3: {'lowestPageID': 4, 'latestPageID': 4, 'totalScore': 0, 'scoresSubmitted': None}}
