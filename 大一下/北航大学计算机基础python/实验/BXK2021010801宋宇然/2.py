import math

t = float(input())
n = int(input())
v = float(input())
shu = math.ceil(t/n)/v
print("{:.3f} {:.0f}".format(t/n, shu))
