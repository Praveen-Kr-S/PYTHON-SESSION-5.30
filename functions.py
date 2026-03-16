#functions
"""
1.function decalration
def function_name(parameter/arguments):
    #block of code

2.function call
function_name()
"""
'''
def fire():
    print("Fire Mode is ON....")

fire()
print("Hi")
fire()
print("Hello")
fire()
'''
#1.without argument function
"""
def jump():
    print("Jump mode activate")
jump()
"""
#with argument function
#1.Positional argument function
'''
def add(x,y,z):
    a = x
    b = y
    print(a)
    print(b)
    print("add :",a+b)

add(10,5,6)
add(45,15,8)
'''

#default arg function
'''
def spec(name="Samsung S25",color="Black",price=120000):
    print("Mobile Name :",name)
    print("Mobile Color :",color)
    print("Mobile Price :",price)

spec("Apple",'white',145000)
spec("Oppo",'orange')
'''
#DEMO TASK
#palindrome in string using function:
def palindrome(data):
    r=""
    for i in data: #python
        r = i+r
    """
    i = p
    r = "p"+"" -> "p"
    i=y
    r = "y"+"p" =>"yp"
    i=t
    r = "t"+"yp" =>"typ"
    i=h
    r = "h"+"typ" =>"htyp"
    i=o
    r = "o"+"htyp" =>"ohtyp"
    i=n
    r = "n"+"ohtyp" =>"nohtyp"
    """
    if r == data:
        print(f"{r} is plaindrome")
    else:
        print(f"{r} is not plaindrome")

d = input("Enter cheking value :") #Praveen
palindrome(d)








