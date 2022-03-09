# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:17:35 2022

@author: Shohruhh077
"""

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
ismlar = ["Jo`rabek", "Farrux", "Anvar", "Shohruh", "Sunnat"]
for ism in ismlar:
    print(f"Salom {ism}")
print(f"Kod {len(ismlar)} marotaba takrorlandi")


# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring
toq_sonlar = list(range(11, 100, 2))
for son in toq_sonlar:
    print(son**3)


# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring
kinolar = []
for n in range(5):
    kinolar.append(input(f"{n+1}-sevimli kinoyingizni nomi nima?\n>>>"))
print(kinolar)


# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring
suxbatdoshlar = []
n = int(input("Bugun nechta kishi bilan suxbat qurdingiz?\n>>>"))
for i in range(n):
    suxbatdoshlar.append(input(f"{i+1}-suxbatlashgan insoningiz ismi nima?\n>>>"))
print(suxbatdoshlar)
