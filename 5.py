#program by Fadhil Aweim
#fungsi=============================
def ganti_kata(kataa,carii,gantii):
    panjang = len(kataa)
    karakter=[] # variable list atau array
    katabaru="" # deklarasi dalam bentuk String
    for i in range(panjang):
        karakter.append(kataa[i])
        if karakter[i] == carii:
            karakter[i] = gantii
        katabaru=katabaru+karakter[i]
    print (katabaru)    
    
    
#program utama=============================    
kata = input("Masukkan Kata/Kalimat: ")
cari = input("Huruf yang dicari: ")
ganti = input("Huruf pengganti: ")
ganti_kata(kata,cari,ganti)
