a=int(input("how much element you want to enter in list : "))
l=[]
for j in range(1,a+1):
      j=int(input())
      l.append(j)
print("entered list is : ",l)
c=list(map(lambda i: i*3 ,l))
print("output of list  : ",c)