class Kamelia:
    def __init__(self):
        self.nama = "Kamelia"          # str
        self.umur = 16                 # int
        self.tinggi = 145            # float
        self.is_lulus = True           # bool
        self.hobi = ["membaca", "memasak"]  # list
        self.nilai = (90, 85, 88)      # tuple
        self.profil = {"jurusan": "PPLG1", "angkatan": 2024}  # dict
        self.keunikan = {"rajin", "cerdas"}  # set
        self.catatan = None            # NoneType

    def tampilkan(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("Tinggi:", self.tinggi)
        print("Lulus:", self.is_lulus)
        print("Hobi:", self.hobi)
        print("Nilai:", self.nilai)
        print("Profil:", self.profil)
        print("Keunikan:", self.keunikan)
        print("Catatan:", self.catatan)

data = Kamelia()
data.tampilkan()
