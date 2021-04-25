#TIPE DATA SEDERHANA
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'tri'
anak4 = 'catur'
print(anak2)


#TIPE DATA DAFTAR / ARRAY / LIST

nama_anak = ['eko', 'dwi', 'tri', 'catur'] #membuat data array
nama_anak.append('five') #menambahkan data pada array yg telah dibuat

#cetak nama anak satuan
print(f'hai {nama_anak[1]}')

#cetak nama semua anak dengan for
for index_nama in nama_anak:
    print(f'hai {index_nama}')

#cetak nama semua anak dengan for in range
for a in range(0, len(nama_anak)):
    print(f'{a+1}. Hai {nama_anak[a]}')

