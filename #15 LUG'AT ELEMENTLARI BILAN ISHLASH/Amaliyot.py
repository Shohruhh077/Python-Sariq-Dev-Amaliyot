# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:07:51 2022

@author: Shohruhh077
"""
"""
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida,
alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
"""
# lugat ={
#         'integer' : 'butun son',
#         'float' : 'o`nli son',
#         'boolean' : 'mantiqiy qiymat',
#         'string' : 'matn',
#         'tuple' : 'o`zgarmas jadval',
#         'title' : 'so`zni bosh harfini katta harfda yozadi',
#         'capitalize' : 'matnni birinchi harfini katta harfda yozadi',
#         'lower' : 'matnni hamma harfini kichik harfda yozadi',
#         'for' : 'biror amalni qayta-qayta takrorlaydi',
#         'if' : 'biror shartni tekshirish operatori',
#         }
# print("Python izohli lug`ati quyidagicha:")
# for kalit, qiymat in sorted(lugat.items()) :
#     print(f"{kalit.capitalize()}-{qiymat.capitalize()}")


"""
Davlatlar va ularning poytaxtlari lug'atini tuzing.
Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
alifbo ketma-ketligida konsolga chiqaring. 
"""
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'
#     }
# print("Dunyo davlatlari quyidagilar:")
# for davlat in sorted(davlatlar.keys()) :
#     print(davlat.upper())
# print("Davlatlarning poytaxti quyidagilar:")
# for poytaxt in sorted(davlatlar.values()) :
#     print(poytaxt.capitalize())


"""
Foydalanuvchidan istalgan davlatni kiritishni so'rang
va shu davlatning poytaxtini konsolga chiqaring.
Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
"Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
"""
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'
#     }
# qiymat = input("Qaysi davlatning poytaxtini bilishni xoxlaysiz?\n>>>").lower()
# country = davlatlar.get(qiymat)
# if country:
#     print(f"{qiymat.upper()} davlatining poytaxti {davlatlar[qiymat].title()} shahri hisoblanadi. ")
# else :
#     print(f"Kechirasiz bizda {qiymat.upper()} davlati haqida hech qanday ma'lumot yo`q")


"""
Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan
taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
"""
# menu = {
#         'osh':20000,
#         "lag`mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000,
#         'sho`rva' : 20000,
#         'kabob' : 30000,
#         'baliq' : 25000
#         }
# buyurtmalar = []
# for son in range(3) :
#     taom = input(f"{son+1}-taomga nima buyurtma berasiz?\n>>>").lower()
#     buyurtmalar.append(taom)
# for buyurtma in buyurtmalar :
#     if buyurtma in menu :
#         print(f"{buyurtma.capitalize()}ning narxi {menu[buyurtma]} so`m")
#     else :
#         print(f"Kechirasiz bizning menyumizda {buyurtma.capitalize()} mavjud emas")


    


    
    