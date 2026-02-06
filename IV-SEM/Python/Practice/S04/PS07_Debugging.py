'''Types of errors :
                1)Syntax errors-->Missing of colon,missing 
                2)Runtime Error
                3)Logical Errors'''
'''try:
    a = int(input("enter a num:"))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by Zero.")
except ValueError:
    print("Invalid input")'''
'''
pdb Comands:
1)n-->to execute the output in a next line
2)p variable -->to get the value of a variable
3)I-->List nearby code
4)c --> Continue the execution
5)s-->to start a function
6)r-->return from the function
7)h-->help
8)q-->Ouit the execution'''
import pdb
def add(a,b):
    pdb.set_trace() #
    return a+b
a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
print(add(a,b))

