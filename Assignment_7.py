#Question 1
"""

radius=float(input("enter the number"))
def area(radius):
    area=3.14*radius*radius
    return area
ar=area(radius)
print(ar)
"""

#Question 2
"""
n=6
def perfect(n):
 sum=0
 for i in range (1,n):
   if(n%i ==0):
       sum=sum+i
   if(sum==n):
       return True
   else:
       return False
print(perfect(n))
for i in range(1,1001):
    if(perfect(i)==True):
        print(i)
        """

#Question 3
"""
def mul_table(n, i=1):
    print (n*i)
    if i != 10:
        mul_table(n,i+1)
mul_table(12)
"""


#Question 4
"""
def power(a,b):
    if b == 1:
        return a
    else:
        return a * power(a,b-1)
print (power(6,3))
"""

#Question 5
"""
d={}
def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return f
n=int(input("enter a number:"))
d[n]=fact(n)
print(d)
"""

