n = int(input())
print(n)
while(n!=1):
    if (n % 2 == 0):
        n /= 2
        print(int(n))
    elif (n % 2 != 0):
        n = 3 * n + 1
        print(int(n))
