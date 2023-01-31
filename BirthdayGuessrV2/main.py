import sets 

constant = "==========> <=========="

age = 0

print(constant)
print(sets.set1)

i = input("Is your birth day in set 1? (write 1 for yes 0 for no) : ")

if i == '1':
	age += 1

print()
print(constant)
print(sets.set2)

i = input("Is your birth day in set 2? (write 1 for yes 0 for no) : ")

if i == '1':
	age += 2
	
print()
print(constant)
print(sets.set3)

i = input("Is your birth day in set 3? (write 1 for yes 0 for no) : ")

if i == '1':
	age += 4

print()
print(constant)
print(sets.set4)

i = input("Is your birth day in set 4? (write 1 for yes 0 for no) : ")

if i == '1':
	age += 8

print()
print(constant)
print(sets.set5)

i = input("Is your birth day in set 5? (write 1 for yes 0 for no) : ")

if i == '1':
	age += 16

print()
print(f"Is your age {age}?")	
input()