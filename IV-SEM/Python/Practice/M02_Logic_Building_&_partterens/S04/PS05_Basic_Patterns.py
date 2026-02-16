'''input:4
output:* * * *
       * * * *
       * * * *
       * * * *'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print(" ")'''
#Simple triangle partten
''' n=4
*
* *
* * *
* * * *'''
# '''n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()'''
#inverse triangle partten
'''n=4
output:
* * * *
* * *
* *
*
'''
#inverse triangle partten
# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
'''* * * *
     * * *
       * *
         *'''
# n = int(input())

# for i in range(n):
#     print("" * i, end="")
#     print("* " * (n - i))
'''n=4
output:
1
2 3
4 5 6
7 8 9 10'''
'''n=int(input())
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()
'''
'''n=4
output:
A
A B C
A B C D
'''
#sol
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()'''
'''Alphabet sequence'''
'''n=4
output:
A
B C
D E F
G H I J'''
'''n=int(input())
k=65
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k+=1
    print()'''
''' n=4
output:
* * * *
*     *
*     *
* * * *
'''
