"""
input data examples
"""
hamster_in_1 = [19, 4, (5, 0), (2, 2), (1, 4), (5, 1)]
hamster_in_2 = [7, 3, (1, 2), (2, 2), (3, 1)]
hamster_in_3 = [2, 2, (1, 50000), (1, 60000)]


def count_hamsters_max_count(hamster_in):
    """
    Finds number of hamsters that can be fed this day considering task conditions
    >>> count_hamsters_max_count(hamster_in_1)
    3

    >>> count_hamsters_max_count(hamster_in_2)
    2

    >>> count_hamsters_max_count(hamster_in_3)
    1

    """
    most_voracious_hamster = None
    most_voracious_hamster_hunger, hamsters_to_feed_hunger = 0, 0
    for hamster_index in range(2, len(hamster_in)):
        current_hamster_hunger = hamster_in[hamster_index][0] + hamster_in[hamster_index][1] * (len(hamster_in) - 3)
        hamsters_to_feed_hunger += current_hamster_hunger
        if most_voracious_hamster_hunger < current_hamster_hunger:
            most_voracious_hamster_hunger = current_hamster_hunger
            most_voracious_hamster = hamster_index
    if hamsters_to_feed_hunger <= hamster_in[0]:
        return len(hamster_in) - 2
    else:
        hamster_in.pop(most_voracious_hamster)
        return count_hamsters_max_count(hamster_in)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)