size = int(input("Enter size (3 to 9): "))
if size < 3 or size > 9:
    print("Invalid size")
else:
    for row in range(1, size + 1):
        if row == 1:
            print(" " * (size - 1) + "1")
        else:
            print(" " * (size - row) + str(row) + " " * (2 * row - 3) + str(row))
    for row in range(size - 1, 0, -1):
        if row == 1:
            print(" " * (size - 1) + "1")
        else:
            print(" " * (size - row) + str(row) + " " * (2 * row - 3) + str(row))

 
