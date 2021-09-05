'''write a program to calculate and print the factorial of a number using a for loop.
eg. factorial of 4 is 4*3*2*1=24
'''
#calculate factorial using math module
'''import math
num = int(input("Enter no: "))
factorial = print("Factorial of num is",math.factorial(num))'''

#calculate factorial using for loop
"""
num = int(input("Enter no: "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print("Factorial of ", num, "is", fact)
"""

#calculate factorial using recursion
num = int(input("Enter no: "))
def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)
print("Factorial of ", num, "is", fact(num))
