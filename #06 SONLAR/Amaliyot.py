# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:35:42 2022

@author: Shohruhh077
"""

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
son = int(input("Istalgan sonni kiriting:\n >>>"))
print(son, " ning kvadrati ", son**2, " ga teng")
print(son, " ning kubi ", son**3, " ga teng")


# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
yosh = int(input("Yoshingiz nechchida?\n >>>"))
print("Siz", 2022-yosh, "yilda tug`ilgansiz")


# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
son1 = float(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting: "))
print(f"{son1} + {son2} =", son1+son2)
print(f"{son1} - {son2} =", son1-son2)
print(f"{son1} * {son2} =", son1*son2)
print(f"{son1} / {son2} =", son1/son2)
