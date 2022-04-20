a = input().split()
a_len = len(a)
b = []
for i in range(0, a_len, 2):
    for j in range(int(a[i])):
        b.append(int(a[i + 1]))
b.append(max(b))
b.append(b.count(int(max(b)))-1)
print(*b)
