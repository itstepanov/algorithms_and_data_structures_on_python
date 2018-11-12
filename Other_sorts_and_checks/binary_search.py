def left_bound(A: list, key):
    left = - 1
    right = len(A)
    if A[0] >= key:
        return left
    if A[-1] < key:
        left = len(A) - 1
        return left
    while right - left > 1:
        mid = (right + left) // 2
        if A[mid] < key:
            left = mid
        else:
            right = mid
    return left


def right_bound(A: list, key):
    left = - 1
    right = len(A)
    if A[0] > key:
        right = 0
        return right
    if A[-1] < key:
        right = len(A)
        return right
    while right - left > 1:
        mid = (right + left) // 2
        if A[mid] <= key:
            left = mid
        else:
            right = mid
    return right


def test_left(func):
    print("Test case 1: ", end='')
    a = [1, 2, 5, 5, 7, 8, 10, 10]
    key = -5
    print("OK" if func(a, key) == -1 else "Fail")

    print("Test case 2: ", end='')
    a = [1, 2, 5, 5, 7, 8, 10, 10]
    key = 6
    print("OK" if func(a, key) == 3 else "Fail")

    print("Test case 3: ", end='')
    a = [1, 2, 5, 5, 7, 8, 10, 10]
    key = 15
    print("OK" if func(a, key) == 7 else "Fail")

    print("Test case 4: ", end='')
    a = [1, ]
    key = 1
    print("OK" if func(a, key) == -1 else "Fail")


def test_right(func):
    print("Test case 1: ", end='')
    a = [1, 2, 5, 5, 7, 8, 10, 10]
    key = -5
    print("OK" if func(a, key) == 0 else "Fail")

    print("Test case 2: ", end='')
    a = [1, 2, 5, 5, 7, 8, 10, 10]
    key = 6
    print("OK" if func(a, key) == 4 else "Fail")

    print("Test case 3: ", end='')
    a = [1, 2, 5, 5, 7, 8, 10, 10]
    key = 15
    print("OK" if func(a, key) == 8 else "Fail")

    print("Test case 4: ", end='')
    a = [1, ]
    key = 1
    print("OK" if func(a, key) == 1 else "Fail")


if __name__ == '__main__':
    test_right(right_bound)
