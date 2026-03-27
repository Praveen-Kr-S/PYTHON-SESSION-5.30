#Exception Handling
'''
a = 10
print(A)
'''

"""
try:
    #block of code
except Exception as e:
    #show the Exception
"""
#1.Name Error
'''
try:
    a = 10
    print(a)#run time error
except Exception as e:
    print(e)
'''
#2 zero divistion error
#print(5/0)
'''
try:
    a = 10
    b = 0
    print(a/b)
except Exception as e:
    print(e)
'''
#3.List index out range error
'''
try:
    l = [30,40,50,60,70]
    n = int(input("Enter The Number :"))
    print(l[n])
except Exception as e:
    print(e)
'''

#4.String index out range error
'''
try:
    l = "Surjith"
    n = int(input("Enter The Number :"))
    print(l[n])
except Exception as e:
    print(e)
finally:
    print("Code Excecuted!!!!")
'''

#assert
a = 101
assert a==10
print(a)


    





















