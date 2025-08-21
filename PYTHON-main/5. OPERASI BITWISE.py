# OPERASI BITWISE


a = 9
b = 5

# OR |
c = a | b
print('\n ==============OR==================')
print ('nilai a:', a,', binary:', format(a, '08b'))
print ('nilai b:', b,', binary:', format(b, '08b'))
print ('hasil a | b:', c,', binary:', format(c, '08b'))

# AND &
d = a & b
print('\n ==============AND==================')
print ('nilai a:', a,', binary:', format(a, '08b'))
print ('nilai b:', b,', binary:', format(b, '08b'))
print ('hasil a & b:', d,', binary:', format(d, '08b'))

# XOR ^
e = a ^ b
print('\n ==============XOR==================')
print ('nilai a:', a,', binary:', format(a, '08b'))
print ('nilai b:', b,', binary:', format(b, '08b'))
print ('hasil a ^ b:', e,', binary:', format(e, '08b'))

# NOT ~
f = ~a
print('\n ==============NOT==================')
print ('nilai a:', a,', binary:', format(a, '08b'))
print ('hasil ~a:', f,', binary:', format(f, '08b'))

# LEFT SHIFT <<
g = a << 2
print('\n ==============LEFT SHIFT==================')
print ('nilai a:', a,', binary:', format(a, '08b'))
print ('hasil a << 2:', g,', binary:', format(g, '08b'))

# RIGHT SHIFT >>
h = a >> 2
print('\n ==============RIGHT SHIFT==================')
print ('nilai a:', a,', binary:', format(a, '08b'))
print ('hasil a >> 2:', h,', binary:', format(h, '08b'))
