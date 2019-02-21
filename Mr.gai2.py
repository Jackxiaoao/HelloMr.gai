import random
a = []
for i in range(50):
    b = random.randint(-10,11)
    a.append(b)
print("a长度:",len(a))
zheng = []
fu = []
for i in a:
    if(i>0):
        zheng.append(i)
    elif(i<0):
        fu.append(i)
print("正数:",zheng)
print("负数:",fu)