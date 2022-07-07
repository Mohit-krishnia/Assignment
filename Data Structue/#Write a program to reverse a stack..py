a=input("Enter the elements in stack: - ").split(" ")
stack=[]
for i in a:
    stack.append(i)
stack2=[]
for i in range(len(a)):
    stack2.append(stack.pop())
print(stack2)