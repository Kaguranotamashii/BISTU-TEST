n = int(input())
line = input()
num = 0
list1= list(line)
for i in range(len(list1)-1):
    if i != len(list1) - 2:
        if list1[i] == '1':
            continue
        else:
            if list1[i + 1] == '0':
                num += 2
            elif list1[i + 1] == '1' and list1[i + 2] == '1':
                continue
            elif list1[i + 1] == '1' and list1[i + 2] == '0':
                num += 1
    else:
        if list1[i] == '1':
            continue
        if list1[i + 1] == '0':
            num += 2
        if list1[i + 1] == '1':
            continue

print(num)