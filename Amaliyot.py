# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:21:53 2022

@author: Shohruhh077
"""

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car.lower() == 'gm':
        print(car.upper())
    else:
        print(car.title())


# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car.lower() != 'gm':
        print(car.title())
    else:
        print(car.upper())


# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring
login = input("Loginni kiriting: ")
if login.lower() == 'admin':
    print(f"Xush kelibsiz, {login.title()}. Foydalanuvchilar ro`yxatini ko`rasizmi?")
else:
    print(f"Xush kelibsiz, {login.title()}!")


# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring
son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
if son1 == son2:
    print("Sonlar teng")


# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring
son = float(input("Istalgan sonni kiriting:\n>>>"))
if son < 0 :
    print(f"Siz kiritgan {son} soni manfiy son")
else:
    print(f"Siz kiritgan {son} soni musbat son")


# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring
son = float(input("Son kiriting:\n>>>"))
if son > 0 :
    print(f"Siz kiritgan {son} ning ildizi {son**(1/2)} ga teng")
else:
    print("Musbat son kiriting!")
