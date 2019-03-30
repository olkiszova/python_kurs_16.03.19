napis = input ("Podaj zdanie: ")

samogloski = "aeiouy" # to samo co samogloski ('a', 'e', 'i', 'o', 'u', 'y')
licznik = 0


for litera in napis.lower(): #dla małych liter
    if litera in samogloski:
        licznik += 1

print(f" W tekście: '{napis}' jest {licznik} samogłosek")




#Inny sposób, dłuższy

zdanie = str(input("Podaj zdanie: "))
a = "a"
A = "A"
e = "e"
E = "E"
i = "i"
I = "I"
o = "o"
O = "O"
u = "u"
U = "U"
Y = "Y"
y = "y"

acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0
ycount = 0

if A or a in zdanie :
     acount = acount + 1

if E or e in zdanie :
     ecount = ecount + 1

if I or i in zdanie :
    icount = icount + 1

if o or O in zdanie :
     ocount = ocount + 1

if u or U in zdanie :
     ucount = ucount + 1

if y or Y in zdanie :
    ycount = ycount + 1

print(acount, ecount, icount, ocount, ucount, ycount)