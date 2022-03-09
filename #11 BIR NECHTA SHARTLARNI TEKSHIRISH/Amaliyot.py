# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:24:22 2022

@author: Shohruhh077
"""

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring
son = float(input("Juft son kiriting: "))
if son%2 == 0 :
    print("Rahmat")
else:
    print("Bu juft son emas!")


# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#     Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#     Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#     Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = float(input("Iltimos yoshingizni ayting: "))
if yosh < 4 or yosh >60 :
    narh = 0
elif yosh < 18 :
    narh = 10000
elif yosh > 18 :
    narh = 20000
print(f"Muzeyga kirish sizga {narh} so`m!")


# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
son1 = float(input('1-Sonni kiriting: '))
son2 = float(input('2-Sonni kiriting: '))
if son1 > son2 :
    print(f"{son1} > {son2}")
elif son1 < son2 :
    print(f"{son1} < {son2}")
elif son1 == son2 :
    print(f"{son1} = {son2}")


# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring
mahsulotlar = ["anor", "banan", 'limon', 'kofe', 'fanta', 'energetik', 'non', 'kolbasa', 'tamaki', 'qatiq']
savat =[]
mah_soni = int(input("Nechta mahsulot olmoqchisiz?\n>>>"))
for n in range(mah_soni) :
    savat.append(input(f"{n+1}-olmoqchi bo`lgan mahsulotingiz nima?\n>>>"))
for mahsulot in savat :
    if mahsulot in mahsulotlar :
        print(f"{mahsulot.title()} do`konimizda bor")
    else :
        print(f"{mahsulot.title()} do`konimizda yo`q")


# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring
mahsulotlar = ["anor", "banan", 'limon', 'kofe', 'fanta', 'energetik', 'non', 'kolbasa', 'tamaki', 'qatiq']
savat =[]
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5) :
    savat.append(input(f"{n+1}-olmoqchi bo`lgan mahsulotingiz nima?\n>>>"))
for mahsulot in savat :
    if mahsulot in mahsulotlar :
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if len(mavjud_emas) > 0 :
    print(f"Quyidagi mahsulotlar do`konimizda mavjud emas:\n {mavjud_emas}")
else:
    print("Do`konimizda siz so`ragan barcha mahsulotlar mavjud")


# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring
foydalanuvchilar = ['shohruh', 'jo`rabek', 'anvar', 'akrom', 'farrux']
login = input("O`zingizga yangi login tanlang:\n>>>")
if login.lower() in foydalanuvchilar :
    print("Login band, yangi login tanlang!")
else :
    print("Xush kelibsiz, foydalanuvchi!")


# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring
son = int(input("Birir butun sonni kiriting: "))

for n in range(2, 11):
    if son % n == 0 :
        print(f"{son} soni {n} ga qoldiqsiz bo`linadi")
