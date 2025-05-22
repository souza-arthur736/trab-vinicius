# CRIACAO DE UM CLASSE PARA O NO
class Node:                            
    def __init__(self, valor):           
        self.valor = valor # guarda o valor do no
        self.esquerda = None # cria uma branch, mas define nada nela
        self.direita = None # o mesmo do de cima
    # PRECISAMOS QUE OS NUMEROS VOLTEM, ENTAO CONVERTEMOS OS VALORES EM STR para retornarem
    def __str__(self):
        return str(self.valor)
# CRIACAO DE UMA CLASSE PARA A ARVOREBINARIA EM SI
class arvorebinaria:
    def __init__(self, valor):
        node = Node(valor) # cria um no com o valor
        self.raiz = node # define essa arvore com  a raiz primeiro no

    # Percurso em ordem simetrica (inorder)
        def in_order(self, node=None):
            if node is None:
                node = self.raiz
            if node.esquerda:
                self.in_order(node.esquerda)
            print(node)
            if node.direita:
                self.in_order(node.direita)

# Percurso em pós ordem
    def post_order(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.post_order(node.esquerda)
        if node.direita:
            self.post_order(node.direita)
        print(node)
    
    # Percuso em pre ordem
    def pre_order(self, node=None):
        if node is None:
            node = self.raiz
        print(node)
        if node.esquerda:
            self.pre_order(node.esquerda)
        if node.direita:
            self.pre_order(node.direita)