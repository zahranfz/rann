# # MEMBUAT SEGITIGA BINTANG siku siku

bintang = int(input("Masukkan tinggi segitiga: "))
print('========== INI FOR LOOP ===========')
count = 1
for i in range(bintang):
    print('*'*count)
    count +=1
print('===== AKHIR DARI FOR LOOP ====\n')

print('========== INI WHILE LOOP ===========')
# bintang = int(input('Masukkan tinggi segitiga: '))
count = 1
while True:
    print('*'*count)
    count += 1
    if count > bintang:
        break
print('========== AKHIR DARI WHILE LOOP ===========\n')

# AMBIL YANG JUMLAHNYA GANJIL

print('========== GANJIL ===========')
# bintang = int(input('Masukkan tinggi segitiga: '))
# bintang = int(input('Masukkan tinggi segitiga: '))
count = 1
loop = True
while loop:
    if count%2:
        print('*'*count)
        count += 1
    else:
        count += 1
        continue
    if count > bintang:
        break
print('========== AKHIR GANJIL ===========\n')

print('========== SAMA KAKI ===========')
# bintang = int(input('Masukkan tinggi segitiga: '))
# bintang = int(input('Masukkan tinggi segitiga: '))
count = 1
spasi = int(bintang/2)
loop = True
while loop:
    if count%2:
        print(' '*spasi,'*'*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > bintang:
        break
print('========== AKHIR SAMA KAKI ===========\n')


print('========== BENTUK TERBALIK ===========')
# bintang = int(input('Masukkan tinggi segitiga: '))
count = bintang
while True:
    print('*'*count)
    count -= 1
    if count == 0:
        break
print('========== END ===========\n')

print('========== BENTUK TERBALIK GANJIL ===========')
# bintang = int(input('Masukkan tinggi segitiga: '))
count = bintang
while True:
    if count%2:
        print('*'*count)
        count -= 1
    else:
        count -=1
        continue
    if count == 0:
        break
print('========== UDAHAN BANG ===========\n')