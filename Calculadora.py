

class Node:


    def __init__(self, elemento):
        self.elem = elemento
        self.izq = None
        self.der = None

    def getDer(self):
        return self.der
    
    def getIzq(self):
        return self.izq
    
    def getElem(self):
        return self.elem

    def setDer(self, elem):
        self.der = elem
    
    def setIzq(self, elem):
        self.izq = elem
    
    def setElem(self, a):
        self.elem = a
    
        


    # def __init__(self):
    #     self.elem = null
    #     self.izq, self.der, self.papa = null

Node(5)

# ,3,+,2,*,4,

# (2-6)*3+5
# pilaA => ( 2 6
# pilaB =>  2<- - ->6

class Tree:
 
    pila = []
    
    def __init__(self, nodo):
        self.raiz = Node(nodo)
        self.cont = 1
    def getRaiz(self):
        return self.raiz

class EmptyCollectionException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
    
class ArrayStack:
    
    def ArrayStack(self):
        self.pila = []

    def __len__(self):
        return len(self.pila)

    def push(self, elem):
        self.pila.append(elem)

    def is_empty(self):
        return (len(self.pila) == 0)

    def pop(self):
        if self.is_empty:
            raise EmptyCollectionException("La pila no contiene datos")
        return self.pila.pop()
    def peek(self):
        if self.is_empty:
            raise EmptyCollectionException("La pila no contiene datos")
        return self.pila[-1]





def calculadora(array):
    pilaA = ArrayStack()
    pilaB = ArrayStack()

    
    operadores = ['+', '-','*','/']

    for i in range(0, len(array)):
        t= array[i]
        if t == '(':
            pilaA.push(t)
        if t in operadores:
            pilaA.push(t)
        if t == ')':
            bandera = False
            while bandera:
                if pilaA.peek != '(':
                    p = pilaB.pop
                    s = pilaB.pop
                    o = pilaA.pop
                    arbol = Tree(o)
                    # arbol.getRaiz.setIzq(s)
                    arbol.raiz.izq = s
                    arbol.raiz.der = p
                    pilaB.push(t)
                else: bandera = True
        else:
            pilaB.push(Tree(t))


    
