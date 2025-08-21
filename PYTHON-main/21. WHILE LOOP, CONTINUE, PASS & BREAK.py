# while loop

angka = 0
while angka < 5:
    angka += 1
    print('Zahran ganteng')
print('akhir\n')

# pass = berfungsi sebagai dummy, tidak akan dieksekusi
print(5*'='+'pass'+5*'=')
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass
    print(angka)
print('akhir\n')

# continue untuk melanjutkan loop dan skip printah di bawah continue, tergantung kita memerintah darimana
print(5*'='+'continue'+5*'=')
angka = 0
print(f'angka sekarang adalah {angka}')
while angka < 5:
    angka += 1
    if angka == 3:
        print('Udah 3 nih')
        continue

    print(f'angka sekarang adalah {angka}')
print('akhir\n')

# break untuk menghentikan loop
print(5*'='+'break'+5*'=')
angka = 0
print(f'angka sekarang adalah {angka}')
while angka <5:
    angka +=1
    if angka == 3:
        print('Udah 3 nih, udahan ah')
        break
    print(f'angka sekarang adalah {angka}')
print('akhir\n')

print(5*'='+'contoh break'+5*'=')
inputUser = int(input('hitung angka: '))
angka = 0
while True:
    angka += 1
    print(f'angka = {angka}')
    if angka == inputUser:
        print("udah bro")
        break