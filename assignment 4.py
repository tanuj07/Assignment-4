#Question 1
list=[1,2,3,4,5,6,7,8]
print(list[::-1])

#Question 2
a=input("enter string")
b=len(a)
for i in range(0,b):
    if a[i].isupper():
        print(a[i])

#Question 3
a=input("enter a string")
a = list(map(int, a))
print(a)

#Question 4
a=input("enter string")
b=a[::-1]
if a==b:
    print("pallindrome")
else:
    print("not pallindrome")

#Question 5
import copy as cop
a=[3,4,5,[8,9],1,2]
b=cop.deepcopy(a)
a[3][1]='yes'
print(a)
print(b)