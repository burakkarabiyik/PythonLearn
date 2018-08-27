# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:05:59 2018

@author: Burak KARABIYIK
"""


import pandas as pd

dataset=pd.read_csv("iris.csv")


#%% Pandas Kütüphanesi

"""
    Veri analizi ve veri ön işlemeyi kolaylaştıran  açık kaynak kodlu bir kütüphanedir
"""



import pandas as pd

dataset=pd.read_csv("iris.csv")

dataset.head() # komutu ile ilk 5 elemanı getirir

sec= pd.read_csv('iris.csv', usecols=['SepalLengthCm','SepalWidthCm']) # Belirli Sutunları okumak için

dataset.columns #kolonları getirir
"""
kolon ismi değiştirmek için 

Kolonisimleri=["col1","col2"]
dataset.columns=kolonisimleri
                                 işlemi yapılmalıdır

"""
dataset["SepalLengthCm"] # Sutun seçmek için kullanılır.

dataset.dtypes # kolonların data tiplerini yazdırır


# dataset.rename(columns ={'Sehir':'Sehir_Yeni'},inplace=True) kolonu yeniden adlandırmak için kullanılır. 
# inplace olmazsa etkilemez sadece geriye döndürür

print(dataset.Species.unique()) # species kolonunu unique bir şekilde ekrana basar

setosa =dataset[dataset.Species=="Iris-setosa"] # Sadece setosa olanları alır Kolon seçilir

print(setosa.describe()) # Dataframe i açıklar [ kaç tane olduğu ,ortalaması ,en büyük en küçük değer gibi]

#%% 


import pandas as pd

dataset=pd.read_csv("iris.csv")
import matplotlib.pyplot as plt
d1=dataset.drop(["Id"],axis=1)
d1.plot(grid=True)  # Görselleştirme yapar 
plt.show() ## Çalışması için Tools>Preferences>IPython Console>Graphics Backend Automatic seçilmeli.Seçtikten sonra spyder kapatılıp açılmalı


#%%



import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("iris.csv")

setosa=dataset[dataset.Species=="Iris-setosa"]  ## Species kolonunu seçip setos olanları al
versicolor=dataset[dataset.Species=="Iris-versicolor"] # versicolorları al
virginica=dataset[dataset.Species=="Iris-virginica"]   # virginicaları al

plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa",alpha=0.3) # Alpha saydamlık veriyor.
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label="virginica")

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()


