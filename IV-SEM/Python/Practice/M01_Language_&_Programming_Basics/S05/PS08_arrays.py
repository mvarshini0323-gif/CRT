'''import numpy as np
arr=np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.max(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even numbers list is:",np.arange(2,11,2))
print("Odd numbers list is:",np.arange(1,10,2))

n=int(input("Enter the size"))
ele=list(map(int,input("enter ele").split()))
print("Array Ele are:",np.array(ele))
print("Sum:",sum(ele))
a = sort(ele)'''
#third max element in array
'''nums=list(map(int,input().split()))
if len(set(nums))>=3:
    print(sorted(set(nums))[-3])
else:
    print(max(nums))'''
#monotonic numbers
nums=list(map(int,input().split()))
inc=True
dec=True
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        dec=False
    if nums[i]<nums[i+1]:
        inc=False
if inc or dec:
    print("Monotonic array")
else:
    print("Not monotonic")


