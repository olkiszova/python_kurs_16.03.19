def formatuj(*args, **kwargs):
    print(kwargs)
    print(args)
    zlaczone = "\n.join(args)"

    for k in kwargs:
        zlaczone.replace(f"${k}", str(kwargs[k]))
        return zlaczone



def test_formatuj():
    x = formatuj(
        'koszt $cena PLN',
        'kwota $brutto brutto',
        cena=10,
        brutto=12.3,
    )
    assert x == "koszt 10 PLN\n nkwota 12.3 brutto"
