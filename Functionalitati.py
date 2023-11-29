from Domain.tranzactie import get_id,get_tip,get_suma,get_ziua

def StergeZI(lista):
    """
    Sterge toate tranzactiile de la ziua specifica
    :param id: string
    :param lista: lista de tranzactii
    :return: lista de tranzactii fara tranzactiile din ziua specificata
    """
    zidata = int(input("Alege data de la care vrei sa stergi toate tranzactiile: "))
    found = False
    for tranzactie in lista:
        if get_ziua(tranzactie) == zidata:
            found = True
            lista.remove(tranzactie)
    if found is False:
        print("Nu exista tranzactie in acea zi!")
    return lista

def StergePerioada(lista):
    found=False
    zidata1=int(input("Alege data de la care vrei sa incepi sa stergi toate tranzactiile: "))
    zidata2=int(input("Alege data de la care vrei sa termini de sters tranzactiile: "))
    for tranzactie in lista:
        if zidata1 <= get_ziua(tranzactie) <= zidata2:
            found = True
            lista.remove(tranzactie)
    if found is False:
        print("Nu exista tranzactie in acea perioada!")
    return lista

def StergeTip(lista):
    found=False
    tipdat=input("Alege tipul din care vrei sa stergi tranzactii(iesire/intrare):")
    while tipdat !='intrare' and tipdat != 'iesire':
        print("Tipul trebuie sa fie iesire sau intrare")
        tipdat = input("Alege tipul din care vrei sa stergi tranzactii(iesire/intrare):")

    for tranzactie in lista:
        if get_tip(tranzactie)==tipdat:
            found=True
            lista.remove(tranzactie)

    if found is False:
        print("Nu exista tranzactie in acea perioada!")
    return lista



def TiparesteSumaMaiMare(lista):
    found=False
    sumadata=int(input("Alege o suma minima pentru a arata tranzactii: "))
    for tranzactie in lista:
        if get_suma(tranzactie)>sumadata:
            found=True
            print(tranzactie)
    if found==False:
        print("Nu exista tranzactii cu suma mai mare decat cea data")
    return lista



def TiparesteZISUMA(lista):
    found=False
    zidata=int(input("Alege ziua pentru a afisa tranzactiile efectuate inainte de: "))
    sumadata=int(input("Alege suma minima pentru care sa se afiseze: "))
    for tranzactie in lista:
        if get_ziua(tranzactie)<zidata and get_suma(tranzactie)>sumadata:
            found=True
            print(tranzactie)
    if found == False:
        print("Nu exista tranzactii de genul")
    return lista


def TiparesteTip(lista):
    found=False
    tipdat=input("Alege tipul tranzactiilor(iesire/intrare): ")
    for tranzactie in lista:
        if get_tip(tranzactie)==tipdat:
            found=True
            print(tranzactie)
    if found == False:
        print("Nu exista tranzactii de acest tip!")
    return lista


def SumaTip(lista):
    tipdat=input("Alege tipul(iesire/intrare):")
    sumatip=0
    for tranzactie in lista:
        if get_tip(tranzactie)==tipdat:
            sumatip=sumatip+get_suma(tranzactie)
    print(sumatip)
    return lista

def Sold(lista):
    sold=0
    for tranzactie in lista:
        if get_tip(tranzactie)=='intrare':
            sold=sold+get_suma(tranzactie)
        else:
            sold = sold-get_suma(tranzactie)
    print(sold)
    return lista


def OrdineTip(lista):
    listaNoua=[]
    tipdat=input("Alege tipul:")
    for tranzactie in lista:
        if get_tip(tranzactie)==tipdat:
            listaNoua.append(tranzactie)
    listaNoua.sort(key=lambda tranzactie: tranzactie["suma"])
    for tranzactie in listaNoua:
        print(tranzactie)
    return lista

def EliminaTip(lista):
    tipdat=input("Alege tipul de tranzactii ce vrei sa fie eliminate din lista: ")
    print("Vor ramane tranzactiile:")
    for tranzactie in lista:
        if get_tip(tranzactie)!=tipdat:
            print(tranzactie)

    return lista


def EliminaTipSuma(lista):
    tipdat=input("Alege tipul ce vrei sa il afisezi: ")
    sumadata=int(input("Alege o suma: "))
    print("Vor ramane tranzactiile: ")
    for tranzactie in lista:
        if get_tip(tranzactie)==tipdat and get_suma(tranzactie)<sumadata:
            print(tranzactie)
    return lista