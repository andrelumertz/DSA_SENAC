class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None  # aponta pro próximo nodo


class Lista:
    def __init__(self):
        self.cabeca = None  # primeiro nodo da lista

    def inserir(self, valor):
        novo = Nodo(valor) # 1. cria o novo nodo
        novo.proximo = self.cabeca # 2. novo aponta pra quem era o primeiro
        self.cabeca = novo # 3. novo vira o primeiro

    def para_lista_python(self):
        """Converte lista encadeada → list do Python (para facilitar ordenação)"""
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        return elementos

    def reconstruir_da_lista(self, elementos):
        """Reconstrói a lista encadeada a partir de uma list do Python"""
        self.cabeca = None
        # percorre ao contrário para compensar o comportamento de pilha do inserir,
        # que sempre coloca o novo nodo na cabeça — garantindo ordem crescente no final
        for valor in reversed(elementos): 
            self.inserir(valor)
            
    
    def counting_sort(self):
        # 1. converte a lista encadeada para uma list do Python
        elementos = self.para_lista_python()
        # se a lista estiver vazia, não há nada a ordenar
        if not elementos:
            return
        # 2. encontra o valor máximo para determinar o tamanho do array de contagem
        maximo = max(elementos)
        # 3. cria o array de contagem e conta as ocorrências de cada valor
        contagem = [0] * (maximo + 1)
        # 4. preenche o array de contagem
        for val in elementos:
            contagem[val] += 1
        # 5. reconstrói a lista ordenada a partir do array de contagem
        ordenado = []
        # para cada valor e sua quantidade, adiciona o valor à lista ordenada a quantidade de vezes que ele aparece
        for val, qtd in enumerate(contagem):
            ordenado.extend([val] * qtd) # cria uma lista repetindo o valor qtd vezes e o extend adiciona esses elementos na lista ordenado
        self.reconstruir_da_lista(ordenado)
        
# ── Teste ──────────────────────────────────────
lista = Lista()

for numero in [3, 1, 2, 1, 3]:
    lista.inserir(numero)

print("antes:", lista.para_lista_python())

lista.counting_sort()

print("depois:", lista.para_lista_python())