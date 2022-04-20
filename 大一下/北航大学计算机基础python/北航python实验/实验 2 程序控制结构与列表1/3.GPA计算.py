# n = int(input())
# score = []
# xuefen = []
# fenzi = 0.0
# fenmu = 0.0
# for i in range(n):
#     a, b = map(int, input().split())
#     score.append(a)
#     xuefen.append(b)
# student_len = len(score)
# for i in range(student_len):
#     if (int(score[i]) < 60):
#         gpa = 0
#     elif (int(score[i]) >= 60):
#         gpa = 4 - 3 * (100 - score[i] ** 2 / 1600)
#     fenzi = fenzi + (gpa * int(xuefen[i]))
# fenmu = sum(xuefen)
# print('%.2f' % (fenzi / fenmu))


n = int(input())
s = 0
h = 0
for i in range(1, n + 1):
    a, b = map(float, input().split())
    if a < 60:
        t = 0
    else:
        t = 4 - 3 * (100 - a) ** 2 / 1600
    s = s + t * b
    h = h + b
gpa = s / h
print('%.2f' % gpa)
