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
            print("Lista vazia")
            return
        
        atual = self.cabeca
        while atual is not None: #Enquanto atual nao for None
            print(f"{atual.valor}", end="->")
            atual = atual.proximo #pula para o proximo
        print("None fim\n")
    
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
    
    
    #Algoritmo de Quick Sort
    def quick_sort(self, cabeca, fim):
        if not cabeca or cabeca == fim:
            return cabeca
        
        nova_cabeca, novo_fim, pivo = self._particionar(cabeca, fim)
        
        if nova_cabeca != pivo:
            aux = nova_cabeca 
            while aux.proximo != pivo:
                aux = aux.proximo
            aux.proximo = None 
            
            nova_cabeca = self.quick_sort(nova_cabeca, aux)
            
            aux = self._get_ultimo(nova_cabeca)
            aux.proximo = pivo
            
        pivo.proximo = self.quick_sort(pivo.proximo, novo_fim)
        return nova_cabeca
    
    def _particionar(self, cabeca, fim):
        pivo = fim
        anterior = None
        atual = cabeca
        cauda = pivo
        nova_cabeca = None
        
        while atual != pivo:
            if atual.valor < pivo.valor:
                if nova_cabeca is None:
                    nova_cabeca = atual
                anterior = atual 
                atual = atual.proximo
            else:
                if anterior:
                    anterior.proximo = atual.proximo
                proximo_temp = atual.proximo
                atual.proximo = None
                cauda.proximo = atual
                cauda = atual
                atual = proximo_temp
        
        if nova_cabeca is None:
            nova_cabeca = pivo
                
        return nova_cabeca, cauda, pivo
        
    def _get_ultimo(self, cabeca):
        while cabeca and cabeca.proximo:
            cabeca = cabeca.proximo
        return cabeca
    #End Quick Sort
    
    #Algoritmo de Counting Sort
    def counting_sort(self):
        #Ordenação por contagem, ideal para inteiros não negativos
        if self.cabeca is None:
            return

        #1 Encontrar o maior valor para saber o tamanho
        maior_valor = self.cabeca.valor
        atual = self.cabeca
        while atual:
            if atual.valor > maior_valor:
                maior_valor = atual.valor
            atual = atual.proximo

        #2 Criar o placar, uma lista de zeros
        #Se o maior valor for 10, precisamos de 11 espaços do 0 ao 10
        placar = [0] * (maior_valor + 1)

        #3 Preencher o placar: percorre o trem e soma +1 na posição do valor
        atual = self.cabeca
        while atual:
            placar[atual.valor] += 1
            atual = atual.proximo

        #4 Reconstruir o trem original usando os dados do placar
        atual = self.cabeca
        for numero, quantidade in enumerate(placar):
            while quantidade > 0:
                atual.valor = numero #Sobrescreve o valor do vagão
                atual = atual.proximo #Pula para o proximo
                quantidade -= 1
    #End Counting Sort
                
    #Algoritmo de Radix Sort
    def radix_sort(self):
        #Ordena olhando digito por digito
        if not self.cabeca:
            return

        #1 Encontrar o maior numero para saber quantos digitos processar
        max_val = self.cabeca.valor
        atual = self.cabeca
        while atual:
            if atual.valor > max_val:
                max_val = atual.valor
            atual = atual.proximo

        #2 Processar cada digito unidade, dezena, centena...
        exp = 1
        while max_val // exp > 0:
            self._counting_sort_para_radix(exp)
            exp *= 10

    def _counting_sort_para_radix(self, exp):
        #Versão do counting sort que olha apenas para um digito
        output = [0] * self._get_tamanho()
        contagem = [0] * 10 #Apenas 10 digitos possiveis 0-9
        
        #Armazena a contagem das ocorrencias
        atual = self.cabeca
        while atual:
            indice = (atual.valor // exp) % 10
            contagem[indice] += 1
            atual = atual.proximo

        #Muda contagem[i] para conter a posição real no output
        for i in range(1, 10):
            contagem[i] += contagem[i - 1]

        #Constroi o array de saida output
        #Para manter percorremos a lista e guardamos os valores
        temp_lista = []
        atual = self.cabeca
        while atual:
            temp_lista.append(atual.valor)
            atual = atual.proximo
        
        #Preenche o output de tras para frente para manter 
        res_array = [0] * len(temp_lista)
        for i in range(len(temp_lista) - 1, -1, -1):
            valor = temp_lista[i]
            indice = (valor // exp) % 10
            res_array[contagem[indice] - 1] = valor
            contagem[indice] -= 1

        #Copia o output de volta para a nossa lista encadeada
        atual = self.cabeca
        for valor in res_array:
            atual.valor = valor
            atual = atual.proximo

    def _get_tamanho(self):
        #Retorna quantos nós existem no trem
        count = 0
        atual = self.cabeca
        while atual:
            count += 1
            atual = atual.proximo
        return count
    
        
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

    lista_counting = Lista()
    for d in [4, 2, 2, 8, 3, 3, 1]:
        lista_counting.adicionar(d)

    print("Counting Sort antes:")
    lista_counting.exibir()

    lista_counting.counting_sort()

    print("Counting Sort depois:")
    lista_counting.exibir()

    #Teste do Radix Sort
    lista_radix = Lista()

    dados_radix = [170, 45, 75, 90, 802, 24, 2, 66]
    for d in dados_radix:
        lista_radix.adicionar(d)

    print("Radix Sort antes:")
    lista_radix.exibir()

    lista_radix.radix_sort()

    print("Radix Sort depois:")
    lista_radix.exibir()