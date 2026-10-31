mark1 = int(input("Mark 1: "))
mark2 = int(input("Mark 2: "))
mark3 = int(input("Mark 3: "))
total = mark1 + mark2 + mark3
average = total / 3
print("Total:", total)
print("Average:", average)
if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    print("Pass")
else:
    print("Fail")
