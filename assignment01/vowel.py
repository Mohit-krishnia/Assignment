print("enter the string")
s=input()
v=['a','e','i','o','u']
count=0
for i in s:
    if i in v:
       count+=1
    else:
        continue
print("Vowels:",count)