# Implement a function get_longest_word(s:str) -> str which returns
# the longest word in the giving string.
# The word can contain any symbols except whitespaces(,\n,\t and so on).
# If there are multiple longest words in the string with the same length
# return the word that occurs first.


def get_longest_word(somestring):
    somestring = somestring.split()
    counter = 0
    longest_word = ''
    for word in somestring:
        if len(word) > counter:
            counter = len(word)
            longest_word = word
    return longest_word

print(get_longest_word('Python is simple and effective!')) # output: 'effective!'
print(get_longest_word('Any pythonista like namespaces a lot.')) # output: 'pythonista'
