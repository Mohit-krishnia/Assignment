def Hanoi(n, start, mid, end):
    if n >= 1:
        Hanoi(n - 1, start, end, mid)  # start-->end
        print("Move", n, "from", start, "to", end)
        Hanoi(n - 1, mid, start, end)  # mid-->start


n = int(input("Enter how many disck in tower"))
Hanoi(n, 'A', 'B', 'C')