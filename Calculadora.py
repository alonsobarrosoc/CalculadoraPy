

class Node:


    def __init__(self, elemento):
        self.elem = elemento
        self.izq, self.der, self.papa = null
    def __init__(self):
        self.elem = null
        self.izq, self.der, self.papa = null

Node(5)

# ,3,+,2,*,4,

# (2-6)*3+5
# pilaA => ( 2 6
# pilaB =>  2<- - ->6

class Tree:
 
    def __init__(self):
        self.raiz = null
        self.cont = 1
    def __init__(self, nodo):
        self.raiz = Node(nodo)
        self.cont = 1
class ArrayStack:
    pila = []
    cont = 0
    def ArrayStack():
        cont = 0

    def push(elem):
        pila.add(elem)
    def pop():
        pila.pop
    def peek():
        return pila[-1]





def calculadora(array):
    pilaA = []
    pilaB = []
    operadores = ['+', '-','*','/']

    for i in range(0, len(array)):
        t= array[i]
        if t == '(':
            pilaA.append(t)
        if t in operadores:
            pilaA.append(t)
        if t == ')':
            while bandera:
                if pilaA[-1] != '(':
                    p = pilaB.pop
                    s = pilaB.pop
                    o = pilaA.pop
                    t = Tree(o)
                    t.izq = s
                    t.der = p
                    pilaB.add(t)
                else: bandera = true
        else:
            pilaB.append(Tree(t))


    
