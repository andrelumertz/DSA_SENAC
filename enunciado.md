Atividade 1 – SISTEMA DE PROCESSAMENTO DE DADOS

Uma empresa de processamento de dados precisa ordenar grandes volumes de valores inteiros não negativos, como identificadores e pontuações.
Para atender diferentes cenários, o sistema deve oferecer múltiplos algoritmos de ordenação, escolhidos conforme as características dos dados.
Você deverá implementar uma estrutura de dados baseada em lista encadeada, contendo:
Uma classe Nodo, que representa cada elemento
Uma classe Lista, que gerencia a estrutura e oferece métodos de ordenação

Requisitos
A classe Lista deve implementar os seguintes métodos:
merge_sort()
quick_sort() 
counting_sort()
radix_sort()

Todos os métodos devem:
Ordenar os elementos em ordem crescente
Manter os dados dentro da própria estrutura Lista
Restrições
Os valores são inteiros não negativos
counting_sort e radix_sort só devem ser usados quando a restrição acima for respeitada