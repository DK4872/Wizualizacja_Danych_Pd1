# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne
import math
napis = 'Ciekawe zdanie'
print('Zadanie 1')
a = 14

print(napis)
print(a)

#Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
print('Zadanie 2')
a=1
b=2

dodawanie = a + b
print('a+b=')
print(dodawanie)

odejmowanie = a - b
print('a-b=')
print(odejmowanie)

mnozenie = a * b
print('a*b=')
print(mnozenie)

dzielenie = a / b
print('a/b=')
print(dzielenie)

potega = a ** b
print('a^b =')
print(potega)

#Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
print('Zadanie 3')
c = 1
c += 1
print(c)

c -= 1
print(c)

c *= 1
print(c)

c /= 1
print(c)

c **= 1
print(c)

c %= 1
print(c)

#Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
print('Zadanie 4')
e = 2
bb = e
bbb = (e)**10
print(bbb)
cc = math.log(5 + math.sin((8)**2))
ccc = math.pow(cc,1/6)
print(ccc)
print("math.floor(3.55) : ", math.floor(3.55))
print("math.ceil(4.80) : ", math.ceil(4.80))


#Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody capitalize)
print('Zadanie 5')
i = "DOMINIK"
n = "KORZENIECKI"

print(i.capitalize() + " " + n.capitalize())

#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)
print('Zadanie 6')
piosenka = "Tra la la la la, ha ha ha"
t = "Ilosc la:"
z = piosenka.count("la")
print(t,z)
#Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu. Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0]. Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
print('Zadanie 7')
napis2: str = "Niesamowity"
print(napis2)
print("Druga litera =" + " " + napis2[1])
print("Przedostatnia litera =" + " " + napis2[9])
#Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy. (trzeba użyć metody split)
print('Zadanie 8')
print(piosenka.split(' '))
#Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie wyświetl je wykorzystując odpowiednie formatowanie.
print('Zadanie 9')
s = '10.5674'
print(type(s))
print('String =', s)
f = float(s)

print(type(f))
print('Float =', f)

h = 0xff
print('Hex =', h)




