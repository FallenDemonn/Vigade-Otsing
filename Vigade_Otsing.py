from ctypes.wintypes import INT
import math #не правильно импортирован модуль
print("Ruudu karakteristikud")
a = float(input("Sisesta ruudu külje pikkus: ")) #не назначен тип
S = a ** 2
print("Ruudu pindala", S)
P = 4*a
print("Ruudu ümbermõõt", P)
di = a*math.sqrt(2) #не правильная функция(не дописана)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b = float(input("Sisesta ristküliku 1. külje pikkus => "))
c = float(input("Sisesta ristküliku 2. külje pikkus => "))
S = b * c
print("Ristküliku pindala", S)
P = 2*(b + c)
print("Ristküliku ümbermõõt", P)
di = math.sqrt((b**2)+(c**2))
print("Ristküliku diagonaal", round(di,2)) #не дано количество цифр после ","
print()
print("Ringi karakteristikud") #лишняя скобка
r = float(input('Sisesta ringi raadiusi pikkus => ')) #не назначен тип
d = 2 * r
print("Ringi läbimõõt", d)
S = math.pi * r ** 2 #не правильное возведение в степень
print("Ringi pindala", round(S,2)) #не дано количество цифр после ","
C = 2* math.pi * r 
print("Ringjoone pikkus", round(C,2)) #не дано количество цифр после ","


