a = input("enter a string in which non repeating element print -- ")
b = {}
for i in range(0, len(a)):
    s = a[i]
    countn = a.count(a[i])
    b[a[i]] = countn

for i, j in b.items():
    if j == 1:
        print(i)
        break