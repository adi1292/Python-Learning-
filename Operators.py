#Operators in the Python
##Arithmetic Operators
##Logical Operators
##Comparison Operators

#1. Arithmetic Operators
#Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
a= 10;
b=5;

print("Addition:",a+b);
print("Subtraction:",a-b);
print("Multiplication:",a*b);
print("Division:",a/b);
print("Modulus:",a%b);
print("Exponent:",a**b);
print("Floor Division:",a//b);

#2. Comparison Operators
#Comparison operators are used to compare two values. They return either True or False according to the

x= 10;
y= 5;

print("Equal:",x==y);
print("Not Equal:",x!=y);
print("Greater than:",x>y);
print("Less than:",x<y);
print("Greater than or equal to:",x>=y);
print("Less than or equal to:",x<=y);

#3. Logical Operators
#Logical operators are used to combine conditional statements.
#AND
age=20;
print(age>18 and age<30);

#OR
age=15;
print(age<18 or age>30);

#NOT
is_adult= True;
print(not is_adult);


#Mini Project: Calculator
num1=int(input("Enter first number: "));
num2=int(input("Enter second number: "));
print("Select operation:");
print("Addition",num1+num2);
print("Subtraction",num1-num2);
print("Multiplication",num1*num2);
print("Division",num1/num2);
print("Modulus",num1%num2);