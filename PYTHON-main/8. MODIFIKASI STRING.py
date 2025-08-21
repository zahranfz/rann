x = "hello world"
#upper() berfungsi untuk mengubah huruf kecil menjadi huruf besar
print(x.upper())
#lower() berfungsi untuk mengubah huruf besar menjadi huruf kecil
print(x.lower())
#title() berfungsi untuk mengubah huruf pertama menjadi huruf besar
print(x.title())
#capitalize() berfungsi untuk mengubah huruf pertama menjadi huruf besar
print(x.capitalize())
#swapcase() berfungsi untuk mengubah huruf besar menjadi huruf kecil dan sebaliknya
print(x.swapcase())
#strip() berfungsi untuk menghapus spasi di awal dan akhir string
print(x.strip())
#rstrip() berfungsi untuk menghapus spasi di akhir string
print(x.rstrip())
#lstrip() berfungsi untuk menghapus spasi di awal string
print(x.lstrip())
#replace() berfungsi untuk mengganti string
print(x.replace("hello", "hi"))
#split() berfungsi untuk memisahkan string
print(x.split(" ")) # ['hello', 'world']
#join() berfungsi untuk menggabungkan string
print(" ".join(["hello", "world"])) # hello world
#find() berfungsi untuk mencari string
print(x.find("world")) # 6
#count() berfungsi untuk menghitung jumlah string
print(x.count("o")) # 2
#startswith() berfungsi untuk mengecek apakah string diawali dengan string tertentu
print(x.startswith("hello")) # True
#endswith() berfungsi untuk mengecek apakah string diakhiri dengan string tertentu
print(x.endswith("world")) # True
#isalpha() berfungsi untuk mengecek apakah string hanya berisi huruf
print(x.isalpha()) # False (karena ada spasi)
#isdigit() berfungsi untuk mengecek apakah string hanya berisi angka
print("123".isdigit()) # True
#isalnum() berfungsi untuk mengecek apakah string hanya berisi huruf dan angka
print("hello123".isalnum()) # True
#isupper() berfungsi untuk mengecek apakah string hanya berisi huruf besar
print(x.isupper()) # False
#islower() berfungsi untuk mengecek apakah string hanya berisi huruf kecil
print(x.islower()) # False
#isspace() berfungsi untuk mengecek apakah string hanya berisi spasi
print("   ".isspace()) # True
#istitle() berfungsi untuk mengecek apakah string dalam format title case
print(x.istitle()) # False (karena "world" tidak diawali huruf besar)
#zfill() berfungsi untuk menambahkan nol di depan string
print("42".zfill(5)) # 00042
#join() berfungsi untuk menggabungkan elemen list menjadi string
list_of_strings = ["hello", "world"]
print(" ".join(list_of_strings)) # hello world
#splitlines() berfungsi untuk memisahkan string berdasarkan baris
multiline_string = "hello\nworld"
print(multiline_string.splitlines()) # ['hello', 'world']
#center() berfungsi untuk meratakan string di tengah dengan padding
print(x.center(20, '-')) # ----hello world-----
#ljust() berfungsi untuk meratakan string ke kiri dengan padding
print(x.ljust(20, '-')) # hello world--------
#rjust() berfungsi untuk meratakan string ke kanan dengan padding
print(x.rjust(20, '-')) # -----------hello world
#partition() berfungsi untuk membagi string menjadi tiga bagian berdasarkan pemisah
print(x.partition(" ")) # ('hello', ' ', 'world')
#strip() berfungsi untuk menghapus karakter tertentu dari awal dan akhir string
print(x.strip("hd")) # ello worl
