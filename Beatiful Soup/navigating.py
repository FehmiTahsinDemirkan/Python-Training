from bs4 import BeautifulSoup
with open("index.html") as file :
    html_doc = file.read()

obj = BeautifulSoup(html_doc,"html.parser")

sonuc = obj.head
sonuc = obj.body.div.contents[1]
sonuc = obj.body.div.contents[3].contents[1]



h2 = obj.body.h2
div = h2.parent
div2 = div.next_sibling.next_sibling
print(div2)