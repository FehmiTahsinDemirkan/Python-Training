from bs4 import BeautifulSoup

file_path = 'C:\\Users\\fehmi\\PycharmProjects\\Python-Training\\Beatiful Soup\\index.html'

with open(file_path) as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")

sonuc = obj
sonuc = obj.prettify()
sonuc = type(obj)
sonuc = obj.title
sonuc = type(obj.title)
sonuc = obj.title.name
sonuc = obj.title.string

sonuc = obj.body
sonuc = obj.body.h1
sonuc = obj.h1
sonuc = obj.h1.name
sonuc = obj.h1.string
sonuc = obj.div


print(sonuc)
