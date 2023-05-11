import unittest
from answer import approx_tsp_cheap, approx_tsp_cheap_and_far


class TestTSPMethods(unittest.TestCase):
    def setUp(self):
        self.matrix1 = [[0, 10, 15, 20], [10, 0, 35, 25],
                        [15, 35, 0, 30], [20, 25, 30, 0]]
        self.matrix2 = [[0, 5, 8, 10], [5, 0, 3, 4],
                        [8, 3, 0, 1], [10, 4, 1, 0]]
        self.matrix3 = [[0, 3, 4, 2, 7], [3, 0, 4, 6, 3], [
            4, 4, 0, 5, 8], [2, 6, 5, 0, 6], [7, 3, 8, 6, 0]]
        self.matrix4 = [[0, 2, 3, 4],
                        [3, 0, 7, 5],
                        [5, 8, 0, 6],
                        [3, 5, 4, 0]]
        self.matrix5 = [[0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46, ],
                        [29, 0, 55, 46, 42, 43, 43, 23,
                         23, 31, 41, 51, 11, 52, 21],
                        [82, 55, 0, 68, 46, 55, 23, 43,
                         41, 29, 79, 21, 64, 31, 51, ],
                        [46, 46, 68, 0, 82, 15, 72, 31,
                         62, 42, 21, 51, 51, 43, 64],
                        [68, 42, 46, 82, 0, 74, 23, 52,
                         21, 46, 82, 58, 46, 65, 23, ],
                        [52, 43, 55, 15, 74, 0, 61, 23,
                         55, 31, 33, 37, 51, 29, 59],
                        [72, 43, 23, 72, 23, 61, 0, 42,
                         23, 31, 77, 37, 51, 46, 33],
                        [42, 23, 43, 31, 52, 23, 42, 0,
                         33, 15, 37, 33, 33, 31, 37],
                        [51, 23, 41, 62, 21, 55, 23, 33,
                         0, 29, 62, 46, 29, 51, 11],
                        [55, 31, 29, 42, 46, 31, 31, 15,
                         29, 0, 51, 21, 41, 23, 37],
                        [29, 41, 79, 21, 82, 33, 77, 37,
                         62, 51, 0, 65, 42, 59, 61],
                        [74, 51, 21, 51, 58, 37, 37, 33,
                         46, 21, 65, 0, 61, 11, 55, ],
                        [23, 11, 64, 51, 46, 51, 51, 33,
                         29, 41, 42, 61, 0, 62, 23, ],
                        [72, 52, 31, 43, 65, 29, 46, 31,
                         51, 23, 59, 11, 62, 0, 59],
                        [46, 21, 51, 64, 23, 59, 33, 37, 11, 37, 61, 55, 23, 59, 0]]

    def test_approx_tsp_cheap(self):
        result1 = approx_tsp_cheap(self.matrix1)
        result2 = approx_tsp_cheap(self.matrix2)
        result3 = approx_tsp_cheap(self.matrix3)
        result4 = approx_tsp_cheap(self.matrix4)
        result5 = approx_tsp_cheap(self.matrix5)
        self.assertEqual(result1[-1], 80)
        self.assertEqual(result2[-1], 19)
        self.assertEqual(result3[-1], 21)
        self.assertEqual(result4[-1], 18)
        self.assertEqual(result5[-1], 291)

    def test_approx_tsp_cheap_and_far(self):
        result1 = approx_tsp_cheap_and_far(self.matrix1)
        result2 = approx_tsp_cheap_and_far(self.matrix2)
        result3 = approx_tsp_cheap_and_far(self.matrix3)
        result4 = approx_tsp_cheap_and_far(self.matrix4)
        result5 = approx_tsp_cheap_and_far(self.matrix5)
        self.assertEqual(result1[-1], 80)
        self.assertEqual(result2[-1], 18)
        self.assertEqual(result3[-1], 19)
        self.assertEqual(result4[-1], 17)
        self.assertEqual(result5[-1], 426)
