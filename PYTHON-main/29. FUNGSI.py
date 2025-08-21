'''Membuat Fungsi dengan argument'''
import os

'''
def fungsi():
    badan fungsi
'''

'''
    Ini fungsi sapa
'''
os.system('cls')
# def halo_dunia(nama):
#     print(f'Selamat datang {nama}')

# nama = input('Masukkan nama: ')
# halo_dunia(nama)

# '''
#     Ini fungsi tambah
# '''
# def tambah(angka1,angka2):
#     hasil = angka1 + angka2
#     print(f'{angka1} + {angka2} = {hasil}')
# tambah(1,5)

# '''
#     Ini untuk fungsi inputnya
# '''
# def input_angka():
#     angka1 = int(input('Masukkan angka pertama: '))
#     angka2 = int(input('Masukkan angka kedua: '))
#     return angka1, angka2

# '''
#     Ini fungsi perkaliannya
# '''
# def kali(angka1,angka2):
#     hasil = angka1*angka2
#     print(f'{angka1} x {angka2} = {hasil}')

# a, b = input_angka()
# kali(a, b)

# '''
#     fungsi dengan list
# '''
# def say_hi(list_peserta):
#     data_peserta = list_peserta.copy()
#     for peserta in data_peserta:
#         print(f'Selamat datang {peserta}')

# lineup = ['agus','daseng','idan'] # variabel ini akan dimasukkan ke parameter list_peserta
# say_hi(lineup)

# '''
#     fungsi dengan return
# '''
# def kuadrat(x):
#     hasil = x**2
#     return hasil
# a= kuadrat(5)
# print(a)

# def fungsi_tambah(angka1, angka2):
#     return angka1+angka2

# y = fungsi_tambah(4,3)
# print(y)

# def operasi_aritnatika(angka1,angka2):
#     kali = angka1 * angka2
#     bagi = angka1/angka2
#     tambah = angka1+angka2
#     kurang = angka1-angka2
#     return kali, bagi, tambah, kurang

# y = operasi_aritnatika(10,4)
# print(y)

# ka,ba,ta,ku = operasi_aritnatika(10,4)
# print(f'Hasil kali = {ka}')
# print(f'Hasil bagi = {ba}')
# print(f'Hasil tambah = {ta}')
# print(f'Hasil kurang = {ku}')

'''
    fungsi dengan default fungsi
    berfungsi jika kita ingin menginput parameter yang banyak
'''
def sapa(nama, pesan = 'Selamat datang'): # jika tidak menginput parameter kedua akan default
    print(f'Hai {nama}, {pesan}')
sapa('Zahran') # tanpa input parameter kedua # output = Hai Zahran, Selamat datang
sapa('Zahran','Selamat pagi')