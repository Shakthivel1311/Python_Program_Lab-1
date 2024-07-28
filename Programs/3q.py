n = 5
alph = 65
for i in range(n):
    print(" " * (n-i), end=" ")
    for j in range(i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()


def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

n = 5
half_pyramid(n)
