def check_if_list_is_sorted(A: list, ascending=True):
    """Проверка отсортированности за O(len(A))"""
    flag = True

    for i in range(0, len(A) - 1):
            if (2 * int(ascending) - 1) * A[i] > A[i + 1] * (2 * int(ascending) - 1):
                flag = False
                break
    return flag


a = [-1, -2, -3, -4, -5]
print(check_if_list_is_sorted(a))
print(check_if_list_is_sorted(a, ascending=False))
