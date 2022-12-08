#https://adventofcode.com/2022/day/8

#poznanie szerokości i wysokości naszego lasu
f = open("input8.txt","r")
szerokosc = len(f.readline())
wysokosc = 1
for i in f:
    wysokosc+=1
f.close()
print(szerokosc,wysokosc)
