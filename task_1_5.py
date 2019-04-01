# Implement a function get_digits(num:int) -> Tuple[int]
# which returns a tuple of a given integer's digits.


def get_digits(num):
    num = str(num)
    nums_list = []
    for i in num:
        nums_list.append(int(i))
    return tuple(nums_list)


print(get_digits(87178291199))  # output: (8,7,1,7,8,2,9,1,1,9,9)

