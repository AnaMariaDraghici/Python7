from Domain.tranzactie import toString
from Logic.CRUD import AdaugaTranzactie, ModificaTranzactie
from Logic.Functionalitati import StergeZI, StergePerioada, StergeTip, TiparesteSumaMaiMare, TiparesteZISUMA, TiparesteTip,SumaTip, Sold,OrdineTip, EliminaTip, EliminaTipSuma

def printMenu():
    print("1.Adaugare de noi tranzactii")
    print("2.Stergere")
    print("3.Cautari")
    print("4.Rapoarte")
    print("5.Filtrare")
    print("6.Afisare tranzactii")
    print("x.Iesire")
    print("y.Undo")

def uiAdaugaTranzactie(lista):
    try:
        id = input("Introduceti ID-ul tranzactiei: ")
        ziua = input("Introduceti ziua in care s-a efectuat tranzactia: ")
        suma = float(input("Introduceti suma tranzactionata: "))
        tip = input("Introduceti tipul tranzactiei(intrare/iesire): ")
        return AdaugaTranzactie(id,ziua,suma,tip,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaTranzactie(lista):
    try:
        id = input("Dati ID-ul tranzactiei ce vreti sa o modificati: ")
        ziua = input("Dati ziua noua a tranzactiei: ")
        suma = input("Dati suma noua a tranzactiei: ")
        tip = input("Dati tipul nou a tranzactiei: ")
        return ModificaTranzactie(id,ziua,suma,tip,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ShowAll(lista):
    for tranzactie in lista:
        print(toString(tranzactie))

def runMenu(lista):
    while True:
        printMenu()
        optiune=input("Dati optiunea: ")
        if optiune == "1":
            print("Adaugare de noi tranzactii:")
            print("1a. adauga tranzactie(se da ziua, suma, tipul)")
            print("2a. actualizare tranzactie(se da noua zi, suma sau tip)")
            moglich=input("Alege care dintre optiunile de adaugare doresti sa o folosesti: ")
            if moglich=='1a':
                lista = uiAdaugaTranzactie(lista)
                print("Tranzactia a fost adaugata! Poti verifica apasand tasta 6")
            if moglich=='2a':
                lista=uiModificaTranzactie(lista)
                print("Tranzactia a fost modificata")
        elif optiune == "2":
            print("Stergere: ")
            print("1b. sterge toate tranzactiile de la ziua specifica")
            print("2b. sterge toate tranzactiile dintr-o perioada data(se da ziua de inceput si de sfarsit)")
            print("3b. sterge toate tranzactiile de un anumit tip")
            moglich2=input("Alege ce fel de stargere vrei sa folosesti: ")
            if moglich2=='1b':
                lista = StergeZI(lista)
                print("Tranzactiile din ziua data daca existau au fost sterse din lista! Poti verifica apasand tasta 6.")
            if moglich2=='2b':
                lista = StergePerioada(lista)
                print("Tranzactiile din perioada data au fost sterse daca existau. Poti verifica apasand tasta 6.")
            if moglich2=='3b':
                lista=StergeTip(lista)
                print("Daca au existat tranzctii de tipul dat, acestea au fost sterse. Poti verifica apasand tasta 6.")
        elif optiune == "3":
            print("Cautari: ")
            print("1c. tipărește tranzacțiile cu sume mai mari decât o sumă dată")
            print("2c. tipareste toate tranzacțiile efectuate înainte de o zi și mai mari decât o suma(Se da ziua si suma")
            print("3c. tipărește tranzacțiile de un anumit tip")
            moglich3=input("Alege ce fel de tiparire doresti: ")
            if moglich3=='1c':
                print("Tranzactiile cu suma mai mare decat suma data sunt:")
                lista=TiparesteSumaMaiMare(lista)
            if moglich3=='2c':
                print("Tranzactiile cu suma mai mare si ziua mai mica decat datele date sunt: ")
                lista=TiparesteZISUMA(lista)
            if moglich3=='3c':
                print("Tranzactiile de tipul selectat sunt: ")
                lista=TiparesteTip(lista)
        elif optiune == "4":
            print("Rapoarte: ")
            print("1d. suma totala a tranzactiilor de un anumit tip")
            print("2d. soldul contului la o data specifica")
            print("3d. tipareste toate tranzactiile de un anumit tip ordonat dupa suma")
            moglich4=input("Alege aportul pe care il doresti: ")
            if moglich4=='1d':
                print("Suma totala a tranzactiilor de tipul dat este: ")
                lista=SumaTip(lista)
            if moglich4=='2d':
                print("Soldul contului este: ")
                lista=Sold(lista)
            if moglich4=='3d':
                print("Tranzacțiile de tipul dat ordonate după sumă sunt:")
                lista=OrdineTip(lista)
        elif optiune == "5":
            print("Filtrare")
            print("1e. elimină toate tranzacțiile de un anumit tip")
            print("2e. elimina toate tranzacțiile mai mici decât o sumă dată care au tipul specificat")
            moglich5=input("Alege optiunea de filtrare a tranzactiilor:")
            if moglich5=='1e':
                lista=EliminaTip(lista)
                print("S-au afisat doar tranzactiile din tipul ce nu e ales!")
            if moglich5=='2e':
                lista=EliminaTipSuma(lista)
                print("S-au afisat doar tranzactiile cu o suma mai mare data cu tipul specificat!")
        elif optiune == "6":
            ShowAll(lista)
        elif optiune == "x":
            break
        else:
            print("Wrong option <3")
