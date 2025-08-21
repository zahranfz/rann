ascii_code = ord('a')  # Mengambil kode ASCII dari karakter 'a'
print(f"Kode ASCII dari 'a' adalah {ascii_code}")  # Output: 97

character = chr(97)  # Mengubah kode ASCII 97 menjadi karakter
print(f"Karakter dengan kode ASCII 97 adalah '{character}'")  # Output: 'a'

binary = bin(10)  # Mengubah angka 10 menjadi biner
print(f"Angka 10 dalam biner adalah {binary}")  # Output: 0b1010

hexadecimal = hex(255)  # Mengubah angka 255 menjadi heksadesimal
print(f"Angka 255 dalam heksadesimal adalah {hexadecimal}")  # Output: 0xff

octal = oct(8)  # Mengubah angka 8 menjadi oktal
print(f"Angka 8 dalam oktal adalah {octal}")  # Output: 0o10

# ASCII ke Biner
ascii_value = ord('a')
print(f"Kode ASCII dari 'a' adalah {ascii_value}")  # Output: 97
binary_value = bin(ascii_value)
print(f"Kode ASCII dari 'a' dalam biner adalah {binary_value}")  # Output: 0b1100001

# Biner ke ASCII
binary_string = '0b1100001'  # Biner untuk 'a'
ascii_value_from_binary = int(binary_string, 2)
print(f"Kode ASCII dari biner {binary_string} adalah {ascii_value_from_binary}")  # Output: 97
character_from_binary = chr(ascii_value_from_binary)
print(f"Karakter dari biner {binary_string} adalah '{character_from_binary}'")  # Output: 'a'

# Operator dalam bentuk method
data = "asamakalajaha bahaahahaha"
jumlah_a = data.count('a')  # Menghitung jumlah 'a' dalam string
print(f"Jumlah 'a' dalam string adalah {jumlah_a}")  # Output: 5
b = data.isascii() # Mengecek apakah semua karakter dalam string adalah ASCII
print(f"Apakah semua karakter dalam string adalah ASCII? {b}")  # Output: True