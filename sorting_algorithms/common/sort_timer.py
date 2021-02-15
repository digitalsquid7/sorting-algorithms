from time import time
from random import randint

from common.algorithms import SortingAlgorithm


class SortTimer:
    """Time how long it takes to sort unordered lists."""

    def __init__(self, min_value: int, max_value: int, values_per_list: int, number_of_lists: int):
        """Generate the list of unordered lists that can be used to test average times of sorting algorithms.

        Parameters
        ----------
        min_value : int
        max_value : int
        values_per_list: int
        number_of_lists: int
        """

        self.unordered_lists = []

        for _ in range(number_of_lists):
            unordered_list = [randint(min_value, max_value) for _ in range(values_per_list)]
            self.unordered_lists.append(unordered_list)

    def average_sort_time(self, sorting_algorithm: SortingAlgorithm) -> float:
        """Get the average time taken to sort the unordered_lists defined on object creation.

        Parameters
        ----------
        sorting_algorithm: SortingAlgorithm

        Returns
        -------
        Average time to sort all unordered lists.
        """

        total_times = []

        for unordered_list in self.unordered_lists:
            start_time = time()
            sorting_algorithm.sort(unordered_list)
            end_time = time()

            total_times.append(end_time - start_time)

        average_time = sum(total_times) / len(total_times)

        return average_time
