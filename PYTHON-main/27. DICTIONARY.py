import datetime

# DATA DICTIONARY --> ASSOCIATIVE ARRAY
# MEMPERMUDAH AKSES DATA, KARENA TIDAK PERLU MEMASUKKAN INDEX
# SEMUA JENIS DATA BISA DIMASUKKAN KE DALAM DICT, BAHKAN DICT SENDIRI BISA DIMASUKKAN KE DICT
data_dict = {
    1 : 'Zahran',
    2 : 'Agus',
    3 : 'Ilham',
    4 : [True, False]
}
print(f'dict asli = {data_dict}')
print(f'dict dari key(1) = {data_dict[1]}')
print(f'dict dari key(1) dgn get = {data_dict.get(1)}')
print(f'dict dari key(4 index ke 0) = {data_dict.get(4)[0]}')
print(f'info key = {data_dict.keys()}')
print(f'Hapus value ke 3 = {data_dict.pop(3)}')
print(f'info value = {data_dict.values()}')
print(f'Hapus bagian terakhir = {data_dict.popitem()}')
print(f'dict baru = {data_dict}')


# LOOPING DICTIONARY

nama = {
    1 : 'Agus',
    2 : 'Ilham',
    3 : 'Ucup',
    4 : 'Isak'
}

key = nama.keys()
print(key)
value = nama.values()
print(value)
item = nama.items()
print(item)


# Looping untuk mengambil keys

print('\n==================KEYS')
for i in nama.keys():
    print(i)
print('\n==================VALUES')
for i in nama.values():
    print(i)
print('\n==================ITEMS')
for k,i in nama.items():
    print(k,i)
print('\n==================ITEMS WITH INDEX')
for k,i in enumerate(nama.items()):
    print(k,i)


# COPY DICTIONARY
nama = {
    1 : 'Agus',
    2 : 'Ilham',
    3 : 'Ucup',
    4 : 'Isak'
}

ngaran = nama.copy() # agar data yang dicopy berbeda dengan aslinya

print(f'nama mereka = {nama}')
print(f'ngaran maraneh = {ngaran}\n')

nama[1]='Abang'
print(f'nama mereka = {nama}')
print(f'ngaran maraneh = {ngaran}\n')


# NESTING DICTIONARY
mhs1 = {
    'nama':'Zahran Febrian Nugraha',
    'nim':'10098701',
    'sks' : 144,
    'lahir' : datetime.datetime(2007,2,12)
}
mhs2 = {
    'nama':'Agus Imanuel',
    'nim':'10098702',
    'sks' : 140,
    'lahir' : datetime.datetime(2006,3,10)
}
mhs3 = {
    'nama':'Sidra',
    'nim':'10098703',
    'sks' : 142,
    'lahir' : datetime.datetime(2006,4,14)
}
mhs4 = {
    'nama':'Gojo Satoru',
    'nim':'10098704',
    'sks' : 144,
    'lahir' : datetime.datetime(2007,3,19)
}

data_mhs = {
    'MHS001':mhs1,
    'MHS002':mhs2,
    'MHS003':mhs3,
    'MHS004':mhs4
}
print(data_mhs)

print(f'{'KEY':<6} {'NAMA':<30} {'NIM':<10} {'SKS':<5} {'LAHIR':<10}')
print('-'*63)

for mahasiswa in data_mhs:
    key = mahasiswa
    nama = data_mhs[key]['nama']
    nim = data_mhs[key]['nim']
    sks = data_mhs[key]['sks']
    lahir = data_mhs[key]['lahir'].strftime('%x')
    print(f'{key:<6} {nama:<30} {nim:<10} {sks:<5} {lahir:<10}')
