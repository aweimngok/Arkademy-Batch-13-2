import re
import random
def randomize(jumlah):
    bilangan = []
    total = 0
    for i in range (jumlah):
        bilangan.append(random.randrange(1, 10, 2))
        total += bilangan[i]
    print ("array : "+ str(bilangan))
    print ("sum : "+ str(total))
    
angka = input ("Masukkan Angka : ")
adaangka=0
cari = re.findall("[0-9]", angka)
for i in cari:
    adaangka+=1
if adaangka>0:
    randomize(int(angka))
else :
    print ("Input Bukan Angka")






    
