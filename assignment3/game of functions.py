def su(lis):
    sum=0
    for i in lis:
        sum=sum+i
    print(sum)

print("how many no. you want to add")
a=int(input())
l=[]
for i in range(0,a):
     b=int(input())
     l.append(b)
print(l)
su(l)