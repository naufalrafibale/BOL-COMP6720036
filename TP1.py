import json

json_data = [
 {
   "No": 1,
   "JenisKelamin": "Laki-Laki",
   "UmurKaryawan": 20,
   "Gaji": 8000000,
   "Transportasi": "Kendaraan Pribadi"
 },
 {
   "No": 2,
   "JenisKelamin": "Laki-Laki",
   "UmurKaryawan": 35,
   "Gaji": 14000000,
   "Transportasi": "Kendaraan Umum"
 },
 {
   "No": 3,
   "JenisKelamin": "Perempuan",
   "UmurKaryawan": 26,
   "Gaji": 10000000,
   "Transportasi": "Kendaraan Umum"
 },
 {
   "No": 4,
   "JenisKelamin": "Perempuan",
   "UmurKaryawan": 27,
   "Gaji": 12000000,
   "Transportasi": "Kendaraan Pribadi"
 },
 {
   "No": 5,
   "JenisKelamin": "Laki-Laki",
   "UmurKaryawan": 21,
   "Gaji": 9000000,
   "Transportasi": "Kendaraan Pribadi"
 },
 {
   "No": 6,
   "JenisKelamin": "Laki-Laki",
   "UmurKaryawan": 22,
   "Gaji": 11000000,
   "Transportasi": "Kendaraan Pribadi"
 },
 {
   "No": 7,
   "JenisKelamin": "Perempuan",
   "UmurKaryawan": 32,
   "Gaji": 15000000,
   "Transportasi": "Kendaraan Umum"
 },
 {
   "No": 8,
   "JenisKelamin": "Perempuan",
   "UmurKaryawan": 26,
   "Gaji": 8000000,
   "Transportasi": "Kendaraan Umum"
 },
 {
   "No": 9,
   "JenisKelamin": "Laki-Laki",
   "UmurKaryawan": 25,
   "Gaji": 9000000,
   "Transportasi": "Kendaraan Umum"
 },
 {
   "No": 10,
   "JenisKelamin": "Perempuan",
   "UmurKaryawan": 20,
   "Gaji": 10000000,
   "Transportasi": "Kendaraan Pribadi"
 }
]

for data in json_data:
    if data["Gaji"] >= 8000000 and data["Gaji"] < 10000000:
        data["Jabatan"] = "Officer"
    elif data["Gaji"] >= 10000000 and data["Gaji"] < 12000000:
        data["Jabatan"] = "Supervisor"
    elif data["Gaji"] >= 12000000 and data["Gaji"] < 15000000:
        data["Jabatan"] = "Asisten Manajer"
    elif data["Gaji"] >= 15000000:
        data["Jabatan"] = "Manager"
    else:
        data["Jabatan"] = None

gaji = []
for data in json_data:
    gaji.append(data["Gaji"])
sorted_gaji = sorted(gaji, reverse=True)
print("Array list gaji dari terbesar hingga terkecil:", sorted_gaji)
print("Gaji terbesar:", sorted_gaji[0])
print("Gaji terkecil:", sorted_gaji[-1])

json_formatted = json.dumps(json_data, indent=2)
print(json_formatted)