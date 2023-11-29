def create_tranzactie(id, ziua, suma, tip):
    """
    Creem o noua tranzactie in contul bancar
    :param id:int,  id-ul tranzactiei
    :param ziua:date,  ziua in care s-a facut tranzactia
    :param suma:int,  suma tranzactionata
    :param tip:string , tipul tranzactiei(intrare/iesire)
    :return: tranzactia
    tranzactie=[id,ziua,suma,tip]
    """
    return {
        "id": id,
        "ziua": ziua,
        "suma": suma,
        "tip": tip
    }

def get_id(tranzactie):
    return tranzactie["id"]
def get_ziua(tranzactie):
    return tranzactie["ziua"]
def get_suma(tranzactie):
    return tranzactie["suma"]
def get_tip(tranzactie):
    return tranzactie["tip"]
def toString(tranzactie):
    return "ID: {},ziua: {},suma: {},tipul: {}".format(get_id(tranzactie),get_ziua(tranzactie),get_suma(tranzactie),get_tip(tranzactie))