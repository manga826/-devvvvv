import string
import random
print("Random Parola Üretici - Black Turtle ")



cevap1 = input("Parolanın İçerisinde Sayı Bulunsun mu ? [E/H]\n")
cevap2 = input("Parolanın İçerisinde Harf Bulunsun mu ? [E/H]\n")
cevap3 = input("Parolanın İçerisinde Özel Karakter Bulunsun mu ? [E/H]\n")


def pwSayi(size = 8, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
def pwHepsi(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))
def pwHarf(size = 8, chars=string.ascii_letters):
	return ''.join(random.choice(chars) for _ in range(size))
def pwOzel(size = 8, chars= string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))
def pwSayiVeHarf(size = 8, chars= string.punctuation + string.ascii_letters):
	return ''.join(random.choice(chars) for _ in range(size))
def pwSayiVeOzel(size = 8, chars= string.punctuation + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


if(cevap1 == "E" and cevap2 == "E" and cevap3 == "E"):
   print(pwHepsi(int(input('Şifreniz Kaç Karakterli Olsun ? | '))))
   print("Sifre olusturulmustur...")

if(cevap1 == "H" and cevap2 == "H" and cevap3 == "H"):
    print("Tuşlama Yapınız..")
    
if(cevap1 == "E" and cevap2 == "H" and cevap3 == "H"):
     print(pwSayi(int(input('Şifreniz Kaç Karakterli Olsun ? | '))))
     print("Sifre olusturulmustur...")

if(cevap1 == "H" and cevap2 == "H" and cevap3 == "E"):
     print(pwOzel(int(input('Şifreniz Kaç Karakterli Olsun ? | '))))
     print("Sifre olusturulmustur...")

if(cevap1 == "E" and cevap2 == "H" and cevap3 == "E"):
     print(pwSayiVeOzel(int(input('Şifreniz Kaç Karakterli Olsun ? | '))))
     print("Sifre olusturulmustur...")

if(cevap1 == "H" and cevap2 == "E" and cevap3 == "H"):
     print(pwHarf(int(input('Şifreniz Kaç Karakterli Olsun ? | '))))
     print("Sifre olusturulmustur...")

if(cevap1 == "E" and cevap2 == "E" and cevap3 == "H"):
     print(pwSayiVeHarf(int(input('Şifreniz Kaç Karakterli Olsun ? | '))))
     print("Sifre olusturulmustur...")
else:
     print("Geçersiz Tuşlama Yapıldı")
