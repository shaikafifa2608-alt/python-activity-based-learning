attended = int(input("Classes attended: "))
held = int(input("Classes held: "))
target = int(input("Target percentage: "))
if held <= 0 or attended < 0 or attended > held or target < 1 or target > 100:
    print("Invalid attendance values")
elif target == 100 and attended < held:
    print("100 percent cannot be reached by attending future classes")
else:
    needed = 0
    while (attended + needed) * 100 / (held + needed) < target:
        needed = needed + 1
    print("Classes to attend:", needed)
