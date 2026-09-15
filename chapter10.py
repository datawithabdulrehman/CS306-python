# a = 123 
# copy = a 
# rev = 0 

# while a > 0:
#     rev = rev * 10 + a%10 
#     a = a //10 

# if copy == rev:
#     print("palindrome number")
# else:
#     print("not a palindrome") 

# Functions are blocks of code that perform a specific task.
# we can not write any program again and again, we can write a function and call it whenever we want to use it.\
    # Two types of functions
    # 1. Built-in functions
    # 2. User-defined functions 
# def hello():
#         print("Hello World")  
#         print('Wellcome to Python Programming')
        
# hello()
# def addition(a,b): #parameters like a variable that accepts values
#     print(a + b)
    
# addition(20,20) # providing values to parameters is called arguments
# addition(50,50)

def palindrome_checker(a):
    copy = a 
    rev = 0 

    while a > 0:
        rev = rev * 10 + a%10 
        a = a //10 

    if copy == rev:
        print(f"{copy} is a palindrome number")
    else:
        print(f"{copy} is not a palindrome")

# palindrome_checker(121)
# palindrome_checker(456)
# palindrome_checker(324)


"""
parameters and arguments 
parameters are the values you accept while 
calling the function
arguments are the values you provide to parameters 
while calling the function
"""

#01_positional arguments 

def multiply(a,b,c,d):
    print(a * b * c * d)

#multiply(5,2,3,3)


#default arguments 

def addition(a,b,d,c = 12):
    print(a + b + c + d)

#addition(5,5,5)

#keyword arguments

def substraction(a,b,c): 
    print("Substraction of two numbers is : ")
    print(b - a)

substraction(20,c = 40,b = 34)