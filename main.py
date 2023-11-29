from Logic.CRUD import AdaugaTranzactie
from UI.console import runMenu
from Tests.testALL import runAllTests

def main():
    runAllTests()
    lista=[]
    lista=AdaugaTranzactie("1",24,78,"intrare",lista)
    lista=AdaugaTranzactie("2",2,100,"iesire",lista)
    lista=AdaugaTranzactie("3",10,150,"intrare",lista)
    runMenu(lista)

main()

