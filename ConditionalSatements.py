#if Statement
age=20;
if age >= 18:
    print("You are eligible to vote.");

marks=80;
if marks >= 35:
    print("You have passed the exam.");

#if-else Statement
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

    number = 10
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

    #if-elif-else Statement
marks1=75

if marks1 >= 90 :
        print("Grade A")
elif marks1 >= 80:
        print("Grade B")
elif marks1  >= 70:
        print("Grade C")
elif marks1 >= 60:
        print("Grade D")        
else:
        print("Grade F")

#Example Using User Input
age=int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
#Nested if Statement
age=22;
has_voter_id=True;
if age >= 18:
  if has_voter_id:
        print("You are eligible to vote.")


  #Write a program to check if a number is positive or negative.
  num=int(input("Enter a number: "));
if  num > 0:
  print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
        print("The number is zero.")    

#Write a program to check if a number is divisible by 5.
num=int(input("Enter a number: "));
if num % 5 == 0:
 print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

#Write a program to compare two numbers and print the larger one
num1=int(input("Enter first number: "));
num2=int(input("Enter second number: "));
if num1 > num2:
    print(num1,"is larger than",num2);
elif num2 > num1:
    print(num2,"is larger than",num1);
else:
    print("Both numbers are equal.");   