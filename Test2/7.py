import time as t

now = int(t.time()%26)

print(f"A random character is {chr(ord('A')+now)}")