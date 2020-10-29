import random

print("****4 Basamaklı rastgele bir sayıyı tahmin etme oyunu****\nOyunun kurallları şu şekil:\nTahmin ettiğin sayı doğru yerde ve doğru sayı ise 1 inek olduğunu söyleyeceğim. Doğru sayı fakat doğru yerde olmadığında bir boğa diyeceğim.\nBöylelikle sen bulana kadar devam edicek program.\nHaydi Başlayalım!!")


syimiz = random.randint(1000,9999)
sayimiz = str(syimiz)



def inekboga(inek=0,boga=0):

        tahmin_sayisi = input('Tahmininiz:')  
        
        if tahmin_sayisi[0] == sayimiz[0]:
            inek += 1       
        if tahmin_sayisi[1] == sayimiz[1]:
            inek += 1       
        if tahmin_sayisi[2] == sayimiz[2]:
            inek += 1
        if tahmin_sayisi[3] == sayimiz[3]:
            inek += 1
        

        if (tahmin_sayisi[0] == sayimiz[1]) or (tahmin_sayisi[0] == sayimiz [2]) or (tahmin_sayisi[0] == sayimiz[3]):
            boga += 1           
        if (tahmin_sayisi[1] == sayimiz[0]) or (tahmin_sayisi[1] == sayimiz[2]) or (tahmin_sayisi[1] == sayimiz[3]):
            boga += 1           
        if tahmin_sayisi[2] == sayimiz[0] or (tahmin_sayisi[2] == sayimiz[1]) or (tahmin_sayisi[2] == sayimiz[3]):
            boga += 1            
        if tahmin_sayisi[3] == sayimiz[0] or (tahmin_sayisi[3] == sayimiz[1]) or (tahmin_sayisi[3] == sayimiz[2]):
            boga += 1            
        kontrol(inek,boga)
        
def kontrol(inek,boga):
    if int(inek) < 4:
        print(f'inek sayısı: {inek},boğa sayısı: {boga}')
        inekboga()
    elif inek == 4:
        print('Mükemmelsin çok çabuk bildin gerçekten.')

inekboga()


    
