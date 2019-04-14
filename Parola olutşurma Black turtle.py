import random

print("BLACK TURTLE - PAROLA URETICI")

print("NOT : Bu parola üretme programi sadece 5 haneli parolalar üretmektedir. :)")

harfsoru = input("Parola içersinde harf Olsunmu e/h :")


sayisoru = input("Parola içersinde sayi Olsunmu e/h :")


karaktersoru = input("Parola içersinde krakter olsunmu e/h :")






karakter2 = ['!','@','$','%','^','&','*','(',')','_','+','\'']

sayi2 = ['0','1','2','3','4','5','6','7','8','9']


harfler2=['A','B','C','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z']


sayi = 0
sayiasd = 0
sayi3 = 0

while sayi <= 100:

     sayi+= 1
     if harfsoru == "e":    
      print(random.choice(harfler2), end ="")
      print(random.choice(harfler2), end ="")
      print(random.choice(harfler2), end ="")
      print(random.choice(harfler2), end ="")
      print(random.choice(harfler2), end ="")
     
           
     break



    

while sayiasd <= 100:

     sayiasd+= 1
     if sayisoru == "e":    
      print(random.choice(sayi2), end ="")
      print(random.choice(sayi2), end ="")
      print(random.choice(sayi2), end ="")
      print(random.choice(sayi2), end ="")
      print(random.choice(sayi2), end ="")
    
      
     break
    


    


while sayi3 <= 100:
     sayi3+= 1
     if karaktersoru == "e":
      
       print(random.choice(karakter2), end ="")
       print(random.choice(karakter2), end ="")
       print(random.choice(karakter2), end ="")
       print(random.choice(karakter2), end ="")
       print(random.choice(karakter2), end ="")
    
      
     break
    

     


    


    
"""if (harf == "e"):
    
 
         parola.append(alfabe2)

    
         


if (sayi == "e"):
 
         parola.append(sayi2)
         
       
         

if (karakter == "e"):
    parola.append(karakter2)
    
    for i in parola:
     random.uniform()
     print(i, end="")

else:

    for i in parola:  

     print(i, end="")"""
     


    




    

