class No:
    def __init__(self, valor):
        self.esquerda = None
        self.valor = valor
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def vazia(self):
        if self.raiz is None:
            return True
        return False

    def adicionar_no(self, valor):
        if self.vazia():
            novo_No = No(valor)
            self.raiz = novo_No
        else:
            self.raiz = self._adicionar_no_folha(self.raiz, valor)

    def _adicionar_no_folha(self, no_atual, valor):
        if not no_atual:
            novo_No = No(valor)
            return novo_No
        elif valor == no_atual.valor:
            print(f"Valor {valor} já existe. Ignorando a Inserção.")
            return no_atual
        elif valor < no_atual.valor:
            no_atual.esquerda = self._adicionar_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._adicionar_no_folha(no_atual.direita, valor)

        ############################# altura
        no_atual.altura = 1 + max(
            self._altura(no_atual.esquerda),
            self._altura(no_atual.direita)
        )
        ############################# Fator Balanceamento
        balanceamento = self._balanceamento(no_atual)

        if balanceamento < -1:
            if valor < no_atual.esquerda.valor:
                return self._rotacao_direita(no_atual)
            else:
                no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
                return self._rotacao_direita(no_atual)

        if balanceamento > 1:
            if valor > no_atual.direita.valor:
                return self._rotacao_esquerda(no_atual)
            else:
                no_atual.direita = self._rotacao_direita(no_atual.direita)
                return self._rotacao_esquerda(no_atual)

        return no_atual

    #Metodo para remover um nó da árvore AVL
    def remover_no(self, valor):
        if self.vazia():
            print("A árvore está vazia!")
            return
        self.raiz = self._remover_no_recursivo(self.raiz, valor)

    def _min_valor_no(self, no):
        #Encontra o menor nó da subárvore direita
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _remover_no_recursivo(self, no_atual, valor):
        if not no_atual:
            return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self._remover_no_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._remover_no_recursivo(no_atual.direita, valor)
        else:
            
            #Casos com 1 ou 0 filhos
            if no_atual.esquerda is None:
                temp = no_atual.direita
                no_atual = None
                return temp
            elif no_atual.direita is None:
                temp = no_atual.esquerda
                no_atual = None
                return temp

            #Casos com 2 filhos e pega o sucessor
            temp = self._min_valor_no(no_atual.direita)
            no_atual.valor = temp.valor
            no_atual.direita = self._remover_no_recursivo(no_atual.direita, temp.valor)

        #Se a arvore ficou vazia apos exclusão
        if no_atual is None:
            return no_atual

        #Atualiza a altura do nó atual
        no_atual.altura = 1 + max(
            self._altura(no_atual.esquerda),
            self._altura(no_atual.direita)
        )

        #Verifica o fator de balanceamento do nó atual
        balanceamento = self._balanceamento(no_atual)

        #Rotações para balancear a árvore
        if balanceamento < -1 and self._balanceamento(no_atual.esquerda) <= 0:
            return self._rotacao_direita(no_atual)

        if balanceamento < -1 and self._balanceamento(no_atual.esquerda) > 0:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        if balanceamento > 1 and self._balanceamento(no_atual.direita) >= 0:
            return self._rotacao_esquerda(no_atual)

        if balanceamento > 1 and self._balanceamento(no_atual.direita) < 0:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual
    

    def _altura(self, no):
        if not no:
            return 0
        return no.altura

    def _balanceamento(self, no):
        if not no:
            return 0
        fb = self._altura(no.direita) - self._altura(no.esquerda)
        return fb

    def _rotacao_esquerda(self, pai):
        if not pai or not pai.direita:
            print(f"Rotação à esquerda não realizada: Filho direito inexistente.")
            return pai
        filhoD = pai.direita
        neto = filhoD.esquerda

        filhoD.esquerda = pai
        pai.direita = neto

        pai.altura = 1 + max(
            self._altura(pai.esquerda),
            self._altura(pai.direita))
        filhoD.altura = 1 + max(
            self._altura(filhoD.esquerda),
            self._altura(filhoD.direita))

        return filhoD

    def _rotacao_direita(self, pai):
        if not pai or not pai.esquerda:
            print("Rotação à direita não realizada: filho esquerdo inexistente.")
            return pai

        filhoE = pai.esquerda
        neto = filhoE.direita

        filhoE.direita = pai
        pai.esquerda = neto

        pai.altura = 1 + max(
            self._altura(pai.esquerda),
            self._altura(pai.direita))
        filhoE.altura = 1 + max(
            self._altura(filhoE.esquerda),
            self._altura(filhoE.direita))
        input("Enter - Pressione Enter para continuar")
        return filhoE

    def imprimir(self):
        if self.vazia():
            print("========== Árvore vazia ==========")
            return
        print("\n=============== Árvore ================")
        self._imprimir(self.raiz)
        print("=========================================\n")

    def _imprimir(self, no_atual):
        if no_atual is not None:
            self._imprimir(no_atual.esquerda)
            print(f"Nó: {str(no_atual)[-5:]} -- Esq.{str(no_atual.esquerda)[-5:]} Valor: {str(no_atual.valor)}  Dir.{str(no_atual.direita)[-5:]} Alt.{str(no_atual.altura)}")
            self._imprimir(no_atual.direita)



#Teste na árvore AVL

def popular_arvore(arvore):
    #Valores do trabalho
    lista_entradas = [100, 50, 20, 40, 30] 
    
    print("---- Inserções ----")
    for e in lista_entradas:
        print(f"\n--- Inserindo o valor {e} ---")
        arvore.adicionar_no(e)
        arvore.imprimir()

    print("\n\n---- Iniciando os testes de exclusão ----")
    
    print("\n---- Excluindo o 40 (Nó folha) ----")
    arvore.remover_no(40)
    arvore.imprimir()

    print("\n---- Excluindo o 50 - Vai forçar a arvore a se arrumar ----")
    arvore.remover_no(50)
    arvore.imprimir()


arvore = ArvoreAVL()

popular_arvore(arvore)


