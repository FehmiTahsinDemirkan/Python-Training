#Error

#Error Handling

try:
    x = int(input("Bir X değeri giriniz:"))
    y = int(input("Bir y değeri giriniz:"))
    print(f"x+y : {x+y}")
except:
    print("bilinmeyen bir hata")
