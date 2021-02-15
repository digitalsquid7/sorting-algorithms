import unittest

from src.sort_timer import SortTimer
from src.sorting_algorithms import BubbleSort


class TestSortTimer(unittest.TestCase):

    def test_average_sort_time_return_type(self):
        sort_timer = SortTimer(0, 10, 5, 5)
        bubble_sort = BubbleSort()
        average_time = sort_timer.average_sort_time(bubble_sort)
        self.assertIsInstance(average_time, float)


if __name__ == '__main__':
    unittest.main()
