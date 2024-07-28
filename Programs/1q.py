A=[1,2,3,4,5]
sum=0
#a
for i in range(0,len(A)):
    sum+=A[i]
print("the sum of digits is",sum)

#b
mul=1
for i in range(0,len(A)):
    mul*=A[i]
print("the product of digits is",mul)

#c
A.sort()
print("largest element is",A[-1])

#d
print("smallest element is",A[0])