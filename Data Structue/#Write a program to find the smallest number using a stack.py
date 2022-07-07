a=input("Enter the elements in stack: - ").split(" ")
a = input("Enter the elements in stack: - ").split(" ")
stack = []
count = 0
for i in a:
    stack.append(i)
    count += 1
min = stack.pop(count - 1)
for i in stack:
    a = stack.pop()
    if min > a:
        min = a
    else:
        continue
print(min)
