#Ex 3
# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def check_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char not in vowels:
        return False
    return True


print check_vowel(1)
print check_vowel('a')
print check_vowel('b')