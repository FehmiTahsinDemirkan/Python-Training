def sayi_say(max):
    sayi = 1
    while sayi <= max:
        yield sayi
        sayi +=1
generator = sonuc =sayi_say(10)
print(help(generator))
iterator = iter(generator)


