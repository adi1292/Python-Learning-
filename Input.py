
name = input("Enter your name: ")
print("My name is " + name)
city=input("Enter your city: ")
print("Your city is " + city)

name=input("Enter your name: ")
age=input("Enter your age: ")
print("Name:",name)
print("Age:",age)

#Important Concept
"""Input input() always returns a string str() even if the user types the number"""

age =input("Enter your age: ")
print(type(age));#Even though you entered 22, Python treats it as text, not a number

#Converting Input to an Integer
#If you want to perform calculations, convert the input using int().
age = int(input("Enter your age: "));
print(type(age));#Now Python treats it as a number, not text

#Example:Add two numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
print("Sum=",sum)

#Example:Decimal Numbers 
#Use float for decimal numbers. 
num1=float(input("Enter first height: "))
print("Height=",num1)

#Example :Take the user name as input and print
name =input("Enter your name: ")
print("Hello",name);

#Example:Take the user age as input and print
age = int(input("Enter your age: "))
print("Your are", age, "years old")

#Example:Take two numbers from the user and print their sum.
num1=int(input("Enter first number: "));
num2=int(input("Enter second number: "));
sum=num1+num2;
print("Sum=",sum);

#Example:Take the user's city and favorite color, then print:
city=input("Enter your city: ");
color=input("Enter your favorite color: ");
print("Aditya lives in",city,"and his favourite color is",color);




