# CRIACAO DE UM CLASSE PARA O NO
class Node:                            
    def __init__(self, valor):           
        self.valor = valor
        self.esquerda = None
        self.direita = None
    # PRECISAMOS QUE OS NUMEROS VOLTEM, ENTAO CONVERTEMOS OS VALORES EM STR
    def __str__(self):
        return str(self.valor)
# CRIACAO DE UMA CLASSE PARA A ARVOREBINARIA EM SI
class arvorebinaria:
    def __init__(self, valor):
        node = Node(valor)
        self.raiz = node

# Percurso em ordem simetrica (inorder)
    def in_order(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.in_order(node.esquerda)
        print(node) # esquerda -> raiz -> direita
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
        print(node) # esquerda -> direita -> raiz    
