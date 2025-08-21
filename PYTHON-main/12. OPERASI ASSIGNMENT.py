# Operasi assignment adalah penyingkatan nilai ke dalam variabel.
# Operasi ini menggabungkan operasi aritmatika dengan penugasan.
# Contoh:
# a = 5
# a += 3  # sama dengan a = a + 3
# a -= 2  # sama dengan a = a - 2
# a *= 4  # sama dengan a = a * 4
# a /= 2  # sama dengan a = a / 2
# a %= 3  # sama dengan a = a % 3
# a //= 2 # sama dengan a = a // 2
# a **= 2 # sama dengan a = a ** 2
# Operasi assignment ini membuat kode lebih ringkas dan mudah dibaca.

print('================== OPERASI ASSIGNMENT ==================')
a = 12
a += 3
print('Nilai a setelah a += 3:', a)  # a = 15
a -= 5
print('Nilai a setelah a -= 5:', a)  # a = 10
a *= 2
print('Nilai a setelah a *= 2:', a)  # a = 20
a /= 4
print('Nilai a setelah a /= 4:', a)  # a = 5.0
a %= 3
print('Nilai a setelah a %= 3:', a)  # a = 2.0
a //= 2
print('Nilai a setelah a //= 2:', a)  # a = 1.0
a **= 2
print('Nilai a setelah a **= 2:', a)  # a = 1.0

# Variabel akan mengikuti operasi terakhir yang dilakukan.

#Operasi bitwise
print('\n================== OPERASI BITWISE ==================')
b = True
print('Nilai b:', b)  # b = True

b &= False
print('Nilai b setelah b &= False:', b)  # b = False

b = True
print('\nNilai b:', b)  # b = True
b |= True
print('Nilai b setelah b |= True:', b)  

b = True
print('\nNilai b:', b)  # b = True
b ^= False
print('Nilai b setelah b ^= False:', b)  

b = True
print('\nNilai b:', b)  # b = True
b = not b
print('Nilai b setelah not b:', b)  #

# Pergeseran bitwise
print('\n================== PERGESERAN BITWISE ==================')
c = 0b1010  # 10 dalam biner
print('Nilai c:', c, ', biner:', format(c, '04b'))  # c = 10
c <<= 2
print('Nilai c setelah c <<= 2:', c, ', biner:', format(c, '04b'))  # c = 40

c = 0b1010  # 10 dalam biner
c >>= 1
print('Nilai c setelah c >>= 1:', c, ', biner:', format(c, '04b'))  # c = 20

# Logika bitwise
print('\n================== LOGIKA BITWISE ==================')
d = 0b1100  # 12 dalam biner
print('Nilai d:', d, ', biner:', format(d, '04b'))  # d = 12

# AND
d &= 0b1010
print('Nilai d setelah d &= 0b1010:', d, ', biner:', format(d, '04b'))  # d = 8

# OR
d = 0b1100  # 12 dalam biner
print('\nNilai d:', d, ', biner:', format(d, '04b'))  # d = 12
d |= 0b0011
print('Nilai d setelah d |= 0b0011:', d, ', biner:', format(d, '04b'))  # d = 11

# XOR
d = 0b1100  # 12 dalam biner
print('\nNilai d:', d, ', biner:', format(d, '04b'))  # d = 12
d ^= 0b0101
print('Nilai d setelah d ^= 0b0101:', d, ', biner:', format(d, '04b'))  # d = 14

# NOT
d = 0b1100  # 12 dalam biner
print('\nNilai d:', d, ', biner:', format(d, '04b'))  # d = 12
d = ~d
print('Nilai d setelah ~d:', d, ', biner:', format(d, '04b'))  # d = -15
