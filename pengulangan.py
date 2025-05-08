# While loop untuk meminta input dari user
while True:
    try:
        # Input tinggi segitiga
        tinggi = int(input("Masukkan tinggi segitiga (angka positif): "))
        if tinggi <= 0:
            print("Tinggi harus lebih besar dari 0!")
        else:
            break  # Keluar dari loop jika input valid
    except ValueError:
        print("Harap masukkan angka yang valid.")

# For loop untuk menampilkan pola segitiga bintang
print("\nPola Segitiga Bintang:")
for i in range(1, tinggi + 1):  # Loop baris
    for j in range(i):  # Loop kolom untuk bintang
        print("*", end="")
    print()  # Pindah ke baris baru

# Nested loop untuk menampilkan tabel perkalian
print("\nTabel Perkalian:")
for i in range(1, 6):  # Loop untuk angka pertama
    for j in range(1, 6):  # Loop untuk angka kedua
        print(f"{i} * {j} = {i * j}", end="\t")  # Menampilkan hasil perkalian
    print()  # Pindah ke baris berikutnya
