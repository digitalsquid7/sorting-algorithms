import src.sorting_algorithms as sa


def sorting_algorithm_factory(algorithm_name: str) -> sa.SortingAlgorithm:
    """Get a sorting algorithm object from the name provided.

    Parameters
    ----------
    algorithm_name: str

    Returns
    -------
    SortingAlgorithm
    """

    algorithm_mapping = {
        "Bubble Sort": sa.BubbleSort
    }

    sorting_algorithm = algorithm_mapping.get(algorithm_name)

    if sorting_algorithm is None:
        raise ValueError("algorithm_name provided is not valid.")

    return sorting_algorithm()
