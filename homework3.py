"""#Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

import time  # Uygulamanın yüklenmesini ve kapanmasını daha çekici hale getirilmesi

print("\nDairenin Alanını Hesaplayan Programa Hoş Geldin!!\n")
print("Uygulama Yükleniyor...\n")
time.sleep(1)  # 1 saniye bekleyerek sanki uygulama yükleniyormuşçasına his verir.

def dairenin_alani(pi,yari_cap):
    alan = pi * (yari_cap ** 2) #Alan = pi * rüzeri2
    return alan 

# Kullanıcıdan pi ve yarıçap değerlerini al
pi_degeri = input("Pi değerini girin (Örneğin 3.14):")
yaricap_degeri = input("Dairenin yarıçapını girin: ") 

# Virgülleri noktaya çevir ve float'a dönüştür
pi_degeri = float(pi_degeri.replace(",", "."))
yaricap_degeri = float(yaricap_degeri.replace(",", "."))

# Fonksiyonu çağır ve sonucu yazdır
alan = dairenin_alani(pi_degeri, yaricap_degeri)
print("\nDairenin Alanı:", round(alan, 3), "\n")  # Boşluk bırakılarak temiz görüntü sağlanır.

print("Uygulama Kapatılıyor...\n")
time.sleep(1)  # Kapanma efekti için 1 saniye bekle ve kapan.
"""
"""
#Faktöriyel adında fonksiyon oluşturulur. 
#Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. 
#Format metodunu kullanılarak ekrana yazdırılır.

import time

# Uygulama başlangıç mesajı verilir.
print("\nFaktöriyel Hesaplama Programına Hoş Geldiniz!\n")
print("Uygulama Yükleniyor...\n")
time.sleep(1)  # Efekt için bekleme süresi

def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

while True:
    try:
        # Kullanıcıdan sayı girişi al
        sayi = int(input("Lütfen bir sayı girin: "))

        # Negatif sayı kontrolü
        if sayi < 0:
            print("\nHata: Negatif sayıların faktöriyeli hesaplanamaz!\n")
            option = input("Devam etmek ister misiniz? (evet/hayır): ").strip().lower()

            if option == "hayır":
                print("\nUygulama Kapatılıyor...\n")
                time.sleep(1)
                break  # Programdan çık
            elif option != "evet":
                print("\nGeçersiz giriş! Lütfen 'evet' veya 'hayır' yazın.\n")
                continue  # Geçersiz giriş durumunda döngüyü tekrar başlat
            # "evet" durumunda döngü devam eder ve yeni bir sayı ister
        else:
            # Faktöriyel hesapla
            sonuc = faktoriyel(sayi)

            # Formatlı çıktı
            print("\n{}! = {:,}".format(sayi, sonuc))  # {:,} sayıyı binlik ayraç ile gösterir

            # Başka bir işlem yapılıp yapılmayacağını sor
            devam = input("\nBaşka bir sayı hesaplamak ister misiniz? (evet/hayır): ").strip().lower()
            if devam == "hayır":
                print("\nUygulama Kapatılıyor...\n")
                time.sleep(1)
                break  # Programdan çık
            elif devam != "evet":
                print("\nGeçersiz giriş! Program sonlandırılıyor...\n")
                time.sleep(1)
                break  # Geçersiz giriş durumunda programdan çık

    except ValueError:
        print("\nHata: Lütfen geçerli bir tam sayı girin!\n")

# Uygulama kapanış mesajı
print("\nUygulama Kapatıldı.\n")
"""
"""
import time
from datetime import datetime

# Uygulama başlangıç mesajı
print("\nYaş Hesaplama Programına Hoş Geldiniz!\n")
print("Uygulama Yükleniyor...\n")
time.sleep(1)  

def yas_hesapla(dogum_yili, dogum_ayi, dogum_gunu):
    mevcut_tarih = datetime.now()
    mevcut_yil, mevcut_ay, mevcut_gun = mevcut_tarih.year, mevcut_tarih.month, mevcut_tarih.day

    yas = mevcut_yil - dogum_yili

    # Doğum günü henüz geçmediyse yaşı bir azalt
    if (dogum_ayi, dogum_gunu) > (mevcut_ay, mevcut_gun):
        yas -= 1
    return yas

while True:
    try:
        # Kullanıcıdan doğum tarihi bilgilerini al
        dogum_yili = int(input("Doğduğunuz yılı giriniz: "))
        dogum_ayi = int(input("Doğduğunuz ayı (1-12 arasında) giriniz: "))
        dogum_gunu = int(input("Doğduğunuz günü (1-31 arasında) giriniz: "))

        mevcut_yil = datetime.now().year

        # Geçersiz girişleri kontrol et
        if dogum_yili > mevcut_yil:
            print("\nHata: Gelecek bir yıl girdiniz! Lütfen geçerli bir doğum yılı girin.\n")
            continue
        elif dogum_yili < 1900:
            print("\nHata: 1900 yılından küçük bir tarih girdiniz. Lütfen geçerli bir yıl giriniz.\n")
            continue
        elif not (1 <= dogum_ayi <= 12):
            print("\nHata: Ay değeri 1 ile 12 arasında olmalıdır!\n")
            continue
        elif not (1 <= dogum_gunu <= 31):
            print("\nHata: Gün değeri 1 ile 31 arasında olmalıdır!\n")
            continue

        # Yaşı hesapla ve ekrana yazdır
        yas = yas_hesapla(dogum_yili, dogum_ayi, dogum_gunu)
        print(f"\n{dogum_yili}-{dogum_ayi}-{dogum_gunu} doğumluysanız yaklaşık {yas} yaşındasınız.\n")
        break  # Başarıyla hesaplandıysa döngüden çık

    except ValueError:
        print("\nHata: Lütfen geçerli bir sayı girin! (Örneğin: 2008, 5, 21)\n")

# Uygulama kapanış mesajı
print("\nUygulama Kapatılıyor...\n")
time.sleep(1)  # Efekt için bekleme süresi
print("Uygulama Kapandı.")
"""
#Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.(Kişi 65 yaşında ise emekli olur.)
#Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) 
#Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 
# 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.

