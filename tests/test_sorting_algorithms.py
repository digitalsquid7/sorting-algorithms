import unittest

import sorting_algorithms.common.algorithms as sa


class TestBase:

    class TestSortingAlgorithm(unittest.TestCase):
        """Tests to perform on each sorting algorithm."""

        @classmethod
        def setUpClass(cls):
            cls.sorting_algorithm = None

        def test_unordered_list(self):
            unordered = [5, 2, 9, 14, 98, 355, 32, 28, 4, 3, 3, 93, 1]
            ordered = self.sorting_algorithm.sort(unordered)
            expected = [1, 2, 3, 3, 4, 5, 9, 14, 28, 32, 93, 98, 355]
            self.assertEqual(expected, ordered)

        def test_descending_list(self):
            descending = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            ordered = self.sorting_algorithm.sort(descending)
            expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            self.assertEqual(expected, ordered)

        def test_ascending_list(self):
            descending = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            ordered = self.sorting_algorithm.sort(descending)
            self.assertEqual(descending, ordered)

        def test_negative_list(self):
            unordered = [-345, -23222, -3453, -23, -1, -2354, -87, -22]
            ordered = self.sorting_algorithm.sort(unordered)
            expected = [-23222, -3453, -2354, -345, -87, -23, -22, -1]
            self.assertEqual(expected, ordered)

        def test_mixed_list(self):
            unordered = [234, -345, 3453, -23, -1, 0, -87, 30, 90, -4]
            ordered = self.sorting_algorithm.sort(unordered)
            expected = [-345, -87, -23, -4, -1, 0, 30, 90, 234, 3453]
            self.assertEqual(expected, ordered)

        def test_float_list(self):
            unordered = [234.232, 2.334, 0.1212, -12.43322, -1001.232222, 20.]
            ordered = self.sorting_algorithm.sort(unordered)
            expected = [-1001.232222, -12.43322, 0.1212, 2.334, 20.0, 234.232]
            self.assertEqual(expected, ordered)


class TestBubbleSort(TestBase.TestSortingAlgorithm):

    @classmethod
    def setUpClass(cls):
        cls.sorting_algorithm = sa.BubbleSort()


if __name__ == '__main__':
    unittest.main()
