

# # MEMBUAT DATA PESERTA

peserta0 = ['Jamal', 24, 'Laki-laki']
peserta1 = ['Manuel', 21, 'Laki-laki']
peserta2 = ['Indah', 19, 'Perempuan']
peserta3 = ['Sri', 20, 'Perempuan']
peserta4 = ['Zahran', 18, 'Laki-laki']

list_peserta = [peserta0,peserta1,peserta2,peserta3,peserta4]

for i in list_peserta:
    print(f'Nama\t: {i[0]}')
    print(f'Umur\t: {i[1]}')
    print(f'Gender\t: {i[2]}\n')

biodata = [['Zahran', 18, 'Laki-laki'],['Manuel', 21, 'Laki-laki'],['Indah', 19, 'Perempuan']]
for j in biodata:
    print(f'Nama\t: {j[0]}\nUmur\t: {j[1]}\nGender\t: {j[2]}\n')

biodata = [['Zahran', 18, 'Laki-laki'],['Manuel', 21, 'Laki-laki'],['Indah', 19, 'Perempuan']]
biodataCopy = biodata.copy()
print(f'adress dari biodata = {hex(id(biodata))}')
print(f'adress dari biodata copy= {hex(id(biodataCopy))}')

# Kedua address sudah berbeda, namun address elemen(member list) tetap sama
print(f'adress elemen ke 1 dari biodata = {hex(id(biodata[0]))}')
print(f'adress elemen ke 1 dari biodata copy = {hex(id(biodataCopy[0]))}')

# Jika address member sama, ketika kita merubah elemen di dalam list, maka list copy akan ikut berubah
biodata[0][0] = 'Asep'
print(f'List biasa = {biodata}')
print(f'List copy = {biodataCopy}')

# agar address dari masing2 elemen berbeda kita harus melakukan deepcopy
# menggunakan = from copy import deepcopy

from copy import deepcopy
biodata = [['Zahran', 18, 'Laki-laki'],['Manuel', 21, 'Laki-laki'],['Indah', 19, 'Perempuan']]
biodataDeepcopy = deepcopy(biodata)
print(f'address list asli = {hex(id(biodata))}')
print(f'address list copy = {hex(id(biodataDeepcopy))}')
print(f'address list asli elemen ke 1 = {hex(id(biodata[0]))}')
print(f'address list copy elemen ke 1 = {hex(id(biodataDeepcopy[0]))}')

#Jadi ketika kita mengganti suatu elemen dalam list asli, list copy tidak akan berubah


