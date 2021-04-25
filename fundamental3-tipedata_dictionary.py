#TIPE DATA DICTIONARY SEKEDAR MENGHUBUNGKAN KEY DAN VALUE
# KVP : KEY VALUE PAIR
#DICTIONARY : KAMUS

kamus = {'anak': 'son', 'ayah': 'father', 'ibu': 'mother', 'istri': 'wife'}

print(kamus)
print(kamus['anak'])

print('data ini dikirimkan dari server Gojek, untuk memberikan info driver terdekat')
data_dari_server_gojek = {
    'tanggal': '2021-4-25',
    'driver_list': [
        {'nama': 'eko', 'jarak': 10},
        {'nama': 'dwi', 'jarak' : 20},
        {'nama': 'tri', 'jarak': 30},
        {'nama': 'catur', 'jarak': 40}
    ]
}
print(f"driver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"driver #2 {data_dari_server_gojek['driver_list'][3]}")
print(f"Jarak driver terdekat {data_dari_server_gojek['driver_list'][0]['jarak']} Meter")