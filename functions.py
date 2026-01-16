def add_numbers(*args):
    total =0

    for num in args:
        total += num 
    return total

print (add_numbers(1,2,3,4))
print (add_numbers(10,15,20,30))



def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} :{value} ")
print(print_info(name = "Alice" , age = 17 , city = "meerut"))