nilai = int(input("Masukkan nilai Anda (0-100): "))

if nilai >= 85:
    print("Kategori: Sangat Baik")
elif nilai >= 70:
    print("Kategori: Baik")
elif nilai >= 55:
    print("Kategori: Cukup")
else:
    print("Kategori: Kurang")
