'''Display Arithemetic Progression values upto 10
a = int(input())
d = int(input())
for i in range(10):
    print(a +(i*d), end=" ")

 Fibonacci series upto 5 
a = int(input())
b = int(input())
for i in range(5):
    print(a, end=" ")
    a, b = b, a + b
Fibonnaci series using a list 
n = int(input())
arr = [0,1]
for i in range(2, n):
    
    arr.append( arr[i-1]+arr[i-2])
print(arr)

power of a number 
n =2
output : 2,4,8,16
n = int(input())
for i in range(1, 11):
    print(n**i, end=" ")
    '''

