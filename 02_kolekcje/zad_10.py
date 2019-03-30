napis = input( "Wpisz tekst: ")
liczniki = {}

for znak in napis:
    liczniki [znak] = liczniki.get(znak,0) + 1
    
    
print (liczniki)

# zamiast get
#if znak in liczniki:
    #liczniki [znak]+=1
#else:
    #liczniki[znak]=1