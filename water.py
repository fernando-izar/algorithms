def water(l: list, area=0) -> int:
    if len(l) < 2:
        return area

    new_area = min(l[0], l[-1]) * (len(l) - 1)
    if new_area > area:
        area = new_area

    if l[0] < l[-1]:
        return water(l[1:], area)

    elif l[0] > l[-1]:
        return water(l[0:-1], area)

    else:
        return water(l[1:-1], area)


my_list = [2, 3, 1, 4, 3, 2, 1]
my_list1 = [1, 2, 3, 10, 10, 3, 2, 1]
my_list3 = [5, 9, 2, 1, 4]

res = water(my_list)
res1 = water(my_list1)
res3 = water(my_list3)

print(res, res1, res3)
