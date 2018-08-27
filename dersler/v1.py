# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:59:24 2018

@author: Burak Karabıyık
"""

#%% Değişkenler 

isim="Burak" ## karakter dizisidir. String (str)
yas=25 ## Tamsayılar için kulllanılır  integer (int)
floatt=10.0 ## ondalıklı sayılar için kullanılır....  float

z=1j # kompleks değişken
## bu iki değişken farklıdır çift tırnak içindeki bir karakter dizisidir diğeri sayıdır
abc=44
abcd="44"

#%%

a=5
b=10
c="Ahmet"
d="Mehmet"
print(a+b) ## Sayıları toplayacaktır
print(c+d) ## iki stringi birleştirip ekrana yazacaktır
#print(a+c) ##string ve int değerini toplamaya çalışırsak hata verecektir
print(a,c) ## şeklinde hata vermeyip arada bir boşlukla ekrana yazacaktır

#%% Operatörler
"""
Matematiksel işlemleri yapmak için kullanıyoruz

"""
x=50
y=10
print(x+y)
print(x-y)
print(x*y)
print(x/y)


#%% for

for i in range(1,101,20): ## 1 den başla 101 e kadar 20şer art
    print(i)
    
    
    

#%% while loops
i=0  
while i<10: ## 0 dan başla 10a kadar 1er arttır ekrana yaz
    print(i)
    i+=1
    
    
    
#%% String
    
isim = "BURAK KARABIYIK"
print(isim)
print(isim[0:5])
print(isim[6:])


#%% List

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = list(("apple", "banana", "cherry", "banana"))
thislist.append("damson")
thislist.remove("apple")
print(thislist)
print(thislist.count("apple")) #listedeki apple sayısı
print(thislist.count("banana")) #listedeki banana sayısı
print(len(thislist)) #listedeki eleman sayısı
print(thislist[0]) ## ilk elemana erişmek için index i  ile ulaşıyoruz
## ilk elemanı silmek için 
thislist.pop(0)
print(thislist[0]) ## ilk elemanın değiştiğini görüyoruz

#%% Tuple
"""
Listeye benziyor ama daha az fonksiyonlu
"""
yenilist=("a","b,","c")

print(yenilist)


#%% Sets

"""
    Listeye benziyor farkı sırasız karışık.
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)

#%% Dictionary

"""
    Küçük bir veritabanı yada küçük bir sözlük için kullanışlı
"""
sozluk={
        "isimler":["Ali","Veli","Ahmet"],
        "Yaslar":[32,23,19],
            }
print(sozluk["isimler"])
print(sozluk["Yaslar"])

## Ekleme işlemi
sozluk["Soyadlar"]=["A","B","C"]
print(sozluk["Soyadlar"])

## Çıkarma işlemi
del(sozluk["Soyadlar"])

## uzunluk için len komutu
print(len(sozluk))

#%% if-else

i=5

if i<3:
    print("kucuk")
elif i<5:
    print("orta")
elif i<7:
    print("büyük")
else:
    print("Hata")

#%% Fonksiyonlar
"""
    Fonksiyonlar tekrar tekrar kod yazmamamız için tek bir kod dizisi oluşturarak
    sadece onu çağırarak kolayca işlemimizi yapmayı sağlıyor.
"""
def my_function(i): ##  sayının karesini almamızı kolaylaştıran fonksyion
  return i

cevap=my_function(7)
print(cevap)


## Varsayılan Fonksiyon elemanı
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") 
my_function() ## Parametre vermesekte olur. Varsayılan olarak içerisinde tanımlı

## Degişken fonksiyon parametresi
def my_function(x,*arg):
    print(arg)
    return 5 * x

(my_function(3))
(my_function(3,55))
(my_function(3,5,7,9))

#%% Lambda

"""
    Az satırlı fonksiyon oluşturmak için hızlı güzel bir yol
    Aşağıdaki 2 gösterimde aynı sonuç verecektir.
"""
def function(a,b): 
    return a+10

x = lambda a,b : a + b
print(x(5,10))
print(function(5,10))


#%% Modul import etmek

import moduldeneme as md ## ismini kısaltmak için as kullandık

md.denemefonk()



#%% Tarihlere erişmek

import datetime

x = datetime.datetime.now()
print(x)

print(x.year)

print(x.day)
print(x.month)
## Tarih oluşturma
print()## boşluk
yenitarih = datetime.datetime(2020, 5, 17)

print(yenitarih.year)

print(yenitarih.day)
print(yenitarih.month)


#%% Try except
"""
    Hata ile karşılaşılırsa ne yapılacağı tanımlanır
"""

try:
  print(x)
except:
  print("Hata değişken tanımlanmadı")
x=5

try:
  print(x)
except:
  print("Hata değişken tanımlanmadı")
    
