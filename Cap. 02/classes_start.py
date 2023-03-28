#
# Exemplo de como criar classes
#

class minhaClasse():
    def __init__(self):
        self.meuAtributo = "Passou Pelo Construtor!"

    def meuMetodo(self):
        print("Passou Pelo meuMetodo")

    def meuMetodo2(self, valor):
        self.outroAtributo = valor

def criaObjeto():
    meuObj = minhaClasse()
    var1 = meuObj.meuAtributo
    print(var1)

    meuObj.meuMetodo()

    meuObj.meuMetodo2("Executando um método")

criaObjeto()