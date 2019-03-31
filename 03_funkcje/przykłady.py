# a- argument wymagany, b- nie jest wymagane
def power (a,b=2): # b= 2 żby się kod nie wywalił jak jest power (2), bo brakuje tego argumentu b
    return a**b

print(power(2,4))
print(power (2))



def dzialanie (a,b=2,c=3):
    return a+b+c

print (dzialanie(a= 2, b= 3, c = 1))

def dodaj_jeden (a):
    return a+1
print


def say_hello (name):
    return f"Hello {name}"

def be_awesome (name):
    return "Yo {name}! You are so awesome!"

def greetings (g_func):
    return g_func (name)

print (greetings (be_awesome, "Rafał"))

 b= "B na głownym poziomie"
def parent ():
    a=1
    print ("Printuję z funkcji parent")
    def first_child():
        print ("Printuję z funkcji first_child")
    def second_chiled():
        print #dok...........