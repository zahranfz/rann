# for loop

for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)

data_str ='Zahran'
for i in data_str:
    print(i)

buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print("Saya suka", item)
# Output: Saya suka apel, dst.

angka = [1, 2, 3, 4, 5]
total = 0
for a in angka:
    total += a
print("Total:", total)
# Output: Total: 15

nilai = {"Ari": 90, "Budi": 85, "Cici": 88}
for nama, skor in nilai.items():
    print(f"{nama} mendapat nilai {skor}")
# Output: Ari mendapat nilai 90, dst.

angka = [1, 2, 3, 4, 5]
kuadrat = [a**2 for a in angka]
print(kuadrat)
# Output: [1, 4, 9, 16, 25]

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
# Output: Perkalian 1-3