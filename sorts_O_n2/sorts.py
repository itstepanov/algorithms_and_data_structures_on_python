def insert_sort(a: list):
    """
    Сортировка списка a вставками
    :param a: not sorted list
    :return: sorted list
    """
    N = len(a)
    for top in range(1, N):
        k = top
        while k > 0 and a[k] < a[k - 1]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1
    return a


def choice_sort(a: list):
    """
    Сортировка списка a выбором
    :param a: not sorted list
    :return: sorted list
    """
    N = len(a)
    for pos in range(N - 1):
        for k in range(pos + 1, N):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
    return a


def bubble_sort(a: list):
    """
    Сортировка списка а методом пузырька
    :param a: not sorted list
    :return: sorted list
    """
    N = len(a)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
    return a


def test_sort(sort_algorithm):
    print("Testing sort algorithm:", sort_algorithm.__name__)
    print("Test case #1: ", end="")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    print("Ok" if a_sorted == sort_algorithm(a) else "Fail")

    print("Test case #2: ", end="")
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))
    print("Ok" if a_sorted == sort_algorithm(a) else "Fail")

    print("Test case #3: ", end="")
    a = [4, 2, 4, 2, 1]
    a_sorted = [1, 2, 2, 4, 4]
    print(("Ok" if a_sorted == sort_algorithm(a) else "Fail"))

    print("Test case #4: ", end="")
    a = []
    a_sorted = []
    print(("Ok" if a_sorted == sort_algorithm(a) else "Fail") + "\n")


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
