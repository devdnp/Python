# i = 1 -> while i<=10: -> print(f"{i} hello ") -> i += 1
from re import I


total = 0
i = 1
while i<=10:
    total += i
    i += 1
print(total)