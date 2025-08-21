# generic

nama = 'Zahran'
alamat = 'Jakarta'
str = 'Nama saya ' + nama + ' Umur saya 20 ' + 'alamat saya di ' + alamat
print(str)

a = 'Zahran'
umur = 20
b = 'Jakarta'
str2 = f'Nama saya {a} Umur saya {umur} alamat saya di {b}'
print(str2)

angka = 20.5
formatStr = f'angka = {angka}'
print(formatStr)

# bilangan bulat
angkaBulat = 100
formatBulat = f'angka bulat = {angkaBulat}'
print(formatBulat)

# bilangan ribuan
angkaRibuan = 1000
formatRibuan = f'angka ribuan = {angkaRibuan:,}'
print(formatRibuan)

# bilangan desimal
angkaDesimal = 1000.52657
formatDesimal = f'angka desimal = {angkaDesimal:.2f}'
print(formatDesimal)

# bilangan desimal ribuan
angkaDesimalRibuan = 1000.52657
formatDesimalRibuan = f'angka desimal ribuan = {angkaDesimalRibuan:,.2f}'
print(formatDesimalRibuan)

# Cara membulatkan angka
angkaPembulatan = 1000.52657
formatPembulatan = f'angka pembulatan = {angkaPembulatan:.0f}'
print(formatPembulatan)

# bilangan desimal dengan tanda +
angkaDesimalPlus = 1000.52657
formatDesimalPlus = f'angka desimal dengan tanda + = {angkaDesimalPlus:+.2f}'
print(formatDesimalPlus)

# bilangan desimal dengan tanda -
# Jika angka negatif, maka tanda - akan muncul
angkaDesimalMinus = -1000.52657
formatDesimalMinus = f'angka desimal dengan tanda - = {angkaDesimalMinus:-.2f}'
print(formatDesimalMinus) 

# Cara membagi angka tapi hasilnya dibulatkan
angkaPembagian = 1000 // 3
formatPembagian = f'angka pembagian = {angkaPembagian}'
print(formatPembagian)

# Cara membagi angka tapi hasilnya dibulatkan ke atas
import math
angkaPembagianAtas = math.ceil(1000 / 3)
formatPembagianAtas = f'angka pembagian atas = {angkaPembagianAtas}'
print(formatPembagianAtas)
bilangan_phi = math.pi
print(f'Phi = {bilangan_phi}')  # Phi = 3.14

# format persen
angkaPersen = 0.25
formatPersen = f'angka persen = {angkaPersen:.2%}'
print(formatPersen)