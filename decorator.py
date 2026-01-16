# def decorator(func):
#     def wrapper():
#         print("Something before")
#         func()
#         print("Something after")
#     return wrapper

# @decorator

# def say_hello():
#     print("Hello!")

# say_hello()    

# def decorator(func):
#     def wrapper(*args , **kwargs):
#         print("Before")
#         result = func(*args , **kwargs)
#         print("After")
#         return func
#     return wrapper

# @decorator
 
# def greet(name):
#     print(f"Hello  {name}!")

# greet("Joy")


#Function based decorator
# def decorator1(func):
#     def wrapper():
#         print("Decorator 1")
#         func()
#     return wrapper

# def decorator2(func):
#     def wrapper():
#         print("Decorator 2")
#         func()
#     return wrapper

# @decorator1
# @decorator2

# def say_hi():
#     print("Hi")
# say_hi()



#Class based decorators
class Decorator:
    def __init__(self, func):
        self.func = func    # Store the functions

    def __call__(self , *args , **kwargs)   :
        print("Before")
        result = self.func(*args , **kwargs)
        print("After")
        return result

@Decorator

def greet(name):
    print(f"Hello  {name}")
greet("Bhuvan")
