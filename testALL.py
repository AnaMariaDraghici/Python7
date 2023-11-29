from Tests.testCRUD import testAdaugaTranzactie
from Tests.testDomain import testTranzactie


def runAllTests():
    testTranzactie()
    testAdaugaTranzactie()