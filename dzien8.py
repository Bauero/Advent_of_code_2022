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

for i in range(wysokosc):
    for j in range(szerokosc-1):

        #element znajduje się na krawędzi
        if i == 0 or i == wysokosc-1 or j == 0 or j == szerokosc-1:
            continue
        else:
            #przetestowanie widoczności we wszystkich kierunkach

            #na boki
            if j > 1 and j+2 < szerokosc:

                #sprawdzanie po lewej
                if not max(lista_danych[i][0:j-1]) >= lista_danych[i][j]:
                    continue 

                #sprawdzanie po prawej
                if not max(lista_danych[i][j+1:]) >= lista_danych[i][j]:
                    continue
            

            kolumna = [lista_danych[x][j] for x in range(0,wysokosc-1)]

            #sprawdznanie w pionie
            if i > 1 and i+2 < wysokosc:

                #w górę
                if not max(kolumna[0:i-1]) >= lista_danych[i][j]:
                    continue
                
                #w dół
                if not max(kolumna[i+1:]) >= lista_danych[i][j]:
                    continue
            
            kopia_lista_danych[i][j] = "*"
            ilosc_dobrych_drzew += 1

print("Ilość dobrych drzew to: ",ilosc_dobrych_drzew)

f = open("wynik8.txt","w")
for i in range(wysokosc):
    napis = ""
    for j in range(szerokosc-1):
        napis+=str(kopia_lista_danych[i][j])
    f.write(napis + "\n")

f.close()