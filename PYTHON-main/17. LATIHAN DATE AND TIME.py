import datetime as ds

print('Silahkan masukkan tanggal lahir anda (dd/mm/yyyy): ')
tanggal = int(input('Tanggal\t: '))
bulan = int(input('Bulan\t: '))
tahun = int(input("Tahun\t: "))

tanggal_lahir = ds.date(tahun, bulan, tanggal)
print(f'Tanggal lahir anda adalah: {tanggal_lahir}')
print(f'Hari lahir anda adalah: {tanggal_lahir:%A}')

hari_ini = ds.date.today()
print(f'Hari ini adalah: {hari_ini:%A}, {hari_ini:%d} {hari_ini:%B} {hari_ini:%Y}')

umur = hari_ini - tanggal_lahir
print(f'Umur anda adalah: {umur.days} hari')
umur_tahun = umur.days // 365
umur_bulan = (umur.days % 365)//30
umur_hari = (umur.days %365)%30
print(f'Umur anda adalah: {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari} hari')