# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:27:07 2022

@author: Shohruhh077
"""

#Quyidagi o'zgaruvchilarni yarating: 
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"1-2
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"


# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")


# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha=input("Ko'cha nomini yozing:\n->")
mahalla=input("Mahalla nomini yozing:\n->")
tuman=input("Tuman nomini yozing:\n->")
viloyat=input("Viloyat nomini yozing:\n->")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati\n")


# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + tuman + " tumani,\n" + viloyat + " viloyati\n")
manzil=f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
