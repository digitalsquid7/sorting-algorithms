import unittest

from common.sorting_algorithm_factory import sorting_algorithm_factory
from common.algorithms import SortingAlgorithm


class TestSortingAlgorithmFactory(unittest.TestCase):

    def test_valid_input(self):
        algorithm = sorting_algorithm_factory("Bubble Sort")
        self.assertIsInstance(algorithm, SortingAlgorithm)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sorting_algorithm_factory("Not A Valid Algorithm Name")


if __name__ == '__main__':
    unittest.main()
