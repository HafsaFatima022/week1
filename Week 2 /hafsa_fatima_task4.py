# ============================================================
#  BioSkillz CodeStart — Python Foundations | Batch 01
#  TASK 04: Lists & Tuples (Session 04)
# ============================================================
#
#  Name            : Hafsa Fatima
#  GitHub username : HafsaFatima022
#  Date            : 27-11-2026
#  ⚠ BEFORE YOU START
#  Practise the Session 04 examples and the Week 2 Reference
#  Guide first. Try every question yourself before asking for
#  help. Errors are part of learning!
#
#  HOW TO SUBMIT
#  1. Write your code under each question in this file.
#  2. Run the file in VS Code and make sure it works.
#  3. Rename it to:  yourname_task_04.py   (no spaces)
#                    e.g. ali_raza_task_04.py
#  4. Upload it to your GitHub repository.
#  5. Submit your GitHub link as instructed by the team.
#
#  DEADLINE: Friday, 27 November 2026, 9:00 PM (PKT)
#
#  TIP: Code shown inside comments (lines starting with #) does
#  not run. To test it, copy it below and remove the #.
# ============================================================


# ############################################################
#  PART A: SESSION EXERCISES (from the slides)
# ############################################################

# ------------------------------------------------------------
# Exercise 1: Predict the output
# ------------------------------------------------------------
# Write your prediction for each snippet. Then copy the code
# below, run it, and check.
#
# 1)  nums = [3, 1, 2]
#     nums.append(5)
#     print(nums)
#     My prediction: [3, 1, 2, 5]
#
# 2)  print([10, 20, 30, 40][1:3])
#     My prediction: [20, 30]
#
# 3)  a = [1, 2]
#     b = a
#     b.append(3)
#     print(a)
#     My prediction: [1, 2, 3]  (b and a are points to same memory address)
#
# 4)  x = [5, 2, 8]
#     print(x.sort())
#     My prediction: None  (sort() changes the list but returns None)
#
# 5)  t = (5,)
#     print(type(t))
#     My prediction: <class 'tuple'>
#
# 6)  print(len([[1, 2], [3, 4]]))
#     My prediction: 2
#===========================================================
# Your code goes here:
#===========================================================
nums = [3, 1, 2]
nums.append(5)
print(nums)                         # 1

print([10, 20, 30, 40][1:3])        # 2

a = [1, 2]
b = a
b.append(3)
print(a)                            # 3

x = [5, 2, 8]
print(x.sort())                     # 4

t = (5,)
print(type(t))                      # 5

print(len([[1, 2], [3, 4]]))        # 6
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Exercise 2: Find and fix 4 bugs
# ------------------------------------------------------------
# This program should add 88 and 50 to the list, print the
# last mark, print the sorted list, and then try to change a
# point. It has 4 bugs.
#
#     marks = [72, 95, 64]
#     marks.append(88, 50)
#     print("Last:", marks[5])
#
#     best = marks.sort()
#     print("Sorted:", best)
#
#     point = (3, 4)
#     point[0] = 5
#
# Write the fixed program below, and add a comment next to
# each fix explaining the bug.
#===========================================================
# Your code goes here:
#===========================================================
marks = [72, 95, 64]
marks.append(88)                    # append() takes only ONE item; call it twice (or use extend)
marks.append(50)
print("Last:", marks[-1])           # marks[5] is out of range (indexes are 0-4); use -1 for the last item

best = sorted(marks)                # sort() returns None; use sorted() to get a new sorted list
print("Sorted:", best)

point = (3, 4)
point = (5, point[1])               # tuples are immutable; build a new tuple instead of point[0] = 5
print("Point:", point)
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Exercise 3: To-do list manager
# ------------------------------------------------------------
# Write a program with a menu that repeats (while True):
#   1. Add a task      -> ask for a task and append it
#   2. Remove a task   -> ask for a task and remove it
#                         (print a message if it isn't there)
#   3. Show tasks      -> print each task with its number
#   4. Quit            -> break
#
# Example:
#   1) Add  2) Remove  3) Show  4) Quit
#   Choose: 1
#   Task: Practise loops
#   Choose: 3
#   1. Practise loops
#
#===========================================================
# Your code goes here:
#===========================================================
tasks = []

