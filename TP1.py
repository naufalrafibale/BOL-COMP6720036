import pandas as pd
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

df = pd.DataFrame(json_data)

def assign_jabatan(row):
  if row >= 8000000 and row < 10000000:
      jabatan = "Officer"
  elif row >= 10000000 and row < 12000000:
      jabatan = "Supervisor"
  elif row >= 12000000 and row < 15000000:
      jabatan = "Asisten Manajer"
  elif row >= 15000000:
      jabatan = "Manager"
  else:
      jabatan = None
  return jabatan

df['Jabatan'] = df['Gaji'].apply(assign_jabatan)
print(df)

print(df['Gaji'].sort_values(ascending=False))
print("Gaji terbesar:", df['Gaji'].max())
print("Gaji terkecil:", df['Gaji'].min())