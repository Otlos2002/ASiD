#zad1
def foo(p_l_imienia, nazwisko):
    return p_l_imienia+'.'+nazwisko
# print(foo('S', 'Otlowski'))

#zad2
def foo2(imie, nazwisko):
    return (str(imie[0])).capitalize() + '.' + (str(nazwisko)).capitalize()
# print(foo2('szymon', 'otlowski'))

#zad3
def foo3(dwie_pier_rok , dwie_ost_rok, wiek):
    temp = int(str(dwie_pier_rok)+ str(dwie_ost_rok))
    if wiek>100:
        return 0
    else:
        return temp-wiek

# print(foo3(20,22,20))

#zad4
def foo4(imie , nazwisko, foot):
    return foot(imie, nazwisko)


def foo4_2(imie , nazwisko):
    return (str(imie[0])).capitalize() + '.' + (str(nazwisko)).capitalize()

# print(foo4('szymon','otlowski',foo4_2))

#zad5
def foo4(arg1, arg2):
    if arg1 > 0 and arg2 > 0 and arg2 != 0:
        return arg1/arg2
    return 0
# print(foo4(2,0.7))

#zad6
# var = 0
# while var < 100:
#     var += int(input("Podaj"))
#     print("Aktualna suma: ", var)
#zad7
def foo7(list):
    return tuple(list)

# print(foo7([1,'w',1,5,5,3,'gff']))

#zad8
def foo8():
    lista = []
    while len(lista)<5:
        lista.append(input("podaj do listy"))
    return tuple(lista)

# print(foo8())

#zad9
def foo9(arg : int):
    dni =['Pon', 'wt','sr','czw','pt','sob','niedziela']
    return dni[arg-1]
# print(foo9(4))
#zad9

#zad10
def foo10(s):
    return s == s[::-1]


s = "malayalam"
ans = foo10(s)

if ans:
    print("Yes")
else:
    print("No")











