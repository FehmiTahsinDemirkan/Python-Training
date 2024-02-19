import random

sayi = random.randint(1, 100)
can_sayisi = int(input("Kaç hak kullanmak istersiniz? "))
puan = 100

while can_sayisi > 0:
    tahmin = int(input("Tahmininizi girin: "))

    if tahmin < 1 or tahmin > 100:
        print("Lütfen 1 ile 100 arasında bir sayı girin.")
        continue

    if tahmin < sayi:
        print("Yukarı. Kalan can:", can_sayisi - 1)
    elif tahmin > sayi:
        print("Aşağı. Kalan can:", can_sayisi - 1)
    else:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break

    can_sayisi -= 1
    puan -= 20

print(f"Oyun bitti. Puanınız: {puan}")

