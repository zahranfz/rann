# BOOLEAN LOGIC JUSTIFICATION AND REASONING

# OR , AND , XOR, NOT

# OPERASI BOOLEAN
a = True
b = False
# OR or
c = a or b
print('\n ==============OR==================')
print(a,' OR ', b, '=', c)

a = True
b = True
c = a or b
print(a,' OR ', b, '=', c)

a = False
b = False
c = a or b
print(a,' OR ', b, '=', c)

a = False
b = True
c = a or b
print(a,' OR ', b, '=', c)

# AND and
a = True
b = False
c = a and b
print('\n ==============AND==================')
print(a,' AND ', b, '=', c)

a = True
b = True
c = a and b
print(a, ' AND ', b, '=', c)

a = False
b = False
c = a and b
print(a, ' AND ', b, '=', c)

a = False
b = True
c = a and b
print(a, ' AND ', b, '=', c)

# XOR xor
a = True
b = False
c = a ^ b
print('\n ==============XOR==================')
print(a,' XOR ', b, '=', c)

a = True
b = True
c = a ^ b
print(a, ' XOR ', b, '=', c)

a = False
b = False
c = a ^ b
print(a, ' XOR ', b, '=', c)

a = False
b = True
c = a ^ b
print(a, ' XOR ', b, '=', c)

# NOT not
a = True
c = not a
print('\n ==============NOT==================')
print('NOT', a, '=', c)

a = False
c = not a
print('NOT', a, '=', c)

