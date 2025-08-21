
print('ENUMERATE')
data_list = [1, 2, 3, 'Zahran', 'Agus', 'Ilham']

for index,data in enumerate(data_list):
    print(f'Index ke = {index}, Data = {data}')

print('\nLIST COMPREHENSION')
data_list = [1, 2, 3, 'Zahran', 'Agus', 'Ilham']
[print(f'data = {i}') for i in data_list]

angka = int(input("Masukkan sampai angka berapa: "))
angka_kuadrat = [i**2 for i in range(angka+1)]
print(f'angka kuadrat = {angka_kuadrat}')