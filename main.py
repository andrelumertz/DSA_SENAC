class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
class Lista:
    def __init__(self):
        self.cabeca = None #Comeca vazia sem nenhum Nodo
        
    def adicionar(self, valor):
        #Metodo para add um novo dado no final da lista
        novo_no = Nodo(valor) #Cria um novo Nodo
        
        #Se a Lista estiver vazia, o novo nó vira a cabeça
        if self.cabeca is None:
            self.cabeca = novo_no
            print(f"{valor} adicionado como o primeiro da lista.")
            return
        
        #Se nao estiver vazia, caminha até o ultimo nó
        atual = self.cabeca 
        while atual.proximo is not None:
            atual = atual.proximo
            
        #Faz o engate: o próximo do último agora é o novo nó
        atual.proximo = novo_no
        print(f"{valor} engatado no final da lista.")
        
    def exibir(self):
        #Percorre a lista e imprime visualmente os elementos
        if self.cabeca is None:
            print("Lista vazia.")
            return
        
        atual = self.cabeca
        while atual is not None: #Enquanto atual nao for None
            print(f"{atual.valor}", end="->")
            atual = atual.proximo #pula para o proximo
        print("None (fim)\n")
    
    #Algoritmo do Merge Sort    
    def merge_sort(self, cabeca):
        if cabeca is None or cabeca.proximo is None:
            return cabeca
        
        meio = self._get_meio(cabeca)
        proximo_do_meio = meio.proximo
        meio.proximo = None
        
        esquerda = self.merge_sort(cabeca)
        direita = self.merge_sort(proximo_do_meio)
        
        return self._merge(esquerda, direita)
    
    def _get_meio(self, cabeca):
        #Logica da tarturuga e lebre
        lento = cabeca 
        rapido = cabeca 
        while rapido.proximo and rapido.proximo.proximo:
            lento = lento.proximo
            rapido = rapido.proximo.proximo
        return lento
    
    def _merge(self, esquerda, direita):
        #Logica de fusao
        if not esquerda: return direita
        if not direita: return esquerda
        
        if esquerda.valor <= direita.valor:
            resultado = esquerda
            resultado.proximo = self._merge(esquerda.proximo, direita)
        else:
            resultado = direita
            resultado.proximo = self._merge(esquerda, direita.proximo) 
        return resultado
    #End Merge Sort
            
        
#testes
    
if __name__ == "__main__":
    minha_lista = Lista()
    dados = [15, 3, 22, 10, 1, 40]
    for d in dados:
        minha_lista.adicionar(d)
    
    print("Antes da ordenacao:")
    minha_lista.exibir()
    
    #Aplicando o merge sort
    minha_lista.cabeca = minha_lista.merge_sort(minha_lista.cabeca)
    
    print("Apos o Merge Sort:")
    minha_lista.exibir()
