

list_buku = []
while True:
    print('\nMasukkan Data Buku')
    judul = input('Judul buku\t: ')
    penulis = input('Penulis\t: ')

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print(10*'=' + 'Data Buku baru' + 10*'=')
    for index,buku in enumerate(list_buku):
        print(f'{index+1} | {buku[0]} | {buku[1]}')

    pilihan = input('Apakah ingin menambah buku? (y/n): ')
    if pilihan == 'n':
        break
print('Terimakasih')