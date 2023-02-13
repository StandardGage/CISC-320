import unittest
import answer


class TestConvertToList(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(answer.convertToList(
            '1\n2\n3\n4\n5'), [1, 2, 3, 4, 5])
        self.assertEqual(answer.convertToList(''), [])
        self.assertEqual(answer.convertToList(
            '-5\n12\n100000\n-100000\n0'), [-5, 12, 100000, -100000, 0])


class TestgetValidSum(unittest.TestCase):
    def test_validSum(self):
        self.assertEqual(answer.getValidSum([6, 5, 10, -3, 15, -999, 13]), 30)
        self.assertEqual(answer.getValidSum([]), 'EMPTY')
        self.assertEqual(answer.getValidSum([-999]), 'EMPTY')
        self.assertEqual(answer.getValidSum([3, 0, 0, 0, 0]), 0)
