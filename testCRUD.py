from Domain.tranzactie import get_tip,get_id,get_suma,get_ziua
from Logic.CRUD import AdaugaTranzactie,getByID

def testAdaugaTranzactie():
    lista = []
    lista = AdaugaTranzactie("1",24,78,"intrare",lista)
    assert len(lista) == 1
    assert get_id(getByID("1",lista)) == "1"
    assert get_ziua(getByID("1",lista))==24
    assert get_suma(getByID("1",lista))==78
    assert get_tip(getByID("1",lista))=="intrare"
'''

def testModificaTranzactie():
    lista = []
    lista = AdaugaTranzactie("1", 24, 78, "intrare", lista)
    lista = AdaugaTranzactie("2", 8, 80, "iesire", lista)
    lista = ModificaTranzactie("2",10,80,"iesire",lista)
    TranzactieNoua = getByID("2",lista)
    assert get_id(TranzactieNoua) == "2"
    assert get_ziua(TranzactieNoua) == 10
    assert get_suma(TranzactieNoua) == 80
    assert get_tip(TranzactieNoua) == "iesire"
'''