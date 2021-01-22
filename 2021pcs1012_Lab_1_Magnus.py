def matrix(total):
    print("Enter (0 for loss), (1 for tie) and (2 for win) against other players: ")
    a = [[int(input("Enter: ")) for x in range(total)] for y in range(total)]
    x = 2
    b = []

    for i in range(0,total):
        c = a[i].count(x)
        b.append(c)

    print(b)
    #b = str(b)
    d = b.index(max(b)) + 1
    d = str(d)
    print("The Magnus is " + d)

total = (int(input("Total number of players: ")))
matrix(total)