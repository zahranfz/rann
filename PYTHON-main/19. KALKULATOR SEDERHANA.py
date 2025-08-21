list_operator = '''1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian'''
print(list_operator)
pilihan = input('Masukkan pilihan: ')
if pilihan == '1':
    data_user = int(input('Masukkan Angka pertama: '))
    data_user2 = int(input('Masukkan Angka kedua: '))

    data_akhir = data_user + data_user2
    print (f'{data_user} + {data_user2} = {data_akhir}')
elif pilihan == '2':
    data_user = int(input('Masukkan Angka pertama: '))
    data_user2 = int(input('Masukkan Angka kedua: '))

    data_akhir = data_user - data_user2
    print (f'{data_user} - {data_user2} = {data_akhir}')
elif pilihan == '3':
    data_user = int(input('Masukkan Angka pertama: '))
    data_user2 = int(input('Masukkan Angka kedua: '))

    data_akhir = data_user * data_user2
    print (f'{data_user} * {data_user2} = {data_akhir}')
else:
    data_user = int(input('Masukkan Angka pertama: '))
    data_user2 = int(input('Masukkan Angka kedua: '))

    data_akhir = data_user/data_user2
    print (f'{data_user} : {data_user2} = {data_akhir}')