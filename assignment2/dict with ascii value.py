print("hello")
l=[]
s=[]
for i in range(97,123):
    x=chr(i)
    print(x,end=" ")
    print(i,end=' ')
    s.append(i)
    l.append(x)
print()
p=dict(zip(l,s))
print(p)