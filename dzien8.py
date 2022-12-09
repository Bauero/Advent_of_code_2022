#https://adventofcode.com/2022/day/8

#poznanie szerokości i wysokości naszego lasu
f = open("input8.txt","r")
linijka = f.readline()
szerokosc = len(linijka)
lista_danych = [list(linijka.rstrip().lstrip())]
wysokosc = 1
for i in f:
    wysokosc+=1
    lista_danych.append(list(i.rstrip().lstrip()))
f.close()

ilosc_dobrych_drzew = 0

for i in range(len(wysokosc)):
    for j in range(len(szerokosc)):

        #element znajduje się na krawędzi
        if i == 0 or i == len(lista_danych) or j == 0 or j == len(lista_danych[i]):
            continue
        else:
            #przetestowanie widoczności we wszystkich kierunkach

