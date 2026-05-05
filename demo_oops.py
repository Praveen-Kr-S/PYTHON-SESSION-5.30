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




#Single Level Inhertance
class ebook:
    def book(self):
        print("Ebook Name : Learn Python")

class author(ebook):
    def author_name(self):
        print("Author Name : Jai Prakash..")

# a = author()
# a.book()
# a.author_name()

#Multi-level inhertance

class power:
    def fun1(self):
        print("Need Electronical device")


class phone(power):
    def fun2(self):
        print("Connect with people")


class smartphone(phone):
    def fun3(self):
        print("Smartphone with internet")

# s = smartphone()
# s.fun1()
# s.fun2()
# s.fun3()


# Hierachical Inheritance

class upi:
    def upi_api_servie(self):
        print("UPI API servie")

class gpay(upi):
    def gpay_money(self):
        print("Gpay Money transfer")


class phonepy(upi):
    def phonepy_money(self):
        print("phonepy Money transfer")


gpay().gpay_money()
gpay().upi_api_servie()
phonepy().phonepy_money()
phonepy().upi_api_servie()





#polymorphism --> Many Faces
"""
1.method overloading
single class
multiple function with same function_name with diffrent arguments
"""
# java method or real method
# class cal:
#     def add(self,a,b):
#         print("Add 2 arguments : ",a+b)
#
#     def add(self,a,b,c):
#         print("Add 3 arguments : ",a+b+c)
#
#     def add(self,a,b,c,d):
#         print("Add 4 arguments : ",a+b+c+d)
#
#     def add(self,a,b,c,d,e):
#         print("Add 5 arguments : ",a+b+c+d+e)
#
# c = cal()
# c.add(1,2,3,4,5)
# c.add(1,2,3,4)

class cal:
    def add(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print("Add 4 arguments : ",a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print("Add 3 arguments : ",a+b+c)
        elif a!=None and b!=None:
            print("Add 2 arguments : ",a+b)
        else:
            print("1 argument value : ",a)

c = cal()
# c.add(1,2,3,4)
# c.add(1,2,3)
# c.add(1,2)
# c.add(1)



# method overraiding
#super()  --> class
class school:
    def mark(self):
        print("10th = 388")

class high_school(school):
    def mark(self):
        super().mark()
        print("12th = 471")

class college(high_school):
    def mark(self):
        super().mark()
        print("CGPA = 7.5")

# cg = college()
# cg.mark()

# Operator overloading

# a = 10
# b = "k"
# print(a.__add__(b))
# print(a.__sub__(b))
# print(a.__sub__(5))
# print(a.__mul__("hi"))



# abstraction in oops
# we need abc module -> ABC,abstractmethod
from abc import ABC,abstractmethod
class ebook(ABC): #abstract class
    @abstractmethod
    def book(self):
        print("Book Name : Learn Python")
        print("Author Name : Kasi prakash ")
        print("Sensitive Content...")

    @abstractmethod
    def book1(self):
        print("Book Name : Learn Java")
        print("Author Name : Kasi Surjith ")
        print("Sensitive Content...")

    def book2(self):
        print("Book Name : Learn Django")
        print("Author Name : Praveen ")

class vendor(ebook):
    def book(self):
        super().book()

    def book1(self):
        print("Book Name : Learn Java")
        print("Author Name : jai surjith ")

v = vendor()
# v.book()
# v.book1()
# v.book2()

# encapsulation in python

class ac:
    name = "Jai Prakash"
    _acNo = 87654321 #protected
    __pin = None #private

    def show_pin(self,p):
        self.__pin=p
        # print(self.__pin)

class gpay(ac):
    def fun1(self):
        print(self.name)
        print(self._acNo)
        # print(self.__pin)

# a = ac()
# print(a.name)
# print(a.__pin)
g = gpay()
g.fun1()
g.show_pin(8765)


