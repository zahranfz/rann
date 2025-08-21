import datetime
import os
import string
import random

template = {
    'nama':'Zahran',
    'nim' : '1111111111',
    'sks' : 144,
    'lahir' : '2000,2,12'
}

data_mhs = {}
while True:
    os.system("cls")
    print(f'{'SELAMAT DATANG':^20}')
    print(f'{'DATA MAHASISWA':^20}')
    print('-'*20)

    mahasiswa = dict.fromkeys(template)
    mahasiswa['nama']=input('Masukkan nama: ')
    
    while True:
        gender_input = input('Masukkan jenis kelamin:\n1.Laki-laki\n2.Perempuan\nMasukkan pilihan: ')
        if gender_input in ['1','Laki-laki','L','laki-laki','laki laki', 'LAKI LAKI', 'LAKI-LAKI','LAKI','l','lelaki','LELAKI','Lelaki']:
            mahasiswa['gender'] = 'L'
            break
        elif gender_input in ['2','Perempuan','P','perempuan','PEREMPUAN','p']:
            mahasiswa['gender'] = 'P'
            break
        else:
            print('Input tidak valid, silakan coba lagi.')
    while True:
        input_nim = input('Masukkan NIM: ')
        if len(input_nim) == 10:
            break
        print('NIM harus lebih dari 10 karakter')
    mahasiswa['nim'] = input_nim
    mahasiswa['sks']=int(input('Masukkan jumlah SKS: '))
    while True:
        tahun = input('Masukkan tahun  lahir (YYYY): ')
        bulan = input('Masukkan bulan  lahir (1-12): ')
        tanggal = input('Masukkan tanggal  lahir (1-31): ')
        if len(tahun) == 4 and tahun.isdigit():
            tahun = int(tahun)
        else:
            print('Tahun lahir harus 4 digit angka')
            continue
        if bulan.isdigit() and 1 <= int(bulan) <= 12:
            bulan = int(bulan)
        else:
            print('Format bulan salah (1-12)')
            continue
        if tanggal.isdigit() and 1 <= int(tanggal) <= 31:
            tanggal = int(tanggal)
        else:
            print('Format tanggal salah (1-31)')
            continue
        break
        print('Format (DD/D)')
    mahasiswa['lahir']=datetime.datetime(tahun, int(bulan), int(tanggal)).strftime('%x')
    
    kunci = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mhs.update({kunci:mahasiswa})

    print(f'{'KEY':<6} {'NAMA':<30} {'NIM':<10} {'Gender':<10} {'SKS':<5} {'LAHIR':<10}')
    print('-'*75)

    for mahasiswa in data_mhs:
        key = mahasiswa
        nama = data_mhs[key]['nama']
        gender = data_mhs[key]['gender']
        nim = data_mhs[key]['nim']
        sks = data_mhs[key]['sks']
        lahir = data_mhs[key]['lahir']
        print(f'{key:<6} {nama:<30} {input_nim:<10} {gender_input:<10} {sks:<5} {lahir:<10}')
    print('='*10+'\nLanjut?(y/n)\n'+'='*10)
    pilihan = input('Masukkan pilihan anda: ')
    if pilihan == 'n':
        break