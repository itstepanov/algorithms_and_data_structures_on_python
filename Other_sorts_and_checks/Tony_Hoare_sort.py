#  a.k.a. Quicksort / qsort


def hoare_sort(A):
    if len(A) <= 1:
        return A
    barrier = A[0]
    L = list()
    M = list()
    R = list()
    for element in A:
        if element < barrier:
            L.append(element)
        elif element == barrier:
            M.append(element)
        else:  # element > barrier
            R.append(element)
    L = hoare_sort(L)
    R = hoare_sort(R)
    A[:] = L + M + R
    return A


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
    a = [-1, ]
    a_sorted = [-1, ]
    print(("Ok" if a_sorted == sort_algorithm(a) else "Fail"))

    print("Test case #5: ", end="")
    a = []
    a_sorted = []
    print("Ok" if a_sorted == sort_algorithm(a) else "Fail")


if __name__ == '__main__':
    test_sort(hoare_sort)
