wymiary = input ("Podaj wymiary rozdzielając je przecinkiem: ")
a,b,c = wymiary.split(",")
a, b, c = int(a), int(b), int(c)
objetosc = a*b*c
print("Czy objetosc większa od 1 l?", objetosc > 1000)

if objetosc < 1000: # jesli jest true to kolejna linia jest wykonana
    print("Objetosc jest mniejsza niz 1 litr")
if objetosc == 1000:
    print("To jest 1 litr")
else:
    print("Objetosc jest wieksza niz 1 litr")