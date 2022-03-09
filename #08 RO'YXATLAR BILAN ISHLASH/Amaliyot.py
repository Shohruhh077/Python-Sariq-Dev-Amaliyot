# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:12:44 2022

@author: Shohruhh077
"""

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring        
davlatlar = ["britaniya", "uzbekiston", "rossiya", "angliya", "germaniya"]
print(davlatlar)


# Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))


# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))


# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))


# Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)


# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)


# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)


# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120, 1201, 2))
print(juft_sonlar)


# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(juft_sonlar))


# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(juft_sonlar)-min(juft_sonlar))


# Ro'yxatdagi elementlar sonini hisoblang
print(len(juft_sonlar))


# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(juft_sonlar[:20])
print(juft_sonlar[-20:])
print(juft_sonlar[531:552])


# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["osh", "somsa", "chuchvara", "kabob", "tabaka"]


# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]


# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
del nonushta[0]
nonushta.remove('chuchvara')
nonushta.remove('kabob')
nonushta.append("norin")
nonushta.append("Sho`rva")


# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)


# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring
nonushta = tuple(nonushta)
nonushta[0] = "Qaymoq va non"

