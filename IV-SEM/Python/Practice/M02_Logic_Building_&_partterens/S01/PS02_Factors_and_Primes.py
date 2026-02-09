#write code to output the no of factors
'''n=int(input())
factors=0
for i in range(1,n+1):
    if(n%i)==0:
        factors+=1
    print("the factors are:",i)

print("No of factors:",factors)'''
#reverse integer
'''n = int(input())

if n<0:
    sign=-1
else:
    sign=1

n = abs(n)

rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed integer:", sign * rev)'''
#or
'''n = int(input())

if n>=0:
    print(int(str(n)[::-1]))
    
else:
    n = abs(n)
    print(-1*int(str(n)[::-1]))'''
#multiply string
#Plus One
#pallindrome
#to check num is prime or no
'''
n = int(input())

if n <= 1:
    print("Not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")'''
