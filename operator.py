# Program: Operasi Aritmatika Dasar
# Tema: Menghitung uang jajan mingguan Kamelia

# Uang jajan per hari
uang_jajan_per_hari = 15000  # rupiah

# Jumlah hari masuk sekolah dalam seminggu
hari_sekolah = 5

# Total uang jajan selama 1 minggu (perkalian)
total_uang_jajan = uang_jajan_per_hari * hari_sekolah

# Tambahan uang dari orang tua pada hari Jumat (penjumlahan)
bonus_jumat = 10000
total_uang_dengan_bonus = total_uang_jajan + bonus_jumat

# Kamelia membeli alat tulis (pengurangan)
pengeluaran = 25000
sisa_uang = total_uang_dengan_bonus - pengeluaran

# Kamelia ingin membagi sisa uang ke 2 tabungan (pembagian)
tabungan_per_kotak = sisa_uang / 2

# Menampilkan hasil
print("=== Laporan Uang Jajan Kamelia ===")
print("Uang jajan per hari       :", uang_jajan_per_hari)
print("Hari sekolah              :", hari_sekolah)
print("Total uang jajan          :", total_uang_jajan)
print("Bonus hari Jumat          :", bonus_jumat)
print("Total uang + bonus        :", total_uang_dengan_bonus)
print("Pengeluaran alat tulis    :", pengeluaran)
print("Sisa uang setelah belanja :", sisa_uang)
print("Tabungan per kotak        :", tabungan_per_kotak)

"""
Komentar multi-baris:
Program ini menunjukkan penggunaan 4 operator aritmatika dasar:
- * (perkalian)
- + (penjumlahan)
- - (pengurangan)
- / (pembagian)
Dengan studi kasus bertema manajemen uang jajan Kamelia selama 1 minggu.
"""
