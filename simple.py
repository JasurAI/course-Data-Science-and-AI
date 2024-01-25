# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:50:39 2023

@author: Jasur Mamarakhimov
"""
"""sonlar = [1, 2, 3, 4, 5, 6]
sonlar2 = sonlar[:]
sonlar2.append(7)
sonlar2.append(8)
print(" Sonlar = ", sonlar, " Sonlar2 = ", sonlar2)
print('       Assalomu alaykum, xush kelibsiz !')
print(" Quyida siz yashash manzilingizni so'ralgan tartibda faqat raqamlari va nomlarini kiriting !")
xonadon = input(" Xonadoningiz raqamini kiriting:  ")
uy = input(" Uy raqamini kiriting:  ") 
kocha = input(" Ko'changiz nomini kiriting:  ")
mahalla = input(" Mahallangiz nomini kiriting:  ")
tuman = input(" Tumaningiz nomini kiriting:  ")
viloyat = input(" Viloyatingiz nomini kiriting:  ")
print("  Siz " + viloyat.title() + " viloyati, " + tuman.title() + " tumani, "\
 + mahalla.title() + " mahallasi, " + kocha.title() + " ko'chasi, " + uy + \
 "-uy, " + xonadon + "-xonadonda yashaysiz.")
print(" Kiritilgan ma'lumotlaringiz to'g'riligini tasdiqlang !")
tasdiq = input(" Tasdiqlash ha/yoq: ")
tasdiq = tasdiq.lower()
if tasdiq=="ha":
    print(" Ma'lumotlaringiz to'g'riligi tasdiqlandi")
else: print(" Kechirasiz!  Ma'lumotlaringiz to'g'riligi tasdiqlanmadi. Qaytadan tekshirib kiriting !")
print(list(range(1,51,2))) """


"""
friends = []
friends.append("Sarvar")
friends.append("Shoxrux")
friends.append("Begzod")
friends.append("Nodir")
friends.append("Zokir")
friends.append("Ulug'bek")
print(friends)
friends.remove("Shoxrux")
del friends[4]
print(friends)
friends.append("Rizamat")
friends.insert(0, "Bektosh")
friends.insert(3, "Ulug'bek")
print(friends)
mehmonlar=[]
mehmonlar.append("Dilshod")
mehmonlar.append("O'lmas")
mehmonlar.append("Shaxzod")
mehmonlar.insert(0, friends.pop(0))
mehmonlar.insert(0, friends.pop(1))
mehmonlar.insert(0, friends.pop(1))
mehmonlar.insert(0, friends.pop(2))
mehmonlar.insert(0, friends.pop(2))

print(friends)
print(mehmonlar) 

#          RO'YXATLARNI TARTIBLASH

Countries = ["Uzbekistan", "Kazaxstan", "Russia", "China", "Mongoly", "Korea",\
             "Japan", "Krgizya", "Tadjikistan", "Turkmenya", "Iran", "Turkey"]
print(len(Countries))
print("Sorted metodida - ", sorted(Countries))
print("Teskari Sorted metodida - ", sorted(Countries, reverse=True))
print("Asli - ", Countries)
Countries.sort()
print("Sort metodi - ", Countries)
Countries.sort(reverse=True)
print("Teskari tartiblangan - ", Countries)            

#              RANGE() FUNKSIYASI

juftsonlar = list(range(120, 1200, 2))
print(juftsonlar)
summa = sum(juftsonlar)
print("Yuqoridagi juft sonlar yig'indisi ", summa, " ga teng")
katta = max(juftsonlar)
kichik = min(juftsonlar)
print("Max - Min = ", katta-kichik)
print("Yuqorida ", len(juftsonlar), " ta son bor")
print(juftsonlar[0:20], juftsonlar[260:280], juftsonlar[520:540])
juftsonlar=tuple(juftsonlar)
print(juftsonlar)
                                            
                                            
#                 FOR SIKLI

mevalar = ["olma", "anor", "xurmo", "banan", "limon"]
narxlar = [15000, 20000, 18000, 22000, 28000]; l = 0
for meva in mevalar:
    narx = []
    for n in narxlar:
        narx.append(n)
    print(f"Bizda {meva} bor, uning narxi {narx[l]} so'm turadi")
    l = l+1
print("Kod ", l, " marta takrorlandi")

Toqsonlar = list(range(11, 100, 2))
print("10 dan 100 gacha toq sonlar - ", Toqsonlar)
for son in Toqsonlar:
    print(f"{son} toq soninig kubi {son**3} soniga teng")

#           For and Input        

kinolar = []
for m in list(range(5)):
    kinolar.append(input(f"{m+1}-Sevimli kinoingizni ayting: ")) 
print("Sizning sevimli filmlaringiz : ", kinolar)     
                                                       
                                                       
                        #    IF-ELSE OR,AND,NOT
                        
                        
