# Implement a function foo(List[int]) -> List[int] which, given a list
# of integers, return a new list such that each element at index i of
# the new list is the product of all numbers in the original array
# except array the one at i.


def foo(some_list):
    new_list = []
    for i in range(len(some_list)):
        temp_list = []
        for k in range(len(some_list)):
            if k != i:
                temp_list.append(some_list[k])
        result = 1
        for x in temp_list:
            result = result * x
        new_list.append(result)
    return new_list



print(foo([1,2,3,4,5]))  # output: [120, 60, 40, 30, 24]
print(foo([3,2,1]))  # output: [2,3,6]





