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
    
    #Algotitmo de Quick Sort
    def quick_sort(self,cabeca,fim):
        #matodo principal do quick sort
        #se a lista estiver vazia ou for um unico nó, para
        if not cabeca or cabeca == fim:
            return cabeca
        
        #particiona a lista e coloca o pivo no lugar certo
        nova_cabeca, novo_fim, pivo = self_particionar(cabeca,fim)
        
        #se o pivo nao for o primeiro elemtno, ordena a parte esquerda da lista
        if nova_cabeca != pivo:
            aux = nova_cabeca 
            while aux.proximo != pivo:
                aux = aux.proximo
            aux.proximo = None #isola a esquerda
            
            nova_cabeca = self.quick_sort(nova_cabeca, aux)
            
            #reconecta o pivo a parte esquerda ordenada
            aux = self._get_ultimo(nova_cabeca)
            aux.proximo = pivo
            
        #ordena a parte da direita da lista apos o pivo
        pivo.proximo  = self.quick_sort(pivo.proximo, novo_fim)
        
        return nova_cabeca
    
    def _particionar(self, cabeca, fim):
        #Organiza os nós ao redor do pivo
        pivo = fim
        anterior = None
        atual = cabeca
        cauda = pivo
        
        nova_cabeca = None
        
        while atual != pivo:
            if atual.valor < pivo.valor:
                #o nó fica onde está
                if nova_cabeca is None:
                    nova_cabeca = atual
                anterior = atual 
                atual =  atual.proximo
            else:
                #O nó é maior: move ele para depois do pivo
                if anterior:
                    anterior.proximo = atual.proximo
                proximo_temp = atual.proximo
                atual.proximo =  None
                cauda.proximo = atual
                cauda = atual
                atual = proximo_temp
            
            if nova_cabeca is None:
                nova_cabeca = pivo
                
            return nova_cabeca, cauda, pivo
        
        def _get_ultimo(self, cabeca):
            #auxiliar para achar o fim do trilho
            while cabeca and cabeca.proximo:
                cabeca = cabeca.proximo
            return cabeca
    
        
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
    
    lista_quick = Lista()
    for d in [30, 10, 45, 5, 20]:
        lista_quick.adicionar(d)

    print("Quick Sort antes")
    lista_quick.exibir()

    #Pega o ultimo nó para passar como parametro
    ultimo_no = lista_quick._get_ultimo(lista_quick.cabeca)
    lista_quick.cabeca = lista_quick.quick_sort(lista_quick.cabeca, ultimo_no)

    print("Quick Sort depois")
    lista_quick.exibir()
