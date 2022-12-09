#https://adventofcode.com/2022/day/8
import copy

#poznanie szerokości i wysokości naszego lasu
f = open("input8.txt","r")
linijka = f.readline()
szerokosc = len(linijka)
lista_danych = []
lista_danych.append([int(x) for x in list(linijka.rstrip().lstrip())])
wysokosc = 1
for i in f:
    wysokosc+=1
    lista_danych.append([int(x) for x in list(i.rstrip().lstrip())])
f.close()

kopia_lista_danych = copy.deepcopy(lista_danych)

ilosc_dobrych_drzew = 0

for r in range(1,wysokosc-1):
    for k in range(1,szerokosc-2):

        obecny_element = lista_danych[r][k]

        lewo = lista_danych[r][:k]
        prawo = lista_danych[r][k+1:]
        kolumna = [lista_danych[x][k] for x in range(wysokosc)]
        gora = kolumna[:r]
        dol = kolumna[r+1:]
        
        #print("Lewo ",lewo)
        #print("Prawo ",prawo)
        #print("Góra ",gora)
        #print("Dół ",dol)


        if max(lewo) < obecny_element or max(prawo) < obecny_element \
            or max(gora) < obecny_element or max(dol) < obecny_element:
            continue

        ilosc_dobrych_drzew +=1

        kopia_lista_danych[r][k] = "*"

f = open("wynik8.txt","w")

for i in kopia_lista_danych:
    napis = ""
    for j in range(len(i)):
        napis += str(j)
