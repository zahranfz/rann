# MEMBUAT OPERASI RANGE ANGKA

# ----------5________________10----------
inputUser = float(input('Masukkan angka yang:\nLebih besar dari 10 atau Lebih kecil dari 5 \nMasukkan: '))

isKurangdari5 = (inputUser<5)
print('Lebih kecil dari 5:', isKurangdari5)

isLebihdari10 = (inputUser>10)
print('Lebih besar dari 10:', isLebihdari10)

isBenar = isKurangdari5 or isLebihdari10
print("nilai nya bernilai =", isBenar)

# __________5----------10___________
inputUser = float(input('Masukkan angka yang:\nLebih besar dari 5 dan Lebih kecil dari 10\nMasukkan: '))

isKurangdari10 = (inputUser < 10)
print('Lebih kecil dari 10:', isKurangdari10)

isLebihdari5 = (inputUser > 5)
print('Lebih besar dari 5:', isLebihdari5)

isBenar = isKurangdari10 and isLebihdari5
print("nilai nya bernilai =", isBenar)


# __________0----------5___________8---------11________
inputUser = float(input('Masukkan angka yang:\nLebih besar dari 0 dan Lebih kecil dari 5 atau Lebih besar dari 8 dan Lebih kecil dari 11\nMasukkan: '))
isKurangdari5lebihdari0 = (inputUser < 5 and inputUser > 0)
isLebihdari8Kurangdari11 = (inputUser > 8 and inputUser < 11)
print('Lebih kecil dari 5 dan lebih besar dari 0:', isKurangdari5lebihdari0)
print('Lebih besar dari 8 dan lebih kecil dari 11:', isLebihdari8Kurangdari11)
isBenar = isKurangdari5lebihdari0 or isLebihdari8Kurangdari11
print("nilai nya bernilai =", isBenar)


# --------0_________5----------8___________11----------
a = float(input('Masukkan angka yang: \nKurang dari 0 atau Lebih besar dari 5 dan Kurang dari 8 atau Lebih besar dari 11\nMasukkan: '))
b = (a < 0)
c = (a > 5 and a < 8)
d = (a > 11)
print('Kurang dari 0:', b)
print('Lebih besar dari 5 dan kurang dari 8:', c)
print('Lebih besar dari 11:', d)
isBenar = b or c or d
print("nilai nya bernilai =", isBenar)