def left(i: int) -> int:
    return 2 * i


def right(i: int) -> int:
    return 2 * i + 1


def change_nodes(A: list, i: int, bigger: int):
    A[i - 1], A[bigger - 1] = A[bigger - 1], A[i - 1]


def max_heapfy(A: list, i: int) -> list:
    l = left(i)
    r = right(i)
    size_heap = len(A)

    if l <= size_heap and A[l - 1] > A[i - 1]:
        bigger = l
    else:
        bigger = i

    if r <= size_heap and A[r - 1] > A[bigger - 1]:
        bigger = r

    if bigger != i:
        change_nodes(A, i, bigger)
        max_heapfy(A, bigger)


A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

max_heapfy(A, 2)

print(A)
