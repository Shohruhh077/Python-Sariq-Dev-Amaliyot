# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:37:38 2022

@author: Shohruhh077
"""

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ["temur", 'anvar', 'sunnat']



# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print(ismlar[0].title() + " bugun qayerga boramiz?")
print('Salom ' + ismlar[1].title() + ' choyxonaga borasanmi?')
print("Qalesan " + ismlar[-1].title() + ' bugun ' + ismlar[0].title() +
      ', ' + ismlar[1].title() + " va men choyxonaga borayabmiz.")


# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [14, -12, 55, 17.5]

# yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
qushish = sonlar[0] + sonlar[1]
print(qushish)
ayirish = sonlar[0] - sonlar[2]
print(ayirish)
kupaytirish = sonlar[1] * sonlar[-1]
print(kupaytirish)
bulish = sonlar[2] / sonlar[-1]
print(bulish)

sonlar[1] = sonlar[1] + 25
sonlar[-1] = 20.2

sonlar.append(77)
del sonlar[0]
sonlar.remove(55)


# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['amir temur', "mirzo ulug'bek", 'alisher navoiy']
z_shaxslar = ['bill geyts', 'stiv jobs', 'elon musk']


# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print("Men ta'rixiy shaxslardan " + t_shaxslar.pop(1).title() + 
      " bilan,\nZamonaviy shaxslardan esa " + z_shaxslar.pop(-1).title() +
      " bilan \nsuxbat qurishni istar edim")


# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append("anvar")
friends.append('sunnat')
friends.append('g`iyos')
friends.append('behzod')
friends.append('siroj')
print(friends)


# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove('g`iyos')
print(friends)


# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('g`iyos')
friends.insert(0, 'ulug`bek')
friends.insert(2, 'vohid')
print(friends)

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(-3))
print(mehmonlar)
