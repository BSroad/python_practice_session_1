# Implement a function
# split_by_index(s:str, indexes: List[int]) -> List[str]
# which splits the s string by indexes specified in indexes.
# Wrong indexes must be ignored.


def split_by_index(somestring,indexes_list):
    listed_string = []
    new_ind_list = []
    prev_ind = 0

    for ind in indexes_list:
        if len(somestring) > ind and ind > 0:
            new_ind_list.append(ind)
    if new_ind_list:
        for ind in new_ind_list:
            temp_str = somestring[prev_ind:ind]
            listed_string.append(temp_str)
            prev_ind = ind
        if somestring[prev_ind:]:
            listed_string.append(somestring[prev_ind:])
        return listed_string
    listed_string.append(somestring)
    return listed_string


print(split_by_index("pythoniscool,isn'tit?",[6,8,12,13,18]))  # output: ["python", "is"," cool", ",", "isn't", "it?"]
print(split_by_index("no luck",[42]))  # output: ["no luck"]
print(split_by_index("no luck",[-12]))  # output: ["no luck"]