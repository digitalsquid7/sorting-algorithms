import abc


class SortingAlgorithm(abc.ABC):
    """Base class for all sorting algorithms."""

    @abc.abstractmethod
    def sort(self, unordered_list: list) -> list:
        """Sorts an unordered list of numbers.

        Parameters
        ----------
        unordered_list: an unordered list of numbers that needs to be sorted in ascending order.

        Returns
        -------
        list
            ordered version of the unordered_list provided
        """
        pass


class BubbleSort(SortingAlgorithm):
    """ A simple and inefficient sorting algorithm.

    Repeatedly switches adjacent values in the list that are out of order until the list is ordered.
    """

    def sort(self, unordered_list):

        last = len(unordered_list) - 1
        swap = True

        while swap and 0 < last:

            swap = False

            for index in range(last):

                if unordered_list[index] > unordered_list[index + 1]:
                    temp = unordered_list[index]
                    unordered_list[index] = unordered_list[index + 1]
                    unordered_list[index + 1] = temp
                    swap = True

            last -= 1

        return unordered_list
