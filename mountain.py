def test_desc(l: list) -> bool:
    return l == sorted(l, reverse=True)


def mountain(l: list) -> bool:
    if len(l) < 3:
        return False

    for i in range(0, len(l) - 2):
        if test_desc([l[i], l[i + 1], l[i + 2]]):
            return True

    return False


my_list = [0, 5, 4, 3, 9, 0]

print(mountain(my_list))
