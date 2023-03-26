import random
import string

uzunluk = int(input('Şifre uzunluğunu giriniz : '))
adet = int(input("Kaç adet şifre üretmek istiyorsunuz: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

for i in range(0,adet):
    all = lower + upper + num + symbols
    temp = random.sample(all, uzunluk)
    password = "".join(temp)
    print(password)

