#itarable ?

#Python dilinde iterator ve generator kavramları, veri koleksiyonları üzerinde dönmek
#için kullanılan ve bellek etkisi minimize edilmiş özel yapıları ifade eder. İ
#iterator ?

sayilar = [1,2,3,4,5]

iterator = iter(sayilar)

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break

#     Iterator:
# Iterator, bir sıralı veri koleksiyonu üzerinde dolaşmak için kullanılan bir nesnedir. Iterator'lar, __iter__() ve __next__() metodlarına sahip olurlar.

# __iter__() metodu, iterator nesnesini döndürür.
# __next__() metodu, bir sonraki elemanı verir ve koleksiyonun sonuna geldiğinde StopIteration hatası fırlatır.