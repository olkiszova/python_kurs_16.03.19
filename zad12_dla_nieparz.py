# rozwiązanie zadania 12
i = 0
while i < 100:
    if i % 2 == 0:
        i += 1
        continue
    print(i, "-", i ** 2)
    i += 1

i = 0
while True:
    i += 1
    if i % 9 == 0:
        break  # przerwania- wyjście z pętli

    if i % 5 == 0:
        continue

    print(i)
print("Dalszy kod")
