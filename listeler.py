<<<<<<< HEAD
def liste_islemleri():
    liste = []  # Boş bir liste oluştur
    islem_gecmisi = []  # İşlem geçmişi listesi

    while True:
        # Kullanıcıya seçenekleri göster
        print("\nMevcut liste:", liste)
        print("1. Eleman ekle")
        print("2. Eleman çıkar")
        print("3. Tüm listeyi sil")
        print("4. Listeyi ayır (belirli bir elemana kadar)")
        print("5. Çıkış")
        secim = input("Lütfen bir seçenek girin (1/2/3/4/5): ")

        if secim == "1":
            # Eleman ekleme
            eleman = input("Eklemek istediğiniz elemanı girin: ")
            liste.append(eleman)
            islem_gecmisi.append(f"'{eleman}' listeye eklendi.")
            print(f"'{eleman}' listeye eklendi.")
        elif secim == "2":
            # Eleman çıkarma
            if not liste:
                print("Liste boş, çıkarılacak eleman yok.")
            else:
                eleman = input("Çıkarmak istediğiniz elemanı girin: ")
                if eleman in liste:
                    liste.remove(eleman)
                    islem_gecmisi.append(f"'{eleman}' listeden çıkarıldı.")
                    print(f"'{eleman}' listeden çıkarıldı.")
                else:
                    print(f"'{eleman}' listede bulunamadı.")
        elif secim == "3":
            # Tüm listeyi silme
            if not liste:
                print("Liste zaten boş.")
            else:
                liste.clear()
                islem_gecmisi.append("Tüm liste silindi.")
                print("Tüm liste silindi.")
        elif secim == "4":
            # Listeyi ayırma (belirli bir elemana kadar)
            if not liste:
                print("Liste boş, ayıracak eleman yok.")
            else:
                eleman = input("Listeyi hangi elemana kadar ayırmak istersiniz? ")
                if eleman in liste:
                    indeks = liste.index(eleman)
                    yeni_liste = liste[:indeks + 1]  # Elemana kadar olan kısmı al
                    islem_gecmisi.append(f"Ayrılan liste: {yeni_liste}")
                    print(f"Ayrılan liste: {yeni_liste}")
                else:
                    print(f"'{eleman}' listede bulunamadı.")
        elif secim == "5":
            # Programdan çık
            print("\nProgramdan çıkılıyor...")
            print("\nYapılan işlemler:")
            for islem in islem_gecmisi:
                print("-", islem)
            break
        else:
            # Geçersiz seçenek
            print("Geçersiz seçenek! Lütfen 1, 2, 3, 4 veya 5 girin.")

# Programı başlat
liste_islemleri()
=======
def liste_islemleri():
    liste = []  # Boş bir liste oluştur
    islem_gecmisi = []  # İşlem geçmişi listesi

    while True:
        # Kullanıcıya seçenekleri göster
        print("\nMevcut liste:", liste)
        print("1. Eleman ekle")
        print("2. Eleman çıkar")
        print("3. Tüm listeyi sil")
        print("4. Listeyi ayır (belirli bir elemana kadar)")
        print("5. Çıkış")
        secim = input("Lütfen bir seçenek girin (1/2/3/4/5): ")

        if secim == "1":
            # Eleman ekleme
            eleman = input("Eklemek istediğiniz elemanı girin: ")
            liste.append(eleman)
            islem_gecmisi.append(f"'{eleman}' listeye eklendi.")
            print(f"'{eleman}' listeye eklendi.")
        elif secim == "2":
            # Eleman çıkarma
            if not liste:
                print("Liste boş, çıkarılacak eleman yok.")
            else:
                eleman = input("Çıkarmak istediğiniz elemanı girin: ")
                if eleman in liste:
                    liste.remove(eleman)
                    islem_gecmisi.append(f"'{eleman}' listeden çıkarıldı.")
                    print(f"'{eleman}' listeden çıkarıldı.")
                else:
                    print(f"'{eleman}' listede bulunamadı.")
        elif secim == "3":
            # Tüm listeyi silme
            if not liste:
                print("Liste zaten boş.")
            else:
                liste.clear()
                islem_gecmisi.append("Tüm liste silindi.")
                print("Tüm liste silindi.")
        elif secim == "4":
            # Listeyi ayırma (belirli bir elemana kadar)
            if not liste:
                print("Liste boş, ayıracak eleman yok.")
            else:
                eleman = input("Listeyi hangi elemana kadar ayırmak istersiniz? ")
                if eleman in liste:
                    indeks = liste.index(eleman)
                    yeni_liste = liste[:indeks + 1]  # Elemana kadar olan kısmı al
                    islem_gecmisi.append(f"Ayrılan liste: {yeni_liste}")
                    print(f"Ayrılan liste: {yeni_liste}")
                else:
                    print(f"'{eleman}' listede bulunamadı.")
        elif secim == "5":
            # Programdan çık
            print("\nProgramdan çıkılıyor...")
            print("\nYapılan işlemler:")
            for islem in islem_gecmisi:
                print("-", islem)
            break
        else:
            # Geçersiz seçenek
            print("Geçersiz seçenek! Lütfen 1, 2, 3, 4 veya 5 girin.")

# Programı başlat
liste_islemleri()
>>>>>>> cbd9ac08f4d5415da78adb57da2caeff49eee7d0
