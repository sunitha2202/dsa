def greet():
    print("hello world")
greet()

#with parameter
def greet(name):
    print(f"hello,{name}")
greet("sunitha")

#function with miultiple parameter
def add(a,b):
    print(a+b)
add(3,5)
#with return statement
def add(a,b):
    return a+b
result=add(3,8)
print(result)

#default value parameter
def name(value="raj"):
    print(f"helle,{value}")
name("sam")
name()

#positional function
def greet(name,age):
    print(f"{name},{age}")
greet("john",54)

def outer_function():
    def inner_function():
        print("I am inside the outer function.")
    inner_function()

outer_function()