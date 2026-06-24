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


    def buscar_no_e_pai(self, valor, no=None, pai=None):
        if self.vazia():
            return None, None
            
        if no is None:
            no = self.raiz

        if no.valor == valor:
            return no, pai

        for filho in no.filhos:
            resultado = self.buscar_no_e_pai(valor, filho, no)
            if resultado != (None, None):
                return resultado

        return None, None

    def imprimir(self, no=None, nivel=0):
        if self.vazia():
            print("--- Árvore vazia ---")
            return

        if no is None:
            no = self.raiz
            
        print("Nível:", nivel, "->", '.' * nivel + str(no.valor))
        for filho in no.filhos:
            self.imprimir(filho, nivel + 1)

    #Parte da exclusão de nós na árvore
    def excluir_no(self, valor):
        if self.vazia():
            return

        #Se for para excluir a raiz
        if self.raiz.valor == valor:
            self.raiz = None
            return

        #Busca quem é o nó e quem é o pai dele
        no_alvo, pai = self.buscar_no_e_pai(valor)

        #Se achou os dois remove o alvo da lista de filhos do pai
        if no_alvo != None and pai != None:
            pai.filhos.remove(no_alvo)


#Parte 2: Leitura de pastas e arquivos do sistema operacional
def carregar_pastas(caminho, arvore, pai=None):
    # Pega apenas o nome da pasta atual
    if "\\" in caminho:
        nome_pasta = caminho.split("\\")[-1]
    else:
        nome_pasta = caminho.split("/")[-1]
        
    if nome_pasta == "": 
        nome_pasta = caminho

    #Adiciona na arvore usando a função
    arvore.adicionar_no(nome_pasta, pai)

    #Lista tudo o que tem dentro da pasta atual
    itens = os.listdir(caminho)
    
    for item in itens:
        if caminho.endswith("\\"):
            sub_caminho = caminho + item
        else:
            sub_caminho = caminho + "\\" + item

        #Se for uma pasta faz a recursão
        if os.path.isdir(sub_caminho):
            carregar_pastas(sub_caminho, arvore, nome_pasta)


#Teste da árvore genérica
arvore = Arvore()

caminho_usuario = input("Digite o caminho da pasta: ")
carregar_pastas(caminho_usuario, arvore)

print("\n--- Árvore criada ---")
arvore.imprimir()

print("\n--- Testando Exclusão ---")
pasta_deletar = input("Digite o nome da pasta que voce quer excluir: ")
arvore.excluir_no(pasta_deletar)

print("\n--- Árvore depois da exclusão ---")
arvore.imprimir()