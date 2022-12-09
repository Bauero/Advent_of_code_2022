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

