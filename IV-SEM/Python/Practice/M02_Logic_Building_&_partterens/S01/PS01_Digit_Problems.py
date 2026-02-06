'''
1) write a python code to count the digits of number?
Ex:15678-->output:5
2)sum of the digits of a number?
Ex:12345-->output:15
'''
'''n=int(input())
count=0
while n>0:
    count+=1
    n=n//10
    print(count)'''
'''n=int(input())
sum=0
while n>0:
    sum+=n%10
    n=n//10
print(sum)'''
'''reverse the number'''
'''num=int(input())
r=0
while num>0:
    r=r*10+num%10
    num=num//10
print(r)'''
'''count the even and odd digits'''
'''n=int(input())
even=0
odd=0
while n>0:
    d = n%10
    if d%2==0:
        even+=1
    else:
        odd+=1
    n = n//10
print(even)
print(odd)'''
n=int(input())
largest =0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n=n//10
print(largest)

