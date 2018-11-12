def merge(A: list, B: list):
    """
    Делаем слияние 2-х отсортированных массивов в один
    """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(A: list):
    """
    Рекурсивная функция сортировки слиянием
    """
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left_half = A[0:middle]
    right_half = A[middle:len(A)]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    C = merge(left_half, right_half)
    A[:] = C[:]
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
    a = []
    a_sorted = []
    print("Ok" if a_sorted == sort_algorithm(a) else "Fail")


if __name__ == '__main__':
    test_sort(merge_sort)
