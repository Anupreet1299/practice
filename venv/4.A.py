"""
 sequences in python
list, tuple, string, set, dictionary
operations performed on sequnces are
 1. concatination
 2. repitition
3. membership testing
4. slicing
5. indexing

list in python
"""
"""

students = ["john", "jessie", "anupama", "arash", "ekpreet"]
print(students, type(students))
#concatination

print(students + ["manmeet", "karan"])

print("========")

#repetition
print(students*2)
print(students*3)
print("========")

#membership testing
print("arash" in students)
print("karan" in students)

print("========")

#object slicing

print(students[1:5])

#indexing

print(students[0])
print(students[4])

#tuple

students = ("john", "jessie", "anupama", "arash", "ekpreet")
print(students, type(students))

#operations on tuple
#1. concatination

print(students + ("mini", "karan"))
#2. repetition

print(students*2)
print()

# 3. membership testing

print("john" in students)

# 4. slicing
print(students[1:3])
print()
#5. indexing

print(students[4])
print("======================================")
"""

#sets in python

students = {"john", "jessie", "anupama", "arash", "ekpreet"}
print(students, type(students))

#1. concatination

#print(students + ["karan", "mini"])

#2. repetition

#print(students*2)

#3. membership testing

print("arash" in students)

#4. slicing

#print(students[1:3])

#5. indexing
print(students[1])












