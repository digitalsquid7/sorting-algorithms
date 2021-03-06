from common.sort_timer import SortTimer
from common.sorting_algorithm_factory import sorting_algorithm_factory


def main():
    """Compares the average time to sort unordered lists with various sorting algorithms."""

    algorithm_names = (
        "Bubble Sort",
    )

    sort_timer = SortTimer(-10000, 10000, 1500, 20)

    print(" Average time to sort ".center(50, "*"))

    for algorithm_name in algorithm_names:
        sorting_algorithm = sorting_algorithm_factory(algorithm_name)
        average_time = sort_timer.average_sort_time(sorting_algorithm)
        average_time_formatted = "{:.3f}".format(average_time)
        print(f"{algorithm_name}: {average_time_formatted} seconds / list")


if __name__ == "__main__":
    main()
