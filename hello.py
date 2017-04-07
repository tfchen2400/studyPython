#!/usr/bin/env python3
print('hello,world')
print('i', 'am', 'king!')
print('input some!')
name = input()
print('input', 'is', name)
print(1024 * 768)
print(0xa5b4c3d2);
print('i\'m \"ok\"')
print(r'i m ok \\\\n\\\\ hahahah!')
print('''line1
line2
line3''')

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
print('我是中文')
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
s1 = 72
s2 = 85
r = (85 - 72) / 72
print('%0.1f%%' % r)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
