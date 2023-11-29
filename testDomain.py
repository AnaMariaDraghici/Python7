from Domain.tranzactie import create_tranzactie, get_tip, get_id, get_suma, get_ziua

def testTranzactie():
    tranzactie = create_tranzactie("1",24,78,"intrare")
    assert get_id(tranzactie) == "1"
    assert get_ziua(tranzactie) == 24
    assert get_suma(tranzactie) == 78
    assert get_tip(tranzactie) == "intrare"

