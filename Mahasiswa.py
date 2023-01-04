# membuat class dengan kata kunci "class"

class Mahasiswa:
    # atribut
    # konstuktor
    def __init__(self, nim, nama, rombel) :
        # variable objek
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    # method
    def lulus(self, nilai):
        if (nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")
    # class mahasiswa memiliki 3 atribut dan 1 fungsi

    def cetak(self):
        print("Nama :", self.nama)
        print("NIM :", self.nim)
        print("Rombel :", self.rombel)


# membuat objek
mahasiswa1 = Mahasiswa("011021", "ahmad", "TI-5")
# mencetak atribut
mahasiswa1.cetak()
mahasiswa1.lulus(95)

# objek ke -2
mahasiswa2 = Mahasiswa("022132","andi", "TI-14")
# mencetak atribut
mahasiswa2.cetak()
mahasiswa2.lulus(85)



# print(help(mahasiswa1))
