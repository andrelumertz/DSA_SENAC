import os

class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)


class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def vazia(self):
        if self.raiz == None:
            return True
        return False

    def adicionar_no(self, valor, pai=None):
        novo_no = No(valor)

        if pai is None:
            self.raiz = novo_no
        else:
            pai_atual = self.raiz
            no_encontrado, _ = self.buscar_no_e_pai(pai, pai_atual)
            if no_encontrado:
               no_encontrado.adicionar_filho(novo_no)
            else:
                input("Pai não encontrado! Enter")


    def buscar_no_e_pai(self, valor, no=None, pai=None):
        if no is None:
            no = self.raiz

        if no.valor == valor:
            return no, pai

        for filho in no.filhos:
            resultado = self.buscar_no_e_pai(valor, filho, no)
            if resultado != (None, None):
                return resultado

        return None, None

    def buscar_no(self, valor):
        no, _ = self.buscar_no_e_pai(valor)
        return no
    "----"
    # def altura(self, no=None):
    #     if no is None:
    #         no = self.raiz
    #
    #     if len(no.filhos) == 0:
    #         return 0
    #
    #     alturas_dos_filhos = [self.altura(filho) for filho in no.filhos]
    #     return 1 + max(alturas_dos_filhos)

    def imprimir(self, no=None, nivel=0):
        if self.vazia():
            print("------ Árvore vazia ------")
            return

        if no is None:
            no = self.raiz
        print(f"Nível: {nivel}", end="-> ")
        print('.' * nivel + str(no.valor))
        for filho in no.filhos:
            self.imprimir(filho, nivel + 1)
        # input("----")



def adicionar_ramo(arvore):
    while True:
        arvore.imprimir()
        print("\nEntre com os dados ou ENTER para encerrar!")
        valor = input("Digite o valor/dado a ser inserido: ")
        if not valor:
            break
        ramo = None
        if not arvore.vazia():
            ramo  = input("Digite o pai para esse dado: ")
            if not ramo:
                break
        arvore.adicionar_no(valor, ramo)


arvore = Arvore()
adicionar_ramo(arvore)



