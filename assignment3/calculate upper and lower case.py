def con(s):
    count=0
    flag=0
    for i in s:
        if i in s and i.isupper():
            count+=1
        elif i in s and i.islower():
            flag+=1
        else:
            continue
    print("No. of Upper case characters :",count)
    print("No. of Lower case characters :",flag)

a=input("enter the string")
con(a)