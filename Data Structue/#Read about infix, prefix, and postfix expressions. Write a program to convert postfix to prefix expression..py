def isOperator(x):
    if x in ['+', '-', '*', '/']:
        return True
    else:
        return False


def postToPre(post):
    s = []
    length = len(post)
    for i in range(length):
        if (isOperator(post[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post[i])
    ans = ""
    for i in s:
        ans += i
    return ans


a = input("Enter a postflix string -- ")
print("Prefix : ", postToPre(a))