import time
from datetime import datetime

print("\nEmeklilik Hesaplama Programına Hoş Geldiniz!\n")
print("Uygulama Yükleniyor...\n")
time.sleep(1)  # Efekt için bekleme süresi

# Yaş hesaplama fonksiyonu
def yas_hesapla(doğum_yili):
    mevcut_yil = datetime.now().year
    if doğum_yili > mevcut_yil:
        raise ValueError("Doğum yılı gelecekten bir yıl olamaz.")
    yas = mevcut_yil - dogum_yili
    return yas

# Emeklilik hesaplama fonksiyonu
def emeklilik_hesapla(isim, dogum_yili):
    try:
        yas = yas_hesapla(dogum_yili)  # İç içe fonksiyon kullanımı
        emeklilik_yasi = 65
        
        if yas >= emeklilik_yasi:
            print(f"\nTebrikler {isim}, emekli oldunuz! 🎉")
        else:
            kalan_yil = emeklilik_yasi - yas
            print(f"\n{isim}, emekliliğinize {kalan_yil} yıl kaldı. Sabret! 😊")
    except ValueError as e:
        print(f"\nHata: {e}")

# Ana program
try:
    isim = input("Adınızı giriniz: ")
    dogum_yili = int(input("Doğum yılınızı giriniz: "))
    
    # Emeklilik hesaplama fonksiyonunu çağırma işlemi
    emeklilik_hesapla(isim, dogum_yili)
except ValueError:
    print("\nHata: Geçerli bir yıl giriniz! (Örneğin: 1990)")

# Uygulama kapanış mesajı
print("\nUygulama Kapatılıyor...\n")
time.sleep(1)
print("Uygulama Kapandı.")