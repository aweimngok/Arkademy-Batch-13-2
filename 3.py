#Program by Fadhil Aweim
import re
import random
#Deklarasi Fungsi
def randomize(jumlah):
    bilangan = []
    total = 0
    for i in range (jumlah):
        bilangan.append(random.randrange(1, 10, 2)) # Menambahkan data random yang telah di generate ke variable list (array) bilangan
        total += bilangan[i] #Syntax untuk summing (increassing)
    print ("array : "+ str(bilangan))
    print ("sum : "+ str(total))

#Program Utama    
angka = input ("Masukkan Angka : ")
adaangka=0
cari = re.findall("[0-9]", angka)
for i in cari:
    adaangka+=1
if adaangka>0: #Jika angka maka jalankan fungsi
    randomize(int(angka))
else : #Jika Bukan angka
    print ("Input Bukan Angka")






    
