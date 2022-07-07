def check(s):
    l = []
    for i in s:
        if i in ["(", "{", "["]:
            l.append(i)
        else:
            if not s:
                return False
            current = l.pop()
            if current in ['(','{',"["]:
                if i not in [")",'}',"]"]:
                    return False

    if l:
        return False
    return True

snippet=input("enter the snippet to check")

if check(snippet):
    print("Balanced")
else:
    print("Not Balanced")