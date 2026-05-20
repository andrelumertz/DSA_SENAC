class TreeNode:
    """
    PLANTA DO POSTO DE COMANDO (NÓ)
    Cada objeto desta classe é um posto na floresta que guarda um valor
    e possui duas trilhas que podem levar a outros postos abaixo dele.
    """
    def __init__(self, val):
        self.val = val      # A caixa onde guardamos o número neste posto
        self.left = None    # A trilha da ESQUERDA (começa vazia, sem saída)
        self.right = None   # A trilha da DIREITA (começa vazia, sem saída)


class BinaryTree:
    """
    A CENTRAL DE CONTROLE (A ÁRVORE)
    Esta classe gerencia a floresta inteira, sabendo apenas onde fica a entrada principal.
    """
    def __init__(self):
        self.root = None    # A entrada da floresta (Raiz). Começa vazia.

    def insert(self, val):
        """
        GUARDA DA ENTRADA (Método Público)
        Recebe o novo número e decide se cria a raiz ou se envia o mensageiro floresta adentro.
        """
        # Se a entrada da floresta estiver completamente vazia...
        if not self.root:
            # Construímos o primeiro posto bem na entrada! Ele vira a Raiz.
            self.root = TreeNode(val)
        else:
            # Se já houver um posto na entrada, enviamos o mensageiro recursivo
            # para descobrir em qual trilha lá para dentro esse novo número deve ir.
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        """
        O MENSAGEIRO RECURSIVO (Método Privado)
        Corre pelas trilhas aplicando a regra da BST: menor para esquerda, maior para direita.
        """
        # Regra de trânsito: O número que queremos guardar é MENOR que o número deste posto?
        if val < node.val:
            # Se for menor, olhamos para a trilha da ESQUERDA. Já existe um posto lá?
            if node.left:
                # Se já existir, o mensageiro corre por essa trilha e repete a pergunta no próximo posto.
                self._insert_recursive(node.left, val)
            else:
                # Se a trilha da esquerda estiver vazia, construímos o novo posto exatamente aqui!
                node.left = TreeNode(val)
        
        # Se o número for MAIOR ou igual...
        else:
            # Olhamos para a trilha da DIREITA. Já existe um posto lá?
            if node.right:
                # Se já existir, o mensageiro desce por ela e repete a lógica no posto de baixo.
                self._insert_recursive(node.right, val)
            else:
                # Se a trilha da direita estiver vazia, fundamos o novo posto aqui!
                node.right = TreeNode(val)

    def search(self, val):
        """
        CHEFIA DE BUSCA (Método Público)
        Aciona o rastreador a partir do topo (raiz) da estrutura.
        """
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        """
        O RASTREADOR VELOZ (Método Privado)
        Busca o número descartando metade das opções a cada decisão.
        """
        # Se o rastreador seguiu uma trilha e deu em um lugar vazio (None)...
        if not node:
            # Significa que o número não existe na floresta. Retorna Falso.
            return False
        
        # Se a caixa do posto atual tiver exatamente o número que procuramos...
        if node.val == val:
            # Encontramos o tesouro! Retorna Verdadeiro.
            return True
        
        # Se o número que buscamos for MENOR que o do posto atual...
        if val < node.val:
            # O rastreador ignora o lado direito e corre para a ESQUERDA.
            return self._search_recursive(node.left, val)
        
        # Caso contrário (se for maior)...
        # O rastreador ignora o lado esquerdo e corre para a DIREITA.
        return self._search_recursive(node.right, val)


# ==============================================================================
# TESTANDO A NOSSA FLORESTA DE POSTOS DE COMANDO
# ==============================================================================

# 1. Criamos o mapa da árvore
tree = BinaryTree()

# 2. Valores que vamos inserir (o primeiro vira a raiz, os outros orbitam ao redor)
values_to_insert = [10, 5, 15, 3, 7, 12, 18]
for val in values_to_insert:
    tree.insert(val)

# 3. Fazendo as buscas na floresta
print(tree.search(7))   # Deve retornar True (O rastreador vai passar por: 10 -> 5 -> 7)
print(tree.search(14))  # Deve retornar False (Vai passar por: 10 -> 15 -> 12 -> Direita vazia)
print(tree.search(10))  # Deve retornar True (Encontra logo de cara na entrada/raiz)
print(tree.search(18))  # Deve retornar True (Vai passar por: 10 -> 15 -> 18)