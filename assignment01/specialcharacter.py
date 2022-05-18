print("enter the string")
s=input()
for i in s:
    if i.isalpha() or i==" " or i.isdigit():
        continue
    else:
        print("String is not accepted")
        break
if i.isalpha() or i==" " or i.isdigit():
    print("String is accepted")