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


############## FizzBuzz #################
"""
FizzBuzz is a well known programming assignment, asked during interviews.

The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn".

You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range.
"""

n = int(input())

for x in range(1, n, 2):
    if x % 3 == 0:
        if x % 5 == 0:
            print("SoloLearn")
        else:
            print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)


############## Celsius to Fahrenheit #################
"""
You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

Sample Input
36

Sample Output
96.8
"""

celsius = int(input())

def conv(c):
    return 9/5 * c + 32
    

fahrenheit = conv(celsius)
print(fahrenheit)