yosh = int(input("Yoshingizni kiriting: "))
if yosh<=4 or yosh>=60:
    bilet=0
elif yosh<18:
    bilet=10000
else:
    bilet=20000
print(f"Sizga kirish {bilet} so'm")
                                                    

##################################################################

mahsulotlar = ["olma", "uzum", "anor", "xurmo", "o'rik", "olcha", "shaftoli",\
               "sabzi", "karam", "olxo'ri"]
savat = []
print(" 5 ta mahsulot kiriting !")
for n in range(5):
    savat.append(input(f"Olmoqchi bo'lgan {n+1} - mahsulotni kiriting : "))
bor_mahsulotlar = [] 
mavjud_emas = []   
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("Kechirasiz, Quyidagi mahsulotlar do'konimizda yoq: ", mavjud_emas)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#                      Ro'yxatlar                                                              
                                                    
foydalanuvchilar = ["Qwer1", "Qwer2", "Qwer3", "qwer4", "qwer5"]
login = input("Loginingizni kiriting: ")
if login in foydalanuvchilar:
    print(f"Xush kelibsiz {login} foydalanuvchi")
else:
    print(f"Siz kiritgan {login} logini mavjud emas, tekshirib qayta \
kiriting yoki yangi login tanlang !")
                                                             


son = int(input("Biror son kiriting: "))
print(f"Siz kiritgan {son} quyidagi raqamlarga qoldiqsiz bo'linadi:")
for b in list(range(1,10)):
    qoldiq = son%int(b)
    if qoldiq==0:
        print(b)
                                                        
#                       Lug'at

countries = { 'Uzbekistan':'Tashkent',
              'Kazaxstan':'Astana',
              'Russia':'Moscow',
              'Kyrgyzstan':'Bishkek',
              'Tadjikistan':'Dushanbe',
              'South Korea':'Seul',
              'Japan':'Tokyo',
              'China':'Beijing',
              'India':'New Dehli',
              'Pakistan':'Islamabad',
              'Afghanistan':'Kabul',
              'Turkey':'Istanbul',
              'Iran':'Tehron',
              'Qatar':'Doha',
              'Turkmenistan':'Ashgabat',
              'Azerbaijan':'Baku'}
#for co, ca in sorted(set(countries.items())):
#    print(f"Country: {co}   -   Capital: {ca}")
country = input("Biror davlatni kiriting: ")
country = country.lower()
country = country.title()
if country in countries:
    print(f"{country} mamlakatining poytaxti {countries[country]}")
else:
    print("Bizda bu mamlakat haqida ma\'lumot yo\'q")
   # country = countries.get('country', 'Bizda bu mamlakat bo\'yicha malumot yo\'q')
    #print(country)
                                                    

#                      To'plamlar
bozorlik = ['choy', 'non', 'kartoshka', 'tuxum', 'sut']
bozorlik = set(bozorlik)
mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']
mahsulotlar = set(mahsulotlar)
bozorlik.add('go\'sht')
mahsulotlar.update({'yog\'', 'shakar', 'guruch', 'mosh'})
bor_mahsulotlar = list(bozorlik&mahsulotlar)  #bozorlik.intersection(mahsulotlar)
dokonda_yoq = list(bozorlik-mahsulotlar)  #mahsulotlar.difference(bozorlik)
print("Bozorlik: ", bozorlik)
print("Do'kondagi barcha mahsulotlar: ", mahsulotlar)
print("Do'konda bor bozorlik: ", bor_mahsulotlar)
print("Do'konda yoq bozorlik: ", dokonda_yoq)

                                                           
#                  NESTING - lug'at ichida lug'at yoki ro'yxat yoki aksincha


countries = {
    'Uzbekistan':{'poytaxti':'Tashkent',
                  'mustaqilligi':'1991',
                  'prezidenti':'Shavkat Mirziyoyev',
                  'millatlar':['o\'zbek', 'tojik', 'qozoq', 'rus', 'tatar', 'va boshqalar'],
                  'davlatchiligi':'respublika'
                  },
    'Kazaxstan':{'poytaxti':'Astana',
                 'mustaqilligi':'1991',
                 'prezidenti':'Kasim Jomart Toqayev',
                 'millatlar':['qozoq', 'o\'zbek', 'tojik', 'rus', 'tatar', 'va boshqalar'],
                 'davlatchiligi':'respublika'
                 },
    'Russia':{'poytaxti':'Moskva',
                 'mustaqilligi':'1691',
                 'prezidenti':'Vladimir Putin',
                 'millatlar':['rus', 'tatar', 'qozoq', 'o\'zbek', 'tojik',  'va boshqalar'],
                 'davlatchiligi':'federativ respublika'
                 },
    'Tadjikistan':{'poytaxti':'Dushanbe',
                 'mustaqilligi':'1991',
                 'prezidenti':'Imomali Raxmon',
                 'millatlar':['tojik', 'rus', 'qozoq', 'o\'zbek', 'va boshqalar'],
                 'davlatchiligi':'respublika'
                 },
    'Turkey':{'poytaxti':'Istanbul',
                 'mustaqilligi':'1785',
                 'prezidenti':'Rajap Tayip Erdog\'an',
                 'millatlar':['turk', 'o\'zbek', 'rus', 'tatar', 'va boshqalar'],
                 'davlatchiligi':'respublika'
                 },
    'Azerbaijan':{'poytaxti':'Baku',
                 'mustaqilligi':'1991',
                 'prezidenti':'Ilxom Aliyev',
                 'millatlar':['azarbayjon', 'rus', 'tatar', 'va boshqalar'],
                 'davlatchiligi':'respublika'
                 }
    }
