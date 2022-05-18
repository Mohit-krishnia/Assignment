print("enter the string") # converting string first and last character in captialize
s=input()
x=s.split(" ")
print(x)
for i in x:
    if(len(i)==1):
        print(i.capitalize(),end=" ")
    else:
       print(i[0:1].upper()+i[1:-1].lower()+i[-1].upper(),end=" ")
print()