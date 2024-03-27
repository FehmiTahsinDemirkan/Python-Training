from instabot import Bot
import time
import random

my_bot = Bot()

#login
my_bot.login(username="junior_to_senior", password="fehmitahsin1078")

# Bekleme fonksiyonu
def bekle():
    time.sleep(random.uniform(1, 3))  # 1 ile 3 saniye arasında rastgele bir bekleme

# Takip işlemi
def takip_et(kullanici):
    try:
        my_bot.follow(kullanici)
        print(f"{kullanici} kullanıcısını takip ediliyor.")
        bekle()
    except Exception as e:
        print(f"Hata: {e}")

# Takip edilmeyenleri takip etmeyi denetleme
def takip_edilmeyenleri_takip_et():
    try:
        my_bot.unfollow_non_followers()
        print("Takip edilmeyenler takip ediliyor.")
        bekle()
    except Exception as e:
        print(f"Hata: {e}")

# İstenilen sayfaları takip etme işlemi
def sayfalari_takip_et(sayfalar):
    for sayfa in sayfalar:
        takip_et(sayfa)

# Ana işlem
def ana_islem():
    sayfalar = ["galatasaray", "besiktas", "fenerbahce"]
    sayfalari_takip_et(sayfalar)
    takip_edilmeyenleri_takip_et()

# Ana işlemi çalıştırma
ana_islem()
