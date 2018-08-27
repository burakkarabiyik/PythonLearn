# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:06:08 2018

@author: Burak KARABIYIK
"""



#%% numpy array  kullanımı

import numpy as np

"""
    Array bir liste aracıdır. Kullanımı kolaylaştırır.
"""
arrayy=np.array([[1,3],[2,4]]); # iki boyutlu matris oluşturduk

print(arrayy,"\n") #Matrisi yazdık
print(arrayy[:,1]) # 2. sütunu yazdırdık
print(arrayy[1,:]) #2. satırı yazdırdık

print(arrayy.mean(axis=0)) ## Sütun ortalaması 
print(arrayy.mean(axis=1),"s") ## Satır ortalaması
arrayy.sort() ## listeyi siralamak için kullanılır
print(arrayy," Sıralı Dizi")
print(arrayy.min()) #minimum sayıyı getirir
print(arrayy.max()) #maksimum sayıyı getirir


sifir=np.zeros((2, 512*512), dtype=np.float32) # 2 satır 512*512 sutundan oluşan bir sıfır matrisi oluşturur. 
#Bellekte yer ayırmak gibi . Programın çalışma hızını arttırmak için kullanılmakta



#%% numpy rasgele sayı
import numpy as np

rastgele=np.random.randint(1,100,3) # integer tipinde yani tamsayı 1-100 arasında 3 tane rasgele tamsayı üretir


rastgelematris=np.random.randint(5, size=(2, 4)) # 2:4 boyutunda bir matris. Maksimum 5 değeri alabilmekte






#%% numpy hstack ve vstack

import numpy as np

matris1=[0,2]
matris2=[3,6]

matris3=np.hstack((matris1,matris2)) ## Yatay olarak iki diziyi birleştirir
matris4=np.vstack((matris1,matris2)) ## Dikey olarak iki diziyi birleştirir

#%% numpy Matematiksel işlemler

import numpy as np

np.mean([5,4]) # ortalama

np.cos(0) 
np.sin(0)

np.sqrt(4) # karekök

np.square(100) # Karesi

np.power(2,4) # 2^4

np.power(16,1/4) # 2^1/4 


