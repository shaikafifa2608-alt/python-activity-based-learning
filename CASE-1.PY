
Problem Statement
Read a whole-number size from 3 to 9 and print a hollow numeric diamond. Show an error for sizes outside this range.
Objectives
•	Print a hollow diamond for sizes 3 to 9.
•	Reject sizes outside the allowed range.
Assumptions
•	Use a whole-number size from 3 to 9.
•	The program checks the range, not text input.
Algorithm
1. Read size.
2. Check whether size is from 3 to 9.
3. Use two loops to print the upper and lower diamond.
Flowchart

 
Pseudocode
READ size
IF size outside 3..9: DISPLAY error
ELSE print rows 1..size and size-1..1
code:

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

 