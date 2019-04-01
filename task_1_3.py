# Implement a function which works the same as str.split method


def split_double_ganger(somestring, separator=" ", max=-1):
    if type(somestring) == str:
        list_somestring = []
        counter = 0
        try:
            if max < 0:
                while counter > max:
                    sep_position = somestring.index(separator)
                    temp_str = somestring[0:sep_position]
                    somestring = somestring[sep_position + len(separator):]
                    list_somestring.append(temp_str)
                    counter += 1
            elif max > 0:
                while counter < max:
                    sep_position = somestring.index(separator)
                    temp_str = somestring[0:sep_position]
                    somestring = somestring[sep_position + len(separator):]
                    list_somestring.append(temp_str)
                    counter += 1
                if somestring:
                    list_somestring.append(somestring)
                return list_somestring
        except:
            if somestring:
                list_somestring.append(somestring)
            return list_somestring
    else:
        return "AttributeError: " + str(type(somestring)) + \
               " object has no attribute 'split_double_ganger'"


txt_1 = "sun is shining"
txt_2 = "floccinaucinihilipilification"
txt_3 = "hello, my name is Peter, I am 26 years old"
txt_4 = """The limit of the song is this
prelude to a journey to
the outer islands, the generative
sentence, waltz project, forms,
qualities, suns, moons, rings,
an inside-outside then
an outside-inside shaped
with her colored clays."""


print(split_double_ganger(txt_1))
print(txt_1.split())
print(split_double_ganger(txt_2))
print(txt_2.split())
print(split_double_ganger(txt_3,","))
print(txt_3.split(","))
print(split_double_ganger(txt_4, " ", 2))
print(txt_4.split(" ",2))

# Here exception must arise
# print(split_double_ganger(['something']))