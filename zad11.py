x = input ("Podaj pozycję gracza x: ")
y = input ("Podaj pozycję gracza y: ")

if (0 > x > 100) or (0 > y > 100):
    print("Jesteś poza planszą frajerze")
elif  x >= 90 and y >= 90:
    print("Jesteś w GPR")
elif  x >= 90 and y <= 10:
    print("Jesteś w DPR")
elif x >= 90 and y >= 90:
    print("Jesteś w DPR")
elif x <= 10 and