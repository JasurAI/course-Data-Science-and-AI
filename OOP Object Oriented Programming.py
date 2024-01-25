# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:31:42 2023
@author: Jasur Mamarakhimov
"""
import pandas as pd
import numpy as np
#########        Web sahifa uchun foydalanuvchi klassi
"""
class User:
    #Web sahifa uchun foydalanuvchi klassi
    def __init__(self, ism,familiya,t_yil,email,mob_number):
        #Foydalanuvchi xususiyatlari
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.email = email
        self.mob_number = mob_number
    
    def get_name(self):
        return self.ism
    def get_familiya(self):
        return self.familiya
    def get_age(self, yil):
        return yil-self.t_yil
    def get_info(self):
        #Foydalanuvchi ma'lumotlari
        print(f"Foydalanuvchi ismi: {self.ism} \n Familiyasi: {self.familiya} \n \
Yoshi: {self.get_age(2023)} \n Emaili: {self.email} \n Mobil numberi: {self.mob_number}")

#user1 = User(input("Ismingiz: "), input("Familyangiz: "), int(input("Tug'ilgan yilingiz: ")), input("Emailingiz: "), input("Mobil number: "))


###############       AVTO  

class Avto:
    def __init__(self, model, rang, karobka, narx, yili):
        #Avtomobil haqida ma'lumotlar
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.yili = yili
        self.probeg = 0
        
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_karobka(self):
        return self.karobka
    
    def get_narx(self):
        return self.narx
    
    def get_yili(self):
        return self.yili
        
    def get_info(self):
        return f" Modeli: {self.model} \n Rangi: {self.rang} \n Karobkasi: {self.karobka} \
\n Narxi: {self.narx} $ \n Ishlab chiqarilgan yili: {self.yili}-yil \n Probeg: {self.probeg} km"
    
    def set_probeg(self, probeg):
        self.probeg = probeg
        
    def update_probeg(self):
        self.probeg += 0


class Avtosalon:
    def __init__(self, salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtolar = []
        self.avtolar_soni = 0
        
    def add_avto(self, avto):
        self.sotuvdagi_avtolar.append(avto)
        self.avtolar_soni += 1
        
    def get_avtolar(self):
        return [avto.get_info() for avto in self.sotuvdagi_avtolar]

#file = open('pay.txt')        
with open('pay.txt') as file:
    pr = file.read()

salon = Avtosalon("Toshkent avtosalon", "Toshkent sh., Yunusobod tum., Amir Temur ko'chasi, 50-uy")
avto1 = Avto("Lacetti", "oq", "Avtomat", "15000", "2022")
pr = pr.rstrip()
pr = pr.replace('\n', '')
pr = float(pr)
avto1.set_probeg(pr)
avto1.update_probeg()
avto2 = Avto("Gentra", "qora", "Avtomat", "13000", "2020")
avto3 = Avto("Damas", "qaymoq", "Mexanik", "7000", "2021")
avto4 = Avto("Cobalt", "qizil", "Mexanik", "12000", "2022")
avto5 = Avto("malibu 2", "qora", "Avtomat", "35000", "2023")
salon.add_avto(avto1)
salon.add_avto(avto2)
salon.add_avto(avto3)
salon.add_avto(avto4)
salon.add_avto(avto5)
print(salon.get_avtolar())                       """


import torch
h = [1,2,3]
g = [2,4,6]
w = torch.tensor([1.0], requires_grad=True) #Taxminiy qiymat

def xw(x):
    return x*w

def loss(x,y):
    y_pred = xw(x)
    return (y_pred-y)**2

#def grad(x,y):
#    return 2*x*(x*w-y)

print("Traningdan avvalgi qiymat: x=4 uchun y=", xw(4))

l_rate=0.01
for qiymat in range(1,10):
    for x_qiymat, y_qiymat in zip(h,g):

        l = loss(x_qiymat,y_qiymat)
        l.backward()
        print("\tgrad:", x_qiymat, y_qiymat, '{:.3f}'.format(w.grad.item()))
        w.data = w.data - l_rate*w.grad.item()
        w.grad.data.zero_()
           
    print(qiymat,"-progress:", "loss=", '{:.3f}'.format(l.item()))
    
#print("Traningdan keyingi qiymat: x=9 uchun y=", xw(9))
print("Traningdan keyingi qiymat: x=4 uchun y=", '{:.3f}'.format(xw(4).item()))
        
