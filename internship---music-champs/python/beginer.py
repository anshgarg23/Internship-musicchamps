import time
current_hour = time.localtime().tm_hour
if current_hour < 12:
    print("good morning")
elif 12 < current_hour < 17:
    print("good afternoon")
elif 17 < current_hour < 22:
     print("good evening")
else:
     print("good night") 
print("program complete")

#program to calculate the area and perimeter of the circle
radius = int(input("enter the radius of the circle: "))
perimeter = 2 * 3.14 * radius
print(perimeter)
r = int(input("enter the radius of the circle: "))
area = 3.14 * r * r
print(area)


#calculator program 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operator = input("choose operater: +, -, *, /: ")
if operator == '+':
     result = num1 + num2
     print(result)
elif operator == '-':
     result = num1 - num2
     print(result)
elif operator == '*':
     result = num1 * num2
     print(result)
elif operator == '/':
     result = num1/num2
     print(result)
else:
     print("invalid input")






#swapping variables with user input
a = input("enter the value for a: ")
b = input("enter the value for b: ")
print("a =", b)
print("b =", a)

#taking user input and printing it in reverse
x = input("enter user input: ")
print(x[::-1])