c0 = int(input("Enter a number: "))
if c0 < 1:
    print("Use a non-negative, non-zero number")
else:
    steps = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = int(c0 / 2)
        else:
            c0 = 3 * c0 + 1
        print(c0)
        steps = steps + 1

print("Total number of steps: ", steps)