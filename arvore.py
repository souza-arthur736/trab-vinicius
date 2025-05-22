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
def posordemex():
    arvore = arvorebinaria()
    n1 = Node('r')
    n2 = Node('a')
    n3 = Node('f')
    n4 = Node('a')
    n5 = Node('e')
    n6 = Node('l')
    n7 = Node('m')
    n8 = Node('e')
    n9 = Node('l')
    n0 = Node('o')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7
    arvore.raiz = n0
    return arvore

print("percurso em pos ordem: ")
arvore = posordemex()