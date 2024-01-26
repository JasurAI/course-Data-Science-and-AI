# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:54:32 2024

@author: Jasur
"""
import random as r

def son_topish(t_son):
    k=0
    shart=True
    while shart:
        k+=1
        if t_son==o_son:
            print(f">>> To'g'ri topdingiz, barakalla! Siz buni {k}-urinishda amalga oshirdingiz.")
            shart=False
        elif t_son>o_son:
            t_son = int(input(f">>> Xato! Men o'ylagan son {t_son} dan kichikroq. Yana urinib ko'ring: "))
        elif t_son<o_son:
            t_son = int(input(f">>> Xato! Men o'ylagan son {t_son} dan kattaroq. Yana urinib ko'ring: "))
    return k

            
def son_topaman(n):
    i=0
    a = 1
    shart = True
    while shart:
        i+=1
        son = r.randint(a, n)
        natija = input(f">>> Siz o'ylagan son {son}. To'g'ri (T), men o'ylagan son bundan katta (+), bundan kichik (-): \n>>>")
        if natija.upper()=="T":
            print(f">>> Men siz o'ylagan sonni {i}-urinishda topdim")
            shart = False
        elif natija == "+":
            a = son+1
        elif natija == "-":
            n = son-1
        else:
            continue
    return i


##############     START FINDING NUMBER GAME



print("          START FINDING NUMBER GAME\n         O'YLAGAN SONNI TOPISH O'YINI")
shart = True
m=0
s=0
while shart:
    n = int(input("     \n>>> O'yin uchun son chegarasini kiriting: "))
    boshlash = int(input("\n>>> O'yinni kim birinchi boshlaydi: Siz (1), men (0) : "))
    if boshlash==1:
        print(f"\n>>> 1 dan {n} gacha oraliqda bir son o'ylang men esa uni topishga harakat qilaman!")
        input(">>> Son o'ylagan bo'lsangiz bosing 'Enter': ")
        men_urinishim = son_topaman(n)
        
        print(f"\n>>> 1 dan {n} gacha bir son o'yladim. Bu sonni topishga urininb ko'ring!")
        o_son = r.randint(1, n)
        t_son = int(input(">>> Sizningcha bu son nechchi, uni kiriting: \n>>> "))
        siz_urinishingiz = son_topish(t_son)
        
    else:
       print(f"\n>>> 1 dan {n} gacha bir son o'yladim. Bu sonni topishga urininb ko'ring!")
       o_son = r.randint(1, n)
       t_son = int(input(">>> Sizningcha bu son nechchi, uni kiriting: \n>>> "))
       siz_urinishingiz = son_topish(t_son)
       
       print(f"\n>>> 1 dan {n} gacha oraliqda bir son o'ylang men esa uni topishga harakat qilaman!")
       input("\n>>> Son o'ylagan bo'lsangiz bosing 'Enter': ")
       men_urinishim = son_topaman(n)
       
        
    if men_urinishim<siz_urinishingiz:
        m += 1
    if men_urinishim>siz_urinishingiz:
        s += 1
    if men_urinishim==siz_urinishingiz:
        m += 0
        s += 0
    print(f"Meni urinishim-{men_urinishim},   Sizning urinishingiz-{siz_urinishingiz}")
    print(f"\n>>> Menda - {m} achko,  Sizda - {s} achko")
    davom_etish = input("\n>>> O'yinni davom ettirishni hoxlaysizmi, Ha (1), Yoq (0) : ")
    
    if davom_etish==1:
        shart = True
    else:
        if m>s:
            print(f"\n>>> Men sizni {m}:{s} hisobida yutdim")
        elif m<s:
            print(f"\n>>> Siz meni {s}:{m} hisobida yutdingiz. Tabriklayman !")
        elif m==s:
            print(f"\n>>> Biz {m}:{s} hisobida durang o'ynadik. Tabriklayman mos raqib bo'ldingiz !")
    
        shart=False


        
    