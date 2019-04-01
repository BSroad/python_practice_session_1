# Implement a function get_pairs(lst: List) -> List[Tuple] which
# returns a list of tuples containing pairs of element.
# Pairs should be formed as in the example.
# If there is only one element in the list return None instead.


def get_pairs(some_list):
    list_of_tuples = []
    if some_list:
        if len(some_list) > 1:
            for i in range(len(some_list)-1):
                pair = some_list[i], some_list[i+1]
                list_of_tuples.append(pair)
            return list_of_tuples
    return None


print(get_pairs([1,2,3,8,9]))  # output: [(1,2),(2,3),(3,8),(8,9)]
print(get_pairs(['need', 'to', 'sleep', 'more']))  # output: [('need','to'),('to','sleep'),('sleep','more')]
print(get_pairs([1]))  #output: None