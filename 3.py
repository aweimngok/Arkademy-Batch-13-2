import random
def randomize(jumlah):
    bilangan = []
    total = 0
    for i in range (jumlah):
        bilangan.append(random.randrange(1, 10, 2))
        total += bilangan[i]
    print ("array : "+ str(bilangan))
    print ("sum : "+ str(total))
    
angka = int(input ("Masukkan Angka : "))
randomize(angka)    
