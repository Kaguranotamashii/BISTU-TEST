import math
n = int(input())
p = float(input())
m = float(input())
print("0" * n)
print(math.floor(p * (m + 15)))
if p > 2.0 and m > 0:
    print(True)
else:
    print(False)
