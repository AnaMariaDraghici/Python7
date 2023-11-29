from Domain.tranzactie import create_tranzactie, get_id

def getByID(id,lista):
    """
    Gaseste o tranzactie in lista dupa ID
    :param id: string
    :param lista: lista
    :return: tranzactia cu ID-ul din lista sau None
    """
    for tranzactie in lista:
        if get_id(tranzactie) == id:
            return tranzactie
    return None

def AdaugaTranzactie(id,ziua,suma,tip,lista):
    """
    Adaugam tranzactie intr-o lista
    :param id: string
    :param ziua: string
    :param suma: float
    :param tip: string
    :param lista: lista de tranzactii
    :return: o lista de tranzactii, noi si cele adaugate
    """
    if getByID(id,lista) is not None:
        raise ValueError("ID-ul exista deja!")
    tranzactie = create_tranzactie(id,ziua,suma,tip)
    lista.append(tranzactie)
    return lista

def ModificaTranzactie(id, ziua, suma, tip, lista):
    tranzactie_gasita = False

    for index, tranzactie in enumerate(lista):
        if get_id(tranzactie) == id:
            tranzactieNoua = create_tranzactie(id, ziua, suma, tip)
            lista.pop(index)
            lista.append(tranzactieNoua)
            tranzactie_gasita = True
            break

    if tranzactie_gasita == False:
        raise ValueError("Nu exista o tranzactie cu ID-ul dat!")

    return lista