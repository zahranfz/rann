nama = [1, 2, 3, 4, 5]

nama.append(6)
print(f'tambahan nilai menjadi {nama}')

# insert berfungsi sebagai penambah nilai di index ke- (ex: (3, 3.5))
nama.insert(3, 3.5)
print(f'insert nilai 3.5 di index ke-3 jadi {nama}')

nama1=nama.reverse()
print(f'reverse nya adalah {nama}')

# Untuk mencopy nilai list
nama1=nama.copy()
print(nama1)
print(f'jumlah dari list adalah {len(nama)}')

print(nama.index(1))

# Reverse untuk membalik nilai
nama1=nama.reverse()
print(nama)

# Extend sebagai fungsi untk menambah beberapa nilai kedalam list
nama_baru = [7, 8, 9]
nama.extend(nama_baru)
print(f'extend/menambahkan beberapa data sekaligus menjadi\n{nama}')


# Nested list
list_baru= [[123, 345, 678], ['zahran', 'alex'], [12.5, 15.6, 19.7]]
print(list_baru)

# Mengambil nilai dari index list, misal ingin mengambil elemen pertama dari list_baru
print(list_baru[0])  # Output: [123, 345, 678]

# Jika ingin mengambil elemen tertentu dari sublist, misal elemen kedua dari sublist pertama
print(list_baru[0][1])  # Output: 345

# Untuk menambahkan nilai baru kedalam list
kota = ['cms', 'jkt', 'tsk']
list_baru.append(kota)
print(list_baru)

# Menambahkan beberapa nilai kedalam list
listBaru1=[[True, False], [44, 21, 39]]
list_baru.extend(listBaru1)
print(list_baru)

# Untuk mengambil nilai dari index ke-
print(list_baru[3])

name = 'indra'
list_baru[1].append(name)
print(list_baru)

print(list_baru[1][2])