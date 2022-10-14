# Write a Python Program to Check if a Number is Positive, Negative or Zero
from re import T
from sys import flags


try:
    number=int(input("Enter the number"))
    if number>0:
        print(f"{number} the number is positive")
    elif number==0:
        print(f"{number} the number is zero ")
    elif number <0:
        print(f"{number} the number is negative")
except Exception as e:
    print("Enter valid credentials",e)

# # Write a Python Program to Check if a Number is Odd or Even?

try:
    n=int(input("Enter the number : "))
    if n%2==0:
        print(f"{n } the number is even")
    elif n%2!=0:
        print(f"{n } the number is odd")
except Exception as T:
    print("Enter valid number.",T)

# Write a Python Program to Check Leap Year?
l=int(input("Enter a year : "))
if l%4==0 and l%100!=0:
    print(f"\n {l } this is a leap year")
elif l%400==0 and l%100==0:
    print(f"\n {l} this is a leap year")
else:
    print("\nthis is not a leap year")

#Write a Python Program to Check Prime Number
num=9
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print("\nThe number is not prime")
else:
    print("\nthe number is prime")

# Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower=1
upper=10

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(f"prime numbers are : {num}")
 