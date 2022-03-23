# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:26:04 2022

@author: Shohruhh077
"""

"""
Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar
haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta
ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
"""
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#             'tyil':810,
#             'vyil':870,
#             'tjoy':'Buxoro'
#             }

# qodiriy = {'ism':'Abdulla Qodiriy',
#             'tyil':1894,
#             'vyil':1938,
#             'tjoy':'Toshkent'
#             }

# vohidov = {'ism':'Erkin Vohidov',
#             'tyil':1936,
#             'vyil':2016,
#             'tjoy':"Farg'ona"
#             }

# navoiy = {'ism':'Alisher Navoiy',
#             'tyil':1441,
#             'vyil':1501,
#             'tjoy':"Xirot"
#             }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar :
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. {vyil-tyil} yil umr ko`rib {vyil}-yilda vafot etgan.")


"""
Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
"""
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#             'tyil':810,
#             'vyil':870,
#             'tjoy':'Buxoro',
#             'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#             }

# qodiriy = {'ism':'Abdulla Qodiriy',
#             'tyil':1894,
#             'vyil':1938,
#             'tjoy':'Toshkent',
#             'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#             }

# vohidov = {'ism':'Erkin Vohidov',
#             'tyil':1936,
#             'vyil':2016,
#             'tjoy':"Farg'ona",
#             'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#             }

# navoiy = {'ism':'Alisher Navoiy',
#             'tyil':1441,
#             'vyil':1501,
#             'tjoy':"Xirot",
#             'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#             }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar :
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism}ning eng mashxur asarlari:")
#     for asar in asarlar:
#         print(asar)


"""
Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida
so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat
ko'rinishida lug'atga saqlang.  Natijani konsolga chiqaring.
"""
# kinolar = {
#     'akrom':['Terminator','Бригада','Titanic'],
#     'vali':['Qashqirlar makoni','Inception','Interstellar'],
#     'anvar':['Abdullajon','Bomba','Shaytanat'],
#     'siroj':['Mahallada duv-duv gap','John Wick']
#     }

# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.capitalize()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)


"""
Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar
haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat
haqida ma'lumotni konsolga chiqaring.
"""
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }
# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat=davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].capitalize()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholi soni: {info['aholi']} kishi"
#           f"\nPul birligi: {info['pul birligi']}")


"""
Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas,
foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning
lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan
xabarni chiqaring.
"""    
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                     'maydon':448978,
#                     'aholi':33_000_000,
#                     'pul birligi':"so'm"
#                     },
#     "rossiya":{'poytaxt':"moskva",
#                     'maydon':17_098_246,
#                     'aholi':144_000_000,
#                     'pul birligi':"rubl"
#                     },
#     "aqsh":{'poytaxt':"vashington",
#                     'maydon':9_631_418,
#                     'aholi':327_000_000,
#                     'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                     'maydon':329750,
#                     'aholi':25_000_000,
#                     'pul birligi':"rinngit"}
#     }
# country = input("Ma'lumot olmoqchi bo`lgan davlatingizni nomini kiriting: ")
# country = country.lower()
# if country in davlatlar:
#     info = davlatlar[country]
#     if country == 'aqsh':
#         country = country.upper()
#     else:
#         country = country.capitalize()
#     print(f"{country}ning poytaxti {info['poytaxt'].capitalize()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholi soni: {info['aholi']} kishi"
#           f"\nPul birligi: {info['pul birligi']}")

