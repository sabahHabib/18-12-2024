#Write a Python program to print the reverse number pattern using a for loop.

#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1
row= 5
k=5
for i in range(0,row+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print("")
# Display numbers from -10 to -1 using for loop
for i in range(-10, 0):
    print(i)
# Display a message “Done” after the successful execution of the for loop
for i in range(5):
    print(i)
print("Done")


# Print all prime numbers within a range
start = int(input("Enter number to get prime number from:"))
end = int(input("Enter number to get prime number till:"))

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Display Fibonacci series up to 10 terms
num1, num2 = 0, 1
print("Fibonacci series is:")
for n in range(10):
    print(num1)
    result=num1+num2
    num1=num2
    num2=result
# Find the factorial of a given number
num=int(input("enter number to calculate factorial:"))
if num <0:
    print("factorial of negative number does not exist")
else:
    factorial = 1
    for n in range(2,num+1):
        factorial= factorial *n
    print("factorial of a number is:",factorial)

# Reverse a integer number
number=int(input("Enter number to get reverse:"))
reverse=0
while number> 0:
    reminder=number % 10
    reverse =(reverse * 10) + reminder
    number= number // 10
print("reverse of a number is:",reverse)


# Print elements from a given list present at odd index positions
list1 =['a', 'b', 'c', 'd']
for i in list1[1::2]:
    print(i, end=" ")


# Calculate the cube of all numbers from 1 to a given number
a=2
for i in range(1, a+1):
    cube = i*i*i
print("cube of a number is:", cube)


#  Find the sum of the series up to n terms
n=5
start=2
sum_of_series=0
for i in range(0,n):
    sum_of_series+=start
    start=start*10+2
print("sum of series is:",sum_of_series)

#Write a program to count how many vowels (a, e, i, o, u) are present in a given string.
a=input("enter string to find vowels").lower()
count=0
vowels="aeiou"
for i in a:
    if i in vowels:
        count+=1
print(count)

# Write a program to check if a number is even or odd using the modulus operator.
num = int(input("Enter number to check even or odd:"))
if (num % 2) == 0:
    print(num, "is a even number")
else:
    print(num, "is a odd number")

# Write a program to compare the lengths of two strings and determine which is longer.

str1= "abcdfgh"
str2="abhkk"
if len(str1) > len(str2):
    print(str1, "is greater")
else:
    print(str2, "is greater")
#Create a program that asks the user for their age and checks if they are eligible to vote (age ≥ 18).
age=int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
#Create a loop that doubles a value starting at 1 until it reaches 1000, updating the value using *=.
value =1
while value <= 1000:
    print(f"current value is :{value}")
    value*=2
print("Loop ended value exceed 1000")
#Create a calculator program that takes two numbers and an operator (+, -, *, /, %, **, //) as input, performs the operation, and prints the result.
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b if b !=0 else "Error !division by zero"
def modulus(a,b):
    return a%b
def power(a,b):
    return a**b
def floor_division(a,b):
    return a//b
num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))
operator=(input("Enter operator (+,_,*,/,**,//,%):"))
if operator=="+":
    result=add(num1,num2)
elif operator=="-":
    result=subtract(num1,num2)
elif operator=='*':
    result=multiply(num1,num2)
elif operator=='/':
    result=divide(num1,num2)
elif operator=='%':
    result=modulus(num1,num2)
elif operator=='//':
    result=floor_division(num1,num2)
elif operator=='**':
    result=power(num1,num2)
print(f"Result is: {result}")
#Create a program to check if a string is a palindrome (reads the same forward and backward).

def is_palindrome(a):
    new_string=a.replace(" ",'').lower()
    return new_string == new_string[::-1]
a=input("Enter a string to verify palindrome:")
if is_palindrome(a):
    print("The string is a palindrome")
else:
    print("Not a palindrome")
#Write a program to count how many elements in a list are divisible by 2 and how many are divisible by 3.
count2 = 0
count3 = 0
numbers=[2,33,78,49,34,98]
for i in numbers:
    if (i % 2) == 0:
        count2 += 1
    elif (i % 3) == 0:
        count3 += 1
print(f"Total number of elements divisible by 2:{count2}")
print(f"Total number of elements divisible by 3:{count3}")