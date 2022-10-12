# Write a Python program to convert kilometers to miles
try :
    a=int(input("Enter kilometer : "))
    b=a*0.6213
    print(f"miles : {b}")
except Exception as a:
    print("this code will run when error occurs in try",a)

# Write a Python program to convert Celsius to Fahrenheit
c=int(input("Enter celcius : "))
f=(c*1.8)+32
print(f"farhenite : {f}")

# Write a Python program to display calendar
import calendar
print("Enter year : ")
yy=input()
print("\nEnter Month Number (1-12): ")
mm=input()

y=int(yy)
m=int(mm)
print("\n",calendar.month(y,m))

# Write a Python program to solve quadratic equation
import cmath 

a=1
b=5
c=6

d=(b**2)-(4*a*c)

sol1=(-b-cmath.sqrt(d)/(2*a))
sol2=(-b+cmath.sqrt(d)/(2*a))

print("the solution are {0} and {1}".format(sol1,sol2))

# Write a Python program to swap two variables without temp variable
x=9
y=10
print(f"before swaping : x={x}, y={y}")
x=x+y
y=x-y
x=x-y
print(f"after swaping : x={x}, y={y}")