# Implement a function which receives a string and
# replaces all " symbols with ' and vise versa.


def replace_symbols(somestr):
    smb_1 = "'"
    smb_2 = '"'
    mutated_list = []
    for i in somestr:
        if i == smb_1:
            i = smb_2
        elif i == smb_2:
            i = smb_1
        mutated_list.append(i)
    mutated_string = ''.join(mutated_list)
    return mutated_string


print(replace_symbols("dfkjha'f\jh"))
print(replace_symbols("shst'sth\"ahhhh"))
print(replace_symbols('df"kjha"jh'))
print(replace_symbols('shststh"ahhhh'))