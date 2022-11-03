# Write a Python Program to Find the Factorial of a Number?



def fact(n):
    n=int(input("\n1. Enter a number : "))
    f=1
    for i in range(2,n+1):
        f=f*i
    return f
result=fact(5)
print(f" factorial is : {result}")

# Write a Python Program to Display the multiplication Table
n=int(input("\n2. Enter the number :"))
for i in range(1,11):
    f=i*n
    print(f"{i} X {n} : {f}")

# Write a Python Program to Print the Fibonacci sequence?
s=int(input("\n3. Enter a number : "))
a=0
b=1
if s<=0:
    print("this is the fibonacci series.")
else:
    print(a , b,end=" ")
    for i in range(2,s):
        next=a+b
        print(next,end=" ")
        a=b
        b=next

# Write a Python Program to Check Armstrong Number
num=int(input("\n4. Enter a number : "))

sum=0

temp=num

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num," is amstrong number .")
else:
    print(num," this is not an amstrong number .")

# Write a Python Program to Find Armstrong Number in an Interval?
lower=100
upper=1000

for num in range(lower,upper+1):

    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10

    if num==sum:
        print(num)

# Write a Python Program to Find the Sum of Natural Numbers
num2=int(input("6. Enter the number : "))
sum=0
for i in range(1,num2+1):
    sum=sum+i
print(sum)

