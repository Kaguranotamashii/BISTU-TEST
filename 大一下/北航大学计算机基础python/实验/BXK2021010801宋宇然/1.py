import math
a=float(input())
b=float(input())
c=float(input())
p=(a+b+c)/2
print("{:.1f}".format(math.sqrt(p*(p-a)*(p-b)*(p-c))))