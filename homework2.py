# Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;
#10000 ve altındaysa maaşından %5 kesinti olur.25000 ve altındaysa maaşından %10 kesinti olur.45000 ve altındaysa maaşından %25 kesinti olur.Diğer koşullarda %30 kesinti olur.

print("Vergi Hesaplama Uygulamasına hoş geldiniz!")
print("Loadining...") 

maas = float(input("Vergi tutarınızı hesaplayabilmek için maaşınızı giriniz: "))
 
# Vergi kesintisini hesapla
if maas <= 10000:
    vergi_orani = 0.05
elif maas <= 25000:
    vergi_orani = 0.10
elif maas <= 45000:
    vergi_orani = 0.25
else:
    vergi_orani = 0.30

# Vergi miktarını hesapla
vergi_kesintisi = maas * vergi_orani
net_maas = maas - vergi_kesintisi

# Sonuçları ekrana yazdır
print(f"\nMaaşınız: {maas} TL")
print(f"Vergi Kesintisi Oranı: %{vergi_orani * 100}")
print(f"Vergi Kesintisi Miktarı: {vergi_kesintisi} TL")
print(f"Net Maaşınız: {net_maas} TL")


#Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir.
# Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, 
# altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır.

print("Şifre Oluşturma uygulamasına hoş geldiniz!")
print("Yükleniyor...")

kullanici_ad = input("Kullanıcı Adınızı Giriniz: ")

while True:
    sifre = input("Şifrenizi Girin (6 haneli olmalıdır): ")

    if len(sifre) == 6:
        print("Hesabınız başarıyla oluşturuldu.")
        break  # Şifre doğru girildi, döngüden çık
    elif len(sifre) < 6:
        print("Hata: Şifre 6 haneli olmalıdır.")
    else:
        print("Hata: Şifre 6 haneden fazla olamaz.")

    # Kullanıcıya devam edip etmeyeceğini sor
    devam = input("Yeni bir şifre girmek istiyor musunuz? (Evet/Hayır): ").strip().lower()
    if devam == "hayır":
        print("Oyundan çıkılıyor...")
        break  # Döngüden çıkar ve program sonlanır
    elif devam != "evet":
        print("Geçersiz seçenek! Lütfen 'Evet' veya 'Hayır' girin.")
        continue  # Döngüyü yeniden başlat

# Kullanıcı bilgilerini yazdır
print("\nKullanıcı Bilgileri:")
print(f"Kullanıcı Adı: {kullanici_ad}")
print(f"Şifre: {sifre}") 

#Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda.
#Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır.
#Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.
#Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder

print("Şifre Oluşturma Uygulamasına Hoş Geldiniz!")
print("Yükleniyor...")

kullanici_ad = input("Kullanıcı Adınızı Giriniz: ")

while True:
    sifre = input("Şifrenizi Girin (5-10 hane arasında olmalıdır): ")

    if 5 <= len(sifre) <= 10:
        print("Hesabınız başarıyla oluşturuldu.")
        break  # Şifre doğru girildi, döngüden çık
    else:
        print("Hata: Lütfen girdiğiniz şifre 5 haneden az veya 10 haneden fazla olmasın!")

# Kullanıcı bilgilerini yazdır
print("\nKullanıcı Bilgileri:")
print(f"Kullanıcı Adı: {kullanici_ad}")
print(f"Şifre: {sifre}") 

#Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
#Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar.
#Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter.
#Tercihe göre kalan hak bilgisi verilir.

print("Giriş Ekranına hoş geldiiz! ")
print("Yükleniyor...") 

Kullancici_isim = "zapepeyz0"
password = "V2r1_B1l1m1"

deneme_hakki = 3

while True:
    
    girilen_kullanici_isim = input("Kullanıcı Adınızı Giriniz: ")

    # Kullanıcı adı kontrolü
    if girilen_kullanici_isim != Kullancici_isim:
        print("Hata: Kullanıcı adı bulunamadı! Lütfen tekrar deneyin.")
        continue  


    while deneme_hakki > 0:
        girilen_sifre = input("Lütfen Şifrenizi Giriniz: ") 


        if girilen_sifre == password and girilen_kullanici_isim == Kullancici_isim: 
            print("Uygulamanıza giriş yapıldı. ")
            break 

        else:
            deneme_hakki -= 1

            if deneme_hakki > 0:
                print(f"Yanlış şifre lütfen tekrar deneyiz. Kalan deneme hakkınız: {deneme_hakki}")

            else:
                print("Yanlış şifre girildi. Deneme hakkınız sonlandı. Program kapatılıyor... ")

