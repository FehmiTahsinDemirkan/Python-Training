def sayi_say(max):
    sayi = 1
    while sayi <= max:
        yield sayi
        sayi +=1
iterator = sonuc =sayi_say(10)
# print(help(generator))
for i in iterator:
    print(i)


# Generator:
# Generator, iterator'lar gibi çalışan ancak daha 
# basit bir sözdizimine sahip olan özel bir fonksiyondur. Generator, değerleri yield ifadesi aracılığıyla üretir ve her çağrıldığında durumunu hatırlar. Bu sayede bellek etkisi minimize edilir.