for country, info in countries.items():
    print(f"\n{country} mamlakati to'g'risida ma'lumotlar:\n"
          f"Mamlakat poytaxti - {info['poytaxti']}\n"
          f"Mustaqillikga erishgan yili - {info['mustaqilligi']}-yil\n"
          f"Mamlakatning hozirgi prezidenti - {info['prezidenti']}\n"
          f"Bu mamlakatda ko'p uchraydigan millatlar - {info['millatlar']}\n")

                                                                   

#                                 WHILE

y = "Bilet olish uchun yoshingizni kiriting.\n"
y += "QUIT yoki EXIT kiritish orqali dasturdan chiqishingiz mumkin. \n"
y += "         Kiriting: "
yosh = True
while yosh:
    yosh = input(y)
    yosh = yosh.lower()
    if yosh == 'quit' or yosh == 'exit':
        print("Siz dasturdan chiqdingiz!")
        yosh = False
    else:
        if int(yosh)<7:
            bilet = 2000
        elif int(yosh)>=65:
            bilet = 0
        elif int(yosh)>=18:
            bilet = 10000
        else:
            bilet = 3000
        print(f"\nSiz uchun muzeyga kirish bilet narxi {bilet} so'm")
        break
                      

                                         
s = "Son ildizini aniqlash\n"
s += "Musbat son kiriting "
s += "(Dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(s)
    if qiymat.lower() == 'exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

                                                          

#                          FUNCTION

def qoldiqsiz_bolish(son):
#    ""Kiritilgan sonni raqamlar(1-10)ga qoldiqsiz bo'linishini ko'rsatadi""
 #   son = int(input("Biror son kiriting: "))
    print(f"Siz kiritgan {son} quyidagi raqamlarga qoldiqsiz bo'linadi:")
    for b in list(range(1,10)):
        qoldiq = son%int(b)
        if qoldiq==0:
            print(b, end=' ')
                                                                   
############
def baholash(talabalar):
    baholar = {}
    while talabalar:
        talaba = talabalar.pop()
        baho = int(input(f" Talaba {talaba.title()}ning bahosini qo'ying: "))
        baholar[talaba] = baho
        print(baholar)
    return baholar

talabalar_list = []
print("Talabalar ro'yxatini tuzing:")
while True:
    talaba = input("   Talabaning ism familasini kiriting \
(tugatish uchun 'yes' ni bosing): ")
    talaba = talaba.lower()
    talabalar_list.append(talaba.title())
    if talaba == 'yes':
        talabalar_list.remove('Yes')
        break
talabalar_list.sort()
baholar = baholash(sorted(talabalar_list[:], reverse=True))
#baholar.sorted(reverse=True)
print(baholar)
                                                           

#            MODULLAR
import random as r
x10 = r.sample(list(range(0,1000)),10)
x102 = list(map(lambda x:x**2, x10))
print(f"0 dan 1000 gacha 10 ta tasodifiy son: {x10}")
print(f"Ularning kvadratlari: {x102}")
print(f"Ular ichidagi toq sonlar: {list(filter(lambda so:so%2!=0, x10))}")

son =  int(input("Biror son kiriting (Tub son bo'lsa True, aks holda False'): "))

"""
################################## TUB SONLAR
""" Kiritilgan songacha bo'lgan tub sonlarni aniqlash"""
def tub_son(son, son0):
    t_son=0
    for nn in range(son0, son):
        if son%nn!=0:
            tub_son=0
        else:
            tub_son=1
        t_son += tub_son
    if t_son == 0:
        return True
print("Biror son yoki sonlar oralig'ini kiriting, men sizga shu songacha \
bo'lgan tub sonlarni aniqlab beraman!")
son0 = int(input("Boshlanish nuqtani kiriting: "))
son = int(input("Oxirgi nuqtani kiriting kiriting: "))
print(list(filter(tub_son, range(son0, son))))

index
