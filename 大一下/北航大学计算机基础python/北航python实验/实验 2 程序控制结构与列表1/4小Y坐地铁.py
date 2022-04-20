score = []
# 第一天
oneday = map(int, input().split())
twoday = map(int, input().split())
threeday = map(int, input().split())
oneday = sum(oneday)
twoday = sum(twoday)
threeday = sum(threeday)
zuixiaopiao1=0
zuixiaopiao2=0
sumScore = oneday + twoday + threeday
if (sumScore > 40):
    zuixiaopiao1=sumScore-40

if (oneday >= 15):
    oneday = 15
if (twoday >= 15):
    twoday = 15
if (threeday >= 15):
    threeday = 15
zuixiaopiao2=sumScore-(oneday+twoday+threeday)
if(zuixiaopiao1<=zuixiaopiao2):
    print(zuixiaopiao2)
elif(zuixiaopiao1>zuixiaopiao2):
    print(zuixiaopiao1)
