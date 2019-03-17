liczby = input ("Podaj 2 liczby rozdzielając je przecinkiem: ")
a,b = liczby.split(",")
a,b = int(a), int(b)
Operacja = input("Podaj rodzaj operacji: ")
if Operacja == "+":
    print(a + b)
elif Operacja == "*":
    print(a * b)
elif Operacja == "/":
    if b==0:
        print ("Nie dziel przez 0!")
    else:
        print(a / b)
elif Operacja == "-":
    print(a - b)
elif Operacja == "**":
    print(a ** b)
elif Operacja == "%":
    print(a % b)
else:
    print("Nieprawidłowa operacja")