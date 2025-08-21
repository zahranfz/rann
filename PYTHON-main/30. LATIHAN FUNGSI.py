# LATIHAN FUNGSI
import os

def header():
    '''FUNGSI HEADER'''
    os.system("cls")
    print(f'{"SELAMAT DATANG":^50}')
    print(f'{"DI PROGRAM PERHITUNGAN LUAS DAN KELILING":^50}')
    print(50*'-')

def input_user():
    '''FUNGSI INPUT USER'''
    lebar = int(input('Masukkan lebar: '))
    panjang = int(input('Masukkan panjang: '))
    return lebar, panjang

def hasil_luas(lebar, panjang):
    '''FUNGSI HASIL LUAS'''
    return lebar*panjang

def hasil_keliling(lebar, panjang):
    '''FUNGSI HASIL KELILING'''
    return 2*(lebar+panjang)

def input_pilihan():
    print(f'Pilih Program\n1. Luas\n2. Keliling\n3. KEDUANYA')
    pilih = int(input('Masukkan pilihan (1/2/3): '))
    return pilih

def pesan(message, value):
    print(f'{message} = {value}')

def opsi(pilih):
    '''FUNGSI PEMILIHAN'''
    if pilih == 1:
        lebar, panjang = input_user()
        hasil = hasil_luas(lebar, panjang)
        pesan('Luas',hasil)
    elif pilih == 2:
        lebar, panjang = input_user()
        hasil = hasil_keliling(lebar, panjang)
        pesan('Keliling',hasil)
    elif pilih == 3:
        lebar, panjang = input_user()
        luas = hasil_luas(lebar, panjang)
        keliling = hasil_keliling(lebar, panjang)
        pesan('Keliling',keliling)
        pesan('Luas',luas)
    else:
        print('pilih yang bener\n')
        pilih = input_pilihan()
        opsi(pilih)

# PROGRAM UTAMA
def main_program():
    '''Program Utama'''
    while True:
        header()
        pilih = input_pilihan()
        opsi(pilih)
        pilihan = input('Apakah ingin melanjutkan? (tekan "y" untuk lanjut): ')
        if pilihan != 'y':
            break

if __name__ == "__main__":
    main_program()