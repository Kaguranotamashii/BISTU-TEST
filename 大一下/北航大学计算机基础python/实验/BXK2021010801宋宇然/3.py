import math
x11, x12, x13 = map(int, input().split())
x21, x22, x23 = map(int, input().split())
x31, x32, x33 = map(int, input().split())
print("{:.2f}".format(x11*x22*x33+x12*x23*x31+x13 *
      x21*x32-x13*x22*x31-x12*x21*x33-x11*x23*x32))
