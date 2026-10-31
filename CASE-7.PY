rows = 2
columns = 2
reserved_row = int(input("Reserved row (1 or 2): "))
reserved_column = int(input("Reserved column (1 or 2): "))
row = 1
while row <= rows:
    column = 1
    line = ""
    while column <= columns:
        if row == reserved_row and column == reserved_column:
            line = line + "XX "
        else:
            line = line + str(row) + str(column) + " "
        column = column + 1
    print(line)
    row = row + 1
