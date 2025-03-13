#Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.
#liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
#"3" değerine ulaşmak için indexleme yapın.
#"Hi-Kod" değerine ulaşmak için indexleme yapın.
#4.7 değerine ulaşmak için indexleme yapın.
#9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.
#8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.
import time
print("\nListedi Elemanını Bulan Programa Hoş Geldin!!\n")
print("Uygulama Yükleniyor...\n")
time.sleep(1)  # 1 saniye bekleyerek sanki uygulama yükleniyormuşçasına his verir.

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

print(liste[3])
print(liste[5])
print(liste[7])
print(liste[2:6])
print(liste[4:])

print("\nUygulama Kapatılıyor...\n")
time.sleep(1)
print("Uygulama Kapandı.")

# Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

import time
print("\nListedi Elemanının Stringini Bulan Programa Hoş Geldin!!\n")
print("Uygulama Yükleniyor...\n")
time.sleep(1)

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
new_list = []

for eleman in liste:
    if isinstance(eleman, str):  # eleman str mi? evet ise eleman yeni listeye ekenir
        new_list.append(eleman)

print(new_list)

print("\nUygulama Kapatılıyor...\n")
time.sleep(1)
print("Uygulama Kapandı.")

#Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.
#for index in range(len(meyveler)):
#print("{}. indexte bulunan meyve: {}".format(index,meyveler[index])

import time

print("\nBir Elemanın kaçıncı sırada Olduğunu Bulan Programa Hoş Geldiniz!!\n")
print("Uygulama Yükleniyor...\n")
time.sleep(1)

meyveler = ["elma", "armut", "muz", "çilek"]

for indeks, meyve in enumerate(meyveler):
    print(f"{indeks}. indeksteki meyve: {meyve}")

