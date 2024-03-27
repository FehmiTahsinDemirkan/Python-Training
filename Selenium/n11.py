from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:/chromedriver.exe"
url = "https://www.n11.com/urun/bianca-stella-su-bazli-saf-akrilik-boya-500-ml-28958386?magaza=ciftciburada"

driver = webdriver.Chrome()
driver.get(url)

# Bekleme süresi: 10 saniye
wait = WebDriverWait(driver, 10)

try:
    # 'priceContainer' elementini bulana kadar bekle
    price_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'priceContainer')))

    # 'priceContainer' içindeki 'oldPrice' elementini bul
    old_price = price_container.find_element(By.CLASS_NAME, 'oldPrice')

    # Eski fiyatı al
    old_price_text = old_price.text.strip()
    print("Indirimli Fiyat:", old_price_text)

except Exception as e:
    print("Hata:", e)

finally:
    # Tarayıcıyı kapat
    driver.quit()
