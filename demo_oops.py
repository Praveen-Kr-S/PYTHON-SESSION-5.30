#oops
"""
Syntaxn of class
class class_name:
    #set of attribute and functions

Syntax of Object
variable = class_name()
"""
class mobile:
    #variables
    brand=None
    model=None
    color=None
    price=None
    #Functions

    def gaming(self):
        print(f" Play Heavy{self.model} and Funny games")

# m1 = mobile()
# # print(m1.price)
# m1.brand="Samsung"
# m1.model="Samsung S25"
# m1.color="blue"
# m1.price=80000
# print(m1.brand)
# print(m1.model)
# print(m1.color)
# print(m1.price)
# m1.gaming()
# print("+++++++++++++++++++")
# m2=mobile();
# m2.brand="Apple"
# m2.model="Apple 16 pro"
# m2.color="red"
# m2.price=120000
# print(m2.brand)
# print(m2.model)
# print(m2.color)
# print(m2.price)
# print(m2.price)
# m2.gaming()


class car:
    brand=None
    model=None
    color=None
    price=None
    def __init__(self,b,m,c,p):
        print("Car Spec's")
        self.brand=b
        self.model=m
        self.color=c
        self.price=p

        print("Car Brand :",self.brand)
        print("Car Model :",self.model)
        print("Car Color :",self.color)
        print("Car Price :",self.price)

        print("*".center(20,"*"))


c1 = car("Tata","Nexon","Blue",1500000)
c2 = car("Hyndai","Creta","Black",1700000)