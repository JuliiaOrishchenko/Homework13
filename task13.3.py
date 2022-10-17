def choose_func(list1, func1, func2):
    if all([num > 0 for num in list1]):
        return func1(list1)
    else:
        return func2(list1)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


print(choose_func([1, 2, 3, 4, 5], square_nums, remove_negatives))
print(choose_func([1, -2, 3, -4, 5], square_nums, remove_negatives))