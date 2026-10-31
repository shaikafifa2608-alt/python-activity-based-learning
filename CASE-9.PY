start = int(input("First day (0=Mon to 6=Sun): "))
days = int(input("Number of days (28 to 31): "))
if start < 0 or start > 6 or days < 28 or days > 31:
    print("Invalid calendar values")
else:
    print("Mon Tue Wed Thu Fri Sat Sun")
    line = "    " * start
    position = start
    day = 1
    while day <= days:
        if day < 10:
            line = line + "  " + str(day) + " "
        else:
            line = line + str(day) + "  "
        position = position + 1
        if position == 7:
            print(line)
            line = ""
            position = 0
        day = day + 1
    if line != "":
        print(line)
