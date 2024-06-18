def inputKalimat():
    kalimat = input("Masukkan kalimat: ")
    tampilkanKalimat(kalimat)
    statistikKalimat(kalimat)

def tampilkanKalimat(kalimat):
    print(kalimat)

def statistikKalimat(kalimat):
    kalimat = kalimat.lower()
    daftarKata = kalimat.split()
    print("Banyak kata: ", len(daftarKata))
    pengecekanKata(daftarKata)

def pengecekanKata(daftarKata):
    tampunganKata = []

    idKata = 1

    for i in daftarKata:
        ditemukan = False
        for item in tampunganKata:
            if item[0] == i:
                item[1] += 1
                ditemukan = True
                break
        if not ditemukan:
            tampunganKata.append([i, 1, idKata])
            idKata += 1
    
    print("Kata yang muncul: \n")
    print("ID \t Banyak Ditemukan \t Kata")
    for t in tampunganKata:
        print(t[2],"\t",t[1],"\t\t\t",t[0])


inputKalimat()