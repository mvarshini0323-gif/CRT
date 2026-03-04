'''li=[1,2,3,4,5]
#output:[1,4,9,16,25]
for x in li:
        res=[x**2 for x in li]
        print(res)'''
#print only evens
'''li=[1,2,3,4,5]
#output:[2,4]
res=[]
for x in li:
    if x%2==0:
        res.append(x)
print(res)'''
'''li=['a','b','c']
#output:' a b c '
print(*li)
#or
print("@".join(li))
'''
#Intermediate Patterns
'''1. Pyramid
n=4
Output:
       *
      * *
     * * *
    * * * *
'''
# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

''' n=4
output:
* * * *
 * * *
  * *
   *
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
'''
#dimond
'''
   * 
  * *
 * * *
* * * *
 * * *
  * *
   *
'''
'''n=int(input())

for i in range(1,n+1):#(1,n)
     print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):#(n,0,-1)
    print(" "*(n-i)+"* "*i)'''
#pyramid in numbers
'''
   1
  1 2
 1 2 3
1 2 3 4'''
'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i) ,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''
'''
   1
  2 2
 3 3 3
4 4 4 4 '''
'''
n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i) ,end=" ")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(k) for k in range(1,i+1)]))
    '''

