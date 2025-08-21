x = "hello world"
y = "i am python"
#indeks
print(x[0]) # h

print(f"indeks ke 0 dari x adalah {x[0]}")
print(f"indeks ke 3 dari y adalah {y[3]}")

#slice berfungsi untuk memotong string
print(x[0:5]) # hello
print(x[0:5:2]) # hlo
print(x[0:5:3]) # h
print(y[0:5]) # i am p
print(y[0:5:2]) # i a
print(y[0:5:3]) # i

#len berfungsi untuk menghitung panjang string
print(len(x)) # 11
print(len(y)) # 10
