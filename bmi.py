L = 1.70
w = 80.5
bmi = 80.5/(1.75*1.75)
print(bmi)
s = ''
if bmi <= 18.5:
    s = '轻'
elif bmi <= 25:
    s = '正'
elif bmi <= 28:
    s = '过'
elif bmi <= 32:
    s = '肥'
else:
    s = '严重'
print(s)
s = 0
for x in range(101):
    s += x
print(s)
L = ['Bart', 'Lisa', 'Adam']
for str in L:
    print(str)