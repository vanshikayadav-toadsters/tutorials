#function greet that prints hello world
# def greet():
#     print("Hello World")
# greet()

#function say_name(name) that prints the given name
# def say_name(name):
#     print(f"My name is {name}")

# say_name("Vanshika")

#Prints the sum of two numbers
# def add(a,b):
#     return a+b
# print(add(5,7))

#square os a number
# def square(n):
#     return n*n 

# print(square(7))

#print even or odd
# def is_even(n):
#     if n%2==0:
#         print("Even number")
#     else:
#         print("Odd number")

# is_even(5)

#Multiply a,b=2
# def multiply(a,b):
#     return a*b

# print(multiply(5,2))


#return full name in a string
# def full_name(first,last):
#     return(f"My name is {first} {last}")

# print(full_name(first="Vanshika", last="Yadav"))


#max of two
# def max_of_two(a,b):
#     if a>b:
#         print("a is maximum")
#     else:
#         print("b is maximum")
# max_of_two(3,4)

#Calculate sum and difference
# def calculate(a,b):
#     return a+b , a-b 

# print(calculate(5,9))

#check age
# def check_age(age):
#     if age <= 18:
#         return "minor"
#     else:
#         return "adult"

# print(check_age(34))

#Count vowels in a string
# s=input("Enter the string: ")
# def count_vowels(s):
#     count=0
#     for ch in s:
#         if ch in ['A','E','I','O','U','a','e','i','o','u']:
#             count +=1
#     return count   

# print(count_vowels(s))


#factorial of a number
# n=int(input("Enter the number: "))
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(factorial(n))

#Calculator
# a=int(input("Enter the number: "))
# b=int(input("Enter the number: "))

# print("--Start the calculation")
# print("1: Addition")
# print("2: Subtraction")
# print("3: Multiplication")
# print("4: Division")


# choice=int(input("Enter the choice: "))


# def Calculator(a,b):
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b
#     def mul(a,b):
#         return a*b
#     def div(a,b):
#         if b==0:
#             return "Cannot divide by zero"
#         return a/b
    
#     if choice==1:
#         print("Answer is :", a+b)
#     elif choice==2:
#         print("Answer is :", a-b)
#     elif choice==3:
#         print("Answer is : ",a*b)
#     elif choice==4:
#         if b==0:
#             print("Invalid division")
#         else:
#             print("Answer is: ", a/b)
#     else:
#         print("Invalid choice")

# print(Calculator(a,b)) 


#function that aceepts any number of output ans returns sum of numbers
# def add_numbers(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum

# print(add_numbers(1,2,3,4,5))



    



# Create a function calculator(a, b, operation) where:
# operation can be "add", "sub", "mul", "div"

# a=int(input("Enter the number: "))
# b=int(input("ENter the number: "))

# operations=input("Enter the opeartion: ")
# def calculator(a,b,operation):

#     if operation == "add":
#         print(a+b)
#     if operation =="sub":
#         print(a-b)
#     if operation == "mul":
#         print(a*b)
#     if operation == "div":
#         if b==0:
#             print("Cannot perform division")
#         else:
#             print(a/b)
    
    
# calculator(a,b,operations)
    


# Write a function outer() that defines another function inner() inside it.
# Call inner() from inside outer()

# def outer():
#     def inner():

#         inner()
# outer()



#Write a function power(base, exponent) that returns base raised to exponent without using **
# base=int(input("Enter the base value:"))
# exponent=int(input("Enter the exponent power:  "))
# def power(base, exponent):
#     ans=1
#     for i in range(exponent):
#         ans *= base
#     return ans
    
    
# print(power(base,exponent))

#Palindrome code with time complexity O(n/2)
s=input("Enter the string:  ")
print(type(s),s)
def palindrome(s):
    n=len(s)
    i=0
    j=n-1 
    while i <= j :
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -=1
    return True

is_palindrome = palindrome(s)
print(is_palindrome)



    


