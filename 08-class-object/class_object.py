class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        print("Nama saya", self.nama, "dari kelas", self.kelas)

s1 = Siswa("Radif", "XI RPL")
s1.perkenalan()
