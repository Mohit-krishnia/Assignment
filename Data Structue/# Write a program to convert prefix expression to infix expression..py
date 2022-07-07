a=input("Enter a preflix string")
b=a[::-1]
stack=[]
for i,j in enumerate(b):  # i=index and j=string char
     if j in ['+','-','*','/']:
         l=f"{stack.pop()}{j}{stack.pop()}"
         stack.append(l)
     else:
         stack.append(j)
L=[]
for i in stack:
    L.append(i)
print("\n")
for i in L[::-1]:
    print(i,end="")