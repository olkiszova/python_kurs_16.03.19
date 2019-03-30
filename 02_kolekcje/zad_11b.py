dane = input ("Podaj liczby rodzielając je przecinkiem")
unikalne_liczby = {int(el) for el in dane.split(",")}


print (f"Unikalnych liczb: {len(unikalne_liczby)}")
print (f"Z czego parzystych w przedaile 0-100 jest {len(unikalne_liczby & set(range(0,101,2)))}")