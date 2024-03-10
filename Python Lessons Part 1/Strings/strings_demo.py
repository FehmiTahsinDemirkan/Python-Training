website = "www.google.com"
kursAdi = "Python Deneme Dersleri : Sıfırdan İleri seviyeye"
name = "Fehmi"
surname = "Demirkan"
Age = 21
Job = "Engineer"
# 1.soru
kursAdiKarakterSayisi = len(kursAdi)
sonuc = len(website)
print(kursAdiKarakterSayisi)
# 2.soru
sonuc = website[7:10]
print(sonuc)
# 3.soru
kursAdiKarakterSayisi = len(website)
sonuc = website[kursAdiKarakterSayisi-3:kursAdiKarakterSayisi]

# 4.soru
print(kursAdi[0:15])
print(kursAdi[15:48])
# 5.soru
sonuc = kursAdi[::-1]
print(sonuc)

# 6.soru
s = "hello world"
s = s[0:6] + "W" + s[-4:]
print(s)

# 7.Soru
print("abc" * 3)
# 8.soru
print(f"Benim adım {name},soyadım {surname}. {Age} yaşındayım ve {Job} olarak çalışmaktayım.")