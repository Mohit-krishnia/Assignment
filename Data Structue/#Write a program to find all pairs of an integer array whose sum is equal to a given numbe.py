a=[1,5,7,-1,5]
b=int(input("enter element whose pair you want : "))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==b:
            print(f"{a[i],a[j]}",end = "")