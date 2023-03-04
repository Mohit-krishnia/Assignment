print("Enter how elements you want in fibonacci series")
x=int(input())
a,b=0,1
ar=[]
print("The Fibonacci Sequence is the series of numbers :")
print(a,b,end=" ")
ar.append(a)
ar.append(b)
for value in range(1,x-1):
   c=a+b
   a=b
   b=c
   print(c,end=" ")
   
