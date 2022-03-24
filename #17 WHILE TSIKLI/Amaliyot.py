# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:03:38 2022

@author: Shohruhh077
"""

"""
Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
"""
# savol = "Yoqtirgan kitobingizni kiriting"
# savol += "(Barcha kitoblaringizni kiritib bo`lgach \"exit\" deb yozing):\n"

# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print("Dastur tugatildi")


"""
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan
yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi
yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit
deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
"""
# savol = "Yoshingizni kiriting "
# savol += "(Dasturdan chiqish uchun \"exit\" yoki \"quit\" deb yozing!):\n>>>"
# while True:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit' :
#         break
#     yosh = float(yosh)
    
#     if yosh < 7:
#         narx = 2000
#     elif yosh <= 18:
#         narx = 3000
#     elif yosh <= 65:
#         narx = 10000
#     else:
#         narx = 0
    
#     if narx == 0:
#         print("Sizga chipta bepul.")
#     else:
#         print(f"Sizga chipta narxi {narx} so`m")
# print("Darturni to`xtatdingiz.")


"""
Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy
holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
"""
# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")




