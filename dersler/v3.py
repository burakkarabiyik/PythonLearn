# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 16:55:54 2018

@author: Burak KARABIYIK
"""

#%% OOP-- Sınıf  --Nesneye Dayalı Programlama

"""
    Programlamayı kolaylaştırmak adına sınıflandırma kullanılmaktadır. 
    Her bir nesnenin özellikleri ve fonksiyonları vardır.
    Her sınıfın olmazsa olmazsı kurucu fonksiyonu vardır.    
"""


class Calisan:
    
    Calisansayisi=0
    
    def __init__(self,Ad,Soyad):
        self.Ad=Ad
        self.Soyad=Soyad
        Calisan.Calisansayisi+=1
    
    def calisansayisigetir():
        return Calisan.Calisansayisi
    


calisan1=Calisan("Ali","A")
print(Calisan.calisansayisigetir()) ## Calışan sayısını geriye döndürür
calisan1=Calisan("Ahmet","B")
print(Calisan.calisansayisigetir())
calisan1=Calisan("Veli","C")
print(Calisan.calisansayisigetir())
calisan1=Calisan("Cenk","D")
print(Calisan.calisansayisigetir())
  
## 4 tane çalışanımız var bu çalışanların isimlerine soyadına kaç çalışanımız var kolayca ulaşabilmekteyiz. 
