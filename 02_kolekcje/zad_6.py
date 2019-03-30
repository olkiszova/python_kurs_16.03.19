liczby = [5, 2, 1, 4, 3] #wynik powinien być [1, 2, 5, 4, 3]


#Tu bedziemy modyfikować liczby


i_min = liczby.index(min(liczby))
i_max = liczby.index(max(liczby))
liczby [i_min], liczby [i_max]= liczby [i_max], liczby [i_min] # ta linijka jest za linijki 15,16,17
print (i_max, i_min)

print (liczby[i_max], liczby[i_min])


#temp = liczby [i_min] #1
#liczby [i_min] = liczby [i_max] # tam gdzie 1 wrzucam 5
#liczby [i_max] = temp #tam gdzie 5 wrzucam 1

assert liczby == [1, 2, 5, 4, 3] #asert to taki test do sprawdzania kodu


#sposób Dominiki
a= min(liczby)
b=max(liczby)
poz_a = liczby.index(a)
poz_b = liczby.index (b)

liczby.remove (a)
liczby.insert (poz_a, b)
liczby.remove (b)
liczby.insert (poz_b, a)

print (liczby)


#kolejny sposób

#symulujemy działanie maks i min - tu są zapisywane wartości

temp_max = liczby [0]
temp_min = liczby [0]

for el in liczby:
     if el > temp_max:
         temp_max = el
     elif el < temp_min:
         temp_min = el

#teraz chcemy indeks - ale bez użycia metody index
for el in range (len(liczby)):
     if liczby [el] > temp_max:
         temp_max_i = liczby [el]
         temp_max_i = el
     elif liczby [el] < temp_min:
         temp_min = liczby [el]
         temp_min_i = el

#enumerate
for i, v in enumarate (liczby):
    print (i, v)
