import random
a = []
for i in range(20):
    num = random.choice(range(10))
    a.append(num)
print("a长度:",len(a))
print("未排序a:",a)
a[::2] = sorted(a[::2],reverse=True)
print("排序a:",a)