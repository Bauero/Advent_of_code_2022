f = open("input13.txt","r")

surowe = []

for i in f:
    if i != "\n":
        surowe.append(eval(i.lstrip().rstrip()))
        nowe.append(i.lstrip().rstrip().replace("[]","X").replace('[','').replace(']',''))

for i in range(len(surowe)):
    if type(surowe[i]) != list:
        surowe[i] = list(i)

lewe = [surowe[i] for i in range(0,len(surowe),2)]
prawe = [surowe[i] for i in range(1,len(surowe),2)]

for l_lista,r_lista in lewe,prawe:
    

def nast_elem(lista):
    