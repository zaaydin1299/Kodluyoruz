import pandas as pd

# Verilen sözlük
sozluk = {
    "Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
    "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
    "Fiyat" : [300,180,450,50,700,400,150,80,850,900]
}

# DataFrame'e dönüştürme
df = pd.DataFrame(sozluk)

# 2. indexteki kategori ve ürün bilgisi
kategori_2 = df.loc[2, "Kategori"]
urun_2 = df.loc[2, "Ürün"]

# 4. index ile 9. index arasındaki veriler
veriler_4_9 = df.loc[4:9]

# 1. index ile 6. index arasındaki sadece ürün bilgileri
urunler_1_6 = df.loc[1:6, "Ürün"]

# Kategoriye göre filtreleme
giyim_urunleri = df[df["Kategori"] == "Giyim"]
ayakkabi_urunleri = df[df["Kategori"] == "Ayakkabı"]
aksesuar_urunleri = df[df["Kategori"] == "Aksesuar"]

# Kategori + fiyat filtreleri
giyim_300_fazla = df[(df["Kategori"] == "Giyim") & (df["Fiyat"] > 300)]
ayakkabi_600_az = df[(df["Kategori"] == "Ayakkabı") & (df["Fiyat"] < 600)]
aksesuar_100_fazla = df[(df["Kategori"] == "Aksesuar") & (df["Fiyat"] > 100)]

# Sonuçların yazdırılması
print("2. indexteki Kategori:", kategori_2)
print("2. indexteki Ürün:", urun_2)
print("\n4-9 index arası veriler:\n", veriler_4_9)
print("\n1-6 index arası Ürünler:\n", urunler_1_6)
print("\nGiyim kategorisindeki ürünler:\n", giyim_urunleri)
print("\nAyakkabı kategorisindeki ürünler:\n", ayakkabi_urunleri)
print("\nAksesuar kategorisindeki ürünler:\n", aksesuar_urunleri)
print("\nGiyim kategorisinde fiyatı 300'den fazla olan ürünler:\n", giyim_300_fazla)
print("\nAyakkabı kategorisinde fiyatı 600'den az olan ürünler:\n", ayakkabi_600_az)
print("\nAksesuar kategorisinde fiyatı 100'den fazla olan ürünler:\n", aksesuar_100_fazla)
