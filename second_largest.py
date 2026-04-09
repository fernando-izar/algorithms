# return the second largest unique number from list
from collections import Counter


def second_largest(nums: list[int]) -> int:
    count = Counter(nums)
    tmp_list = [item[0] for item in count.items() if item[1] == 1]
    if len(tmp_list) >= 2:
        return sorted(tmp_list)[-2]
    else:
        raise ValueError("Not enough unique elements")


my_list = []
second_largest_value = second_largest(my_list)
print(second_largest_value)
