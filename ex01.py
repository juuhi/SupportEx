# Ex 1
#1. Define a function max() that takes two numbers as arguments and returns the largest of
#them. Use the if-then- else construct available in Python.



def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

n1 = input('Enter First number \n')

n2 = input('Enter Second number \n')

print('\n' + str(max(n1, n2))+ ' is larger')