while True:
    print("1) Add  2) Remove  3) Show  4) Quit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
    elif choice == "2":
        task = input("Task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Removed:", task)
        else:
            print("That task isn't in the list.")
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
#===========================================================
#===========================================================
# ############################################################
#  PART B: TASKS
# ############################################################

# ------------------------------------------------------------
# Task 1: List explorer
# ------------------------------------------------------------
# Ask the user to type 5 numbers on ONE line, separated by
# spaces. Turn them into a list of integers, then print:
#   - the sorted list
#   - the sum, the average, the largest and the smallest
#
# Example:
#   Enter 5 numbers: 12 5 30 8 20
#   Sorted : [5, 8, 12, 20, 30]
#   Sum    : 75
#   Average: 15.0
#   Largest: 30
#   Smallest: 5
#
# Hint: input().split() gives a list of strings. Use a loop
# with int() and append() to build a list of numbers.
#
#===========================================================
# Your code goes here:
#===========================================================
text = input("Enter 5 numbers: ")
parts = text.split()

numbers = []
for p in parts:
    numbers.append(int(p))

print("Sorted :", sorted(numbers))
print("Sum    :", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Task 2: Predict the output
# ------------------------------------------------------------
# Write your prediction first, then run the code to check.
# If your prediction was wrong, write one line explaining why.
#
# 1)  print([1, 2, 3] * 2)
#     My prediction: [1, 2, 3, 1, 2, 3]
#
# 2)  x = [4, 7, 1]
#     x.insert(1, 9)
#     print(x)
#     My prediction: [4, 9, 7, 1]
#
# 3)  y = [1, 2, 2, 3]
#     y.remove(2)
#     print(y)
#     My prediction: [1, 2, 3]  (remove() deletes only the first 2)
#
# 4)  print(sorted([3, 1, 2], reverse=True))
#     My prediction: [3, 2, 1]
#
# 5)  a, b, c = (1, 2, 3)
#     print(b)
#     My prediction: 2
#
# 6)  print(" ".join(["Code", "Start"]))
#     My prediction: Code Start
#===========================================================
# Your code goes here:
#===========================================================
print([1, 2, 3] * 2)                # 1

x = [4, 7, 1]
x.insert(1, 9)
print(x)                            # 2

y = [1, 2, 2, 3]
y.remove(2)
print(y)                            # 3

print(sorted([3, 1, 2], reverse=True))  # 4

a, b, c = (1, 2, 3)
print(b)                            # 5

print(" ".join(["Code", "Start"]))  # 6
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Task 3: Find and fix the bugs
# ------------------------------------------------------------
# This program should add "zara" to the list, print every
# name in title case, remove "sara", and print the total.
# It has 4 bugs.
#
#     names = ["ali", "sara", "omar"]
#     names.add("zara")
#
#     for i in range(len(names) + 1):
#         print(names[i].title())
#
#     names.remove("Sara")
#     print("Total:", len(names)
#
# Write the fixed program below, and add a comment next to
# each fix explaining the bug.
#===========================================================
# Your code goes here:
#===========================================================
names = ["ali", "sara", "omar"]
names.append("zara")                # Bug 1: lists have append(), not add()

for i in range(len(names)):         # Bug 2: len(names) + 1 goes one index too far (IndexError)
    print(names[i].title())

names.remove("sara")                # Bug 3: the list holds "sara" (lowercase); "Sara" is not found
print("Total:", len(names))         # Bug 4: missing closing parenthesis
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Task 4: Remove duplicates (without sets)
# ------------------------------------------------------------
# Start with this list:
#     numbers = [3, 7, 3, 9, 7, 1, 3]
# Build a NEW list that keeps only the first copy of each
# number, in the original order. Use a loop and "not in".
#
# Expected output:
#   [3, 7, 9, 1]
#
# (In Session 05 you'll learn sets, which make this easier.)
#
#===========================================================
# Your code goes here:
#===========================================================
numbers = [3, 7, 3, 9, 7, 1, 3]
unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Task 5: Your field
# ------------------------------------------------------------
# Solve a small problem from YOUR field using lists or tuples.
# Choose ONE option (or create your own):
#
#   Option A: Codons
#     Ask for a DNA sequence (e.g. ATGGCCTAA). Split it into a
#     list of 3-letter codons using slicing in a loop, then
#     print the list and the number of codons.
#     Example: ['ATG', 'GCC', 'TAA'] -> 3 codons
#
#   Option B: Readings above a threshold
#     Store at least 6 lab readings in a list. Ask for a
#     threshold value and print a new list of the readings
#     above it, plus how many there are.
#
#   Option C: Your own idea
#     Any problem from your subject that uses a list or tuple.
#     Describe it in a comment first.
#===========================================================
# Your code goes here:
#===========================================================
# Option A: Codons
dna = input("Enter a DNA sequence: ").strip().upper()
codons = []

for i in range(0, len(dna) - 2, 3):     # step by 3; stops before an incomplete last codon
    codons.append(dna[i:i + 3])

print(codons)
print(len(codons), "codons")
#===========================================================
#===========================================================
