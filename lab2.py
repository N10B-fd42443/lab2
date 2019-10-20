import sys

print("Witaj w Kalkulatorze \n 1. Dodawanie \n 2. Odejmowanie \n 3. Mnozenie \n 4. Dzielenie \n 0. Wyjdz"  )
x = input("Wprowadz wybor: ")
if x == 0:
    print('Do widzenia!')
    sys.exit()
a = input("Wprowadz liczbe a: ")
b = input("Wprowadz liczbe b: ")
a = float(a)
b = float(b)
if x == 1:
    print('Wynik = ', a+b)
if x == 2:
    print('Wynik = ', a-b)
if x == 3:
    print('Wynik = ', a*b)
if x == 4:
    if b == 0:
        print('Blad! Nie mozna dzielic przez 0')
    else:
        print('Wynik = ', a/b)


