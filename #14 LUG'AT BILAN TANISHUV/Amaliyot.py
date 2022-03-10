# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:00:02 2022

@author: Shohruhh077
"""
"""
otam (onam, akam, ukam, va hokazo) degan lug'at yarating
va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting
(ismi, tu'gilgan yili, shahri, manzili va hokazo).
Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring:
Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
"""
otam = {
        'ism':'g`aybulla',
        'familiya':'davlatov',
        't_yil':1960,
        't_oy':'aprel',
        't_sana':16
        }
onam = {
        'ism':'xonigul',
        'familiya':'muhammadiyeva',
        't_yil':1960,
        't_oy':'dekabr',
        't_sana':24
        }
akam = {
        'ism':'valijon',
        'familiya':'ravshanov',
        't_yil':1991,
        't_oy':'noyabr',
        't_sana':4
        }
print(f"Otamning ismi {otam['ism'].capitalize()}, familiyasi {otam['familiya'].title()}, {otam['t_sana']}-{otam['t_oy']} {otam['t_yil']}-yilda tug`ilgan")
print(f"Onamning ismi {onam['ism'].capitalize()}, familiyasi {onam['familiya'].title()}, {onam['t_sana']}-{onam['t_oy']} {onam['t_yil']}-yilda tug`ilgan")
print(f"Akamning ismi {akam['ism'].capitalize()}, familiyasi {akam['familiya'].title()}, {akam['t_sana']}-{akam['t_oy']} {akam['t_yil']}-yilda tug`ilgan")


"""
Oila a'zolaringizning sevimli taomlari lug'atini tuzing.
Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
Kamida uch kishining sevimli taomini konsolga chiqaring:
Alining sevimli taomi osh
"""
taom = {
        'vali':'palov',
        'jo`rabek':'somsa',
        'shohruh':'kabob',
        'akrom':'shashlik',
        'farrux':'sho`rva'
        }
vali= taom['vali']
shohruh = taom['shohruh']
akrom = taom['akrom']
print(f"Valining sevimli taomi {vali}")
print(f"Shohruh taomlardan {shohruh}ni yaxshi ko`radi ")
print(f"Akrom {akrom}ni sevib iste'mol qiladi.")


"""
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan
10 ta so'z (atamani) kiriting (masalan integer, float, string, if,
else va hokazo) va har birining qisqacha tarjimasini yozing.
"""
lugat = {
    'int':'butun son',
    'float':'o`nli son',
    'str':'matn',
    'list':'ro`yxat',
    'tuple':'o`zgarmas yo`yxat',
    'dict':'lug`at'
         }
print(lugat['int'].capitalize())
print(lugat['float'].capitalize())
print(lugat['str'].capitalize())
print(lugat['list'].capitalize())
print(lugat['tuple'].capitalize())
print(lugat['dict'].capitalize())


"""
Foydalanuvchidan biror so'z kiritishni so'rang va so'zning
tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z
lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
"""
lugat = {
    'int':'butun son',
    'float':'o`nli son',
    'str':'matn',
    'list':'ro`yxat',
    'tuple':'o`zgarmas yo`yxat',
    'dict':'lug`at'
          }
nom = input("Qaysi so`zni ma'nosi kerak?\n>>>")
print(lugat.get(nom,"Bunday so`z lug`atimizda mavjud emas"))


"""
Yuqoridagi vazifani if-else yordamida qiling va natijani
ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
"""
lugat = {
    'int':'butun son',
    'float':'o`nli son',
    'str':'matn',
    'list':'ro`yxat',
    'tuple':'o`zgarmas yo`yxat',
    'dict':'lug`at'
          }
nom = input("Qaysi so`zni ma'nosi kerak?\n>>>")
if nom.lower() in lugat :
    print(f"{nom}-{lugat[nom].capitalize()}")
else :
    print("Lug`atimizda bunday so`z mavjud emas")



