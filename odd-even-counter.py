number =[1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = 0
even = 0
for i in number:
       if i%2!=0:
           odd+=1
       else:
           even+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)