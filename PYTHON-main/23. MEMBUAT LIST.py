dataList = [i for i in range(0,11)]
print (f'Ini adalah data list normal = {dataList}')

dataList2 = [i**2 for i in range(0,11)]
print(f'data list kuadrat = {dataList2}')

dataList2 = [i for i in range(0,11,3)] # range(start, stop, step)
print(f'data list loncat 3 = {dataList2}')

dataListGenap = [i for i in range (0,11) if i%2 == 0]
print(f'Ini adalah list Genap = {dataListGenap}')

dataListGanjil = [i for i in range(0,11) if i%2 !=0]
print(f'Ini adalah list Ganjil = {dataListGanjil}')

print(f'Index ke 1 dari data ganjil bernilai = {dataListGanjil[1]}')
print(f'Nilai 3 dalam data ganjil memiliki indeks ke-{dataListGanjil.index(3)}')