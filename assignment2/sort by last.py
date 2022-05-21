def last(n):
    return n[-1]
print("how many (a,b) tuple in list you want ")
l1=[]
l2=[]
l3=[]
x=int(input())
for i in range(x):
    l1.append(int(input("a :"))) # (2, 5), (1, 2), (4, 4), (2, 3), (2, 1)
    l2.append(int(input("b :")))
l3=tuple(zip(l1,l2))
print("before sorted ")
print(l3)
print()
print("after sorted ")
print(sorted(l3,key=last))