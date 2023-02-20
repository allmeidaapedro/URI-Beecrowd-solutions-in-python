# Árvores -> estruturas de dados hierárquicas -> raiz, nós, filhos - pais - folhas, subárvores, níveis, altura, arestas
# Árvores Binárias de busca
# cada nó pai possui apenas dois filhos
# filhos à esquerda são menores que o nó pai
# filhos à direita são maiores que o nó pai
# PreOrdem: visita nó, recursão à esquerda, recursão à direita
# PosOrdem: recursão à esquerda, recursão à direita, visita nó
# EmOrdem: recursão à esquerda, visita nó, recursão à direita


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def insert(self, value):
        parent = None
        x = self.root
        while x:
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)


    # visita nó -> recursão à esquerda -> recursão à direita
    def preOrder(self, node):
        if node != None:
            yield node.data
            yield from self.preOrder(node.left)
            yield from self.preOrder(node.right)

    # recursão à esquerda -> recursão à direita -> visita nó
    def postOrder(self, node):
        if node != None:
            yield from self.postOrder(node.left)
            yield from self.postOrder(node.right)
            yield node.data

    # recursão à esquerda -> visita nó -> recursão à direita
    def inorder(self, node):
        if node != None:
            yield from self.inorder(node.left)
            yield node.data
            yield from self.inorder(node.right)


    def search(self, value, node):
        if node == None:
            return False
        if node.data == value:
            return True
        if value < node.data:
            return self.search(value, node.left)
        else:
            return self.search(value, node.right)

tree = BST()
while True:
    try:
        cd = input().split()

    except EOFError:
        break

    if cd[0] == 'I':
        tree.insert(cd[1])
    elif cd[0] == 'INFIXA':
        print(*[no for no in tree.inorder(tree.root)])
    elif cd[0] == 'PREFIXA':
        print(*[no for no in tree.preOrder(tree.root)])
    elif cd[0] == 'POSFIXA':
        print(*[no for no in tree.postOrder(tree.root)])
    elif cd[0] == 'P':
        existe = tree.search(cd[1], tree.root)
        if existe:
            print(f'{cd[1]} existe')
        else:
            print(f'{cd[1]} nao existe')



