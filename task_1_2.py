# Write a function that check whether a string is a palindrome or not.
# Usage of any reversing functions is prohibited.


def check_palindrome(somestring):
    listed_string = []
    for i in somestring:
        if i.isalpha():
            i = i.lower()
            listed_string.append(i)
        elif i.isdigit():
            listed_string.append(i)
    len_listed_string = len(listed_string)
    for ind in range(len_listed_string//2):
        if listed_string[ind] != listed_string[-1-ind]:
            return False
    return True


print(check_palindrome("abccba"))
print(check_palindrome("Mr. Owl ate my metal worm"))
print(check_palindrome("Step on no pets"))
print(check_palindrome("Live on time, emit no evil"))
print(check_palindrome("Rats live on no evil star"))
print(check_palindrome("123454321"))
print(check_palindrome("absddfsba"))
