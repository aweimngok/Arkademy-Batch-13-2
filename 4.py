#Program by Fadhil Aweim
def findSame(kata): #membuat fungsi findSame
    panjang=[] #membuat variable list panjang
    banyakdata=0
    adasama =0
    for i in kata: #fungsi perulangan sebanyak data yang ada pada variable list kata
        panjang.append(len(kata[banyakdata])) #menyimpan masing2 panjang karakter dari masing2 data pada variable list kata
        banyakdata+=1
    #print (panjang)
    indeks = banyakdata-1
        
    for a in range (indeks):
        for b in range (indeks-a):
            #print (str(a)+str(b+1))
            if panjang[a]==panjang[(b+1)*-1]: # memeriksa apakah ada data yang jumlah karakternya sama
                adasama+=1
    if adasama>0:
        print ("ada")
    else :
        print ("enggak")
            

findSame(["mangga","apel","jambu"])
