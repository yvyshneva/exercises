############## Exponentiation #################
"""
Exponentiation is the raising of one number to the power of another.
This operation is performed using two asterisks **.

Let's use exponentiation to solve a known problem.
You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).

Task:
Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.
"""

choice_million = 1000000
choice_penny = 0.01 * (2**30)

if choice_penny > choice_million:
    print(choice_penny)
elif choice_million > choice_penny:
    print(choice_million)
else:
    print('Results are equal')

    
############## Simple Calculator #################
"""
Write a program to take two integers as input and output their sum.

Sample Input:
2
8

Sample Output:
10
"""

int_1 = int(input())
int_2 = int(input())

print(int_1 + int_2)
