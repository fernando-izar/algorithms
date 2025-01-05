import math


# division and conquer
# p <= q < r
# merge two lists in ascending order
def merge(A: list, p: int, q: int, r: int) -> list:
    n1 = q - p + 1
    n2 = r - q
    L1 = [0] * n1
    L2 = [0] * n2
    for i in range(0, n1):
        L1[i] = A[p + i]
    for j in range(0, n2):
        L2[j] = A[q + 1 + j]
    L1.append(math.inf)
    L2.append(math.inf)

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L1[i] <= L2[j]:
            A[k] = L1[i]
            i += 1
        else:
            A[k] = L2[j]
            j += 1


def merge_sort(A: list, p: int, r: int):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def div_conq(A: list):
    merge_sort(A, 0, len(A) - 1)


# my_list = [2, 4, 5, 7, 1, 2, 3, 6]
my_list = [4, 2, 1, 3]

div_conq(my_list)
print(my_list)
