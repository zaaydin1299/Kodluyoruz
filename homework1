# Ödev-1: Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.

a = "21"
b = 20.5
c = True

# String'den int'e dönüşüm
a_int = int(a)  # 10

# Float'tan int'e dönüşüm
b_int = int(b)  # 20

# Boolean'dan string'e dönüşüm
c_str = str(c)  # "True" 

print(a)
print(b)
print(c)

print(type(a_int))
print(type(b_int))
print(type(c_str))

#Ödev-2: İsimlerden Oluşan Üç Değişkene Yaş Değerleri Atanması, Karşılaştırılması ve Operatörler Kullanımı

# İsimlere yaş atama
ali_yas = 25
ayse_yas = 30
mehmet_yas = 22

# Karşılaştırmalar
ali_ayse_ayni_yas = (ali_yas == ayse_yas)  # False
ali_mehmetten_buyuk = (ali_yas > mehmet_yas)  # True
ayse_mehmetten_kucuk = (ayse_yas < mehmet_yas)  # False

# Mantıksal operatörlerle
ali_en_buyuk = (ali_yas > ayse_yas) and (ali_yas > mehmet_yas)  # False 
print(ali_ayse_ayni_yas )
print(ali_mehmetten_buyuk)
print(ayse_mehmetten_kucuk)
print(ali_en_buyuk)

#Ödev-3: Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.
print("The game is Loading...")
print("4 işlem oyununa hoş geldin!")

while True:
    print("Hangi işlemi yapmak istersin? Toplama = 1, Çarpma = 2, Bölme = 3, Çıkarma = 4, Çıkış = 0")

    operation = int(input("İşlem numarasını giriniz: "))

    if operation == 0:
        print("Oyundan çıkılıyor...")
        break  # Döngüden çıkar ve oyun biter.
    elif operation not in [1, 2, 3, 4]:
        print("Hatalı girdiniz! Lütfen geçerli bir işlem numarası girin.")
        continue  # Geç ve işleme aynı soru sorulsun.

    first_number = int(input("İlk değeri giriniz: "))
    second_number = int(input("İkinci değeri giriniz: "))

    if operation == 1:
        result = first_number + second_number
        print(f"Toplama işleminin sonucu: {result}")
    elif operation == 2:
        result = first_number * second_number
        print(f"Çarpma işleminin sonucu: {result}")
    elif operation == 3:
        if second_number != 0:
            result = first_number / second_number
            print(f"Bölme işleminin sonucu: {result}")
        else:
            print("Hata: Sıfıra bölme hatası!")
    elif operation == 4:
        result = first_number - second_number
        print(f"Çıkarma işleminin sonucu: {result}")

    # Devam edip etmeyeceğini sor. Eğer ki cevabu evetse döngü devam eder hayırsa döngü biter.
    devam = input("Oyuna devam etmek istiyor musunuz? (Evet/Hayır): ").strip().lower()
    if devam == "hayır":
        print("Oyundan çıkılıyor...")
        break  # Dögüden çıkar ve oyun biter.
    elif devam != "evet":
        print("Oyuna devam edilir. ")
        continue

# Ödev-4: Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.
# Kullanıcıdan bilgileri al
isim = input("İsminizi giriniz: ")
yas = input("Yaşınızı giriniz: ")
sehir = input("Şehirinizi giriniz: ")
meslek = input("Mesleğinizi giriniz: ")

# Bilgileri ekrana yazdır
print("\nKullanıcı Bilgileri:")
print(f"İsim: {isim}")
print(f"Yaş: {yas}")
print(f"Şehir: {sehir}")
print(f"Meslek: {meslek}")

#Ödev-5: "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.

# "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımla
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# İfadedeki her bir kelimeyi seç
kelimeler = ifade.split()  # split() metodu ile kelimeleri ayır
print("Kelimeler:", kelimeler)

# İfadeyi hepsini büyük harf olacak hale çevir
buyuk_harf = ifade.upper()
print("Büyük Harf:", buyuk_harf)

# İfadeyi hepsini küçük harf olacak hale çevir
kucuk_harf = ifade.lower()
print("Küçük Harf:", kucuk_harf)  


