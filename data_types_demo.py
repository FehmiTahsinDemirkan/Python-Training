# Yarı çapı verilen bir dairenin alan ve çevresini hesapla
# Daire Alanı : pi*r*r
# Daire Çevre : 2*pi*r
pi = 3.14
x = float(input("Lütfen bir yari çap Giriniz"))
alan = pi * (x ** 2)
print("Dairenin Alanı: ", alan)

cevre = 2 * pi * x
print("Dairenin Çevresi: ", cevre)

print("*******************************************")
# Bir aracın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
# mil = km/1.609344

km = float(input("Lütfen Km degeri giriniz"))
mil = km // 1.609344
print("Mil Karşılığı", mil)
