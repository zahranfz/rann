#a = 10, a adalah variabel yang menyimpan nilai 10
#x = 5, x adalah variabel yang menyimpan nilai 5
#panjang = 1000, panjang adalah variabel yang menyimpan nilai 1000
#lebar = 500, lebar adalah variabel yang menyimpan nilai 500
#simbol , adalah pemisah antara nama variabel dengan nilai variabel
#simbol - adalah pemisah antara nama variabel dengan nilai variabel
#simbol = adalah pemisah antara nama variabel dengan nilai variabel
#simbol _ adalah pemisah antara nama variabel dengan nilai variabel
#simbol : adalah pemisah antara nama variabel dengan nilai variabel
#simbol ; adalah pemisah antara nama variabel dengan nilai variabel

#tipe data: angka satuan (integer), angka desimal (float), string, boolean
data_integer = 10 #tipe data integer
data_float = 10.5 #tipe data float
data_string = "Hello World" #tipe data string
data_boolean = True #tipe data boolean
data_boolean2 = False #tipe data boolean
datalist = [1, 2, 3, 4, 5] #tipe data list
data_tuple = (1, 2, 3, 4, 5) #tipe data tuple
data_dict = {"name": "John", "age": 30} #tipe data dictionary
data_set = {1, 2, 3, 4, 5} #tipe data set

#data integer (satuan)
print("data :", data_integer)
print(", bertipe data :", type(data_integer))
print("- bertipe data :", type(data_integer))

#data float (desimal)
print("data :", data_float)
print(", bertipe data :", type(data_float))
print("- bertipe data :", type(data_float))

#data string (teks)
print("data :", data_string)
print(", bertipe data :", type(data_string))
print("- bertipe data :", type(data_string))

#data boolean (benar/salah)
print("data :", data_boolean)
print(", bertipe data :", type(data_boolean))
print("- bertipe data :", type(data_boolean))
print("data :", data_boolean2)
print(", bertipe data :", type(data_boolean2))
print("- bertipe data :", type(data_boolean2))

#data list (daftar)
print("data :", datalist)
print(", bertipe data :", type(datalist))
print("- bertipe data :", type(datalist))

#data tuple (kumpulan data yang tidak bisa diubah)
print("data :", data_tuple)
print(", bertipe data :", type(data_tuple))
print("- bertipe data :", type(data_tuple))

#data dictionary (kumpulan data yang bisa diubah)
print("data :", data_dict)
print(", bertipe data :", type(data_dict))
print("- bertipe data :", type(data_dict))

#data set (kumpulan data yang tidak bisa diubah dan tidak bisa diulang)
print("data :", data_set)
print(", bertipe data :", type(data_set))
print("- bertipe data :", type(data_set))

#tipe data khusus
#data complex (bilangan kompleks)
data_complex = 1 + 2j #tipe data complex
data_complex2 = complex(1, 2) #tipe data complex
print("data :", data_complex)
print(", bertipe data :", type(data_complex))
print("- bertipe data :", type(data_complex))

print("data :", data_complex2)
print(", bertipe data :", type(data_complex2))
print("- bertipe data :", type(data_complex2))

#tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5) #tipe data c_double
print("data :", data_c_double)
print(", bertipe data :", type(data_c_double))
print("- bertipe data :", type(data_c_double))

int = 3
print("data :", int)
print(", bertipe data :", type(int))
print("- bertipe data :", type(int))

a = [1, 2, 3, 4, 5]
print("data :", a, end ='')
print(", bertipe data :", type(a))

x = 5
y = 10
function = x**3 + y/2 - 5*x + 3*y - 7
print("data :", function, end ='')
print(", bertipe data :", type(function))

if function > 129:
    print("data :", function, end ='')
    print(", bertipe data :", type(function))
else:
    print("data tidak ditemukan")

while function > 122:
    print("data :", function, end ='')
    print(", bertipe data :", type(function))
    break
else:
    print("data tidak ditemukan")

int = 3
float = 3.5
function = int + float
print("data :", function, end ='')
print(", bertipe data :", type(function))

combine = 3 + 4j
print("data :", combine, end ='')
print(", bertipe data :", type(combine))

imaginary = 4j
int = 3
function = imaginary + int
print("data :", function, end ='')
print(", bertipe data :", type(function))

x = 80
y =651
function = (x/y)
print("data :", function, end ='')
print(", bertipe data :", type(function))