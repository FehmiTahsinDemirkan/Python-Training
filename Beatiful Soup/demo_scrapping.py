import requests
from bs4 import BeautifulSoup
from csv import writer
url = "https://sadikturan.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

kurslar = soup.find_all(class_="kurs")

with open('kurslar.csv','w') as csv_file: #'w' write modunda açılacağını bildiriyor
    csv_writer = writer(csv_file)
    csv_writer.writerow(['kurs_resmi','kurs_basligi','kurs_aciklama','udemy_link','site_link'])
    for kurs in kurslar:
        kurs_resmi = kurs.find('img')['src']
        kurs_basligi = kurs.find(class_="media-body").find('h2').string
        kurs_aciklama = kurs.find(class_="media-body").find('span').string
        kurs_linkler = kurs.find(class_="card-footer").find_all('div')[1].find_all('a')
        kurs_udemy_link = kurs_linkler[0]['href']
        kurs_site_link = url + kurs_linkler[1]['href']

        csv_writer.writerow([kurs_resmi,kurs_basligi,kurs_aciklama,kurs_udemy_link,kurs_site_link])




