size = int(input())
for i in range(size):
    for j in range(i):
        print(" ", end="")
    for j in range(size, i, -1):
        print("*", end="")
    print()