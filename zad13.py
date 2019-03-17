#i=0
#suma_temperatur = 0

#while i !=7:
 #   suma_temperatur += float (input("Podaj temperaturę: "))
  #  i = i + 1  # i=+1
   # print(i, suma_temperatur)
#print ("Srednia: ", suma_temperatur, i, suma_temperatur/i)


i = 0
suma_temperatur = 0
while True:
    komenda = input ("Podaj temperturę lub wpisz [k] by zakończyć: ")

    if komenda == 'k':
        break

    suma_temperatur += float (komenda)
    i = i+1
    print (i, suma_temperatur)

print ("Średnia", suma_temperatur, i, suma_temperatur/1)