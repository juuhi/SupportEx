#Ex 8
#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(myList):
    return max(len(i) for i in myList)

print(find_longest_word(["pra","prakash","prakash patel"]))