class Node:
    def __init__(self, elemento):
        self.elem = elemento
        self.izq = None
        self.der = None

    def __str__(self):
        return self.elem


class BinaryTree:
    def __init__(self, nodo):
        self.raiz = Node(nodo)
        self.cont = 1

    
    


class EmptyCollectionException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
class ParenthesisException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

    


class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def __str__(self):
        return str(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, elem):
        self._data.append(elem)
    def pop(self):
        if ( self.is_empty() ):
            raise EmptyCollectionException("La pila no contiene datos")
        return self._data.pop()
    def peek(self):
        if self.is_empty():
            raise EmptyCollectionException("La pila no contiene datos")
        return self._data[-1]



def evaluador_parentesis(array):
    pila = ArrayStack()
    for i in range(0, len(array)):
        if array[i] == '(':
           pila.push(array[i])
        if array[i] == ')':
            if pila.is_empty():
                return False
            else:
               pila.pop()
    return pila.is_empty()
          

def arbol_jerarquico(array):
    if evaluador_parentesis(array) == False:
        # print("Los paréntesis no están colocados correctamente")
        # return False
        raise ParenthesisException("No corresponsen los parentesis")
    pilaA = ArrayStack()
    pilaB = ArrayStack()
    for i in range(0, len(array)):
        dato = array[i]
        if type(dato).__name__ == 'float':
            pilaB.push(BinaryTree(dato))
        elif dato == '(':
            pilaA.push(dato)
        elif dato == ')':
            bandera = True
            while pilaA.peek() != '(':
                p = pilaB.pop()
                s = pilaB.pop()
                o = pilaA.pop()
                arbol = BinaryTree(o)
                arbol.raiz.izq = s.raiz
                arbol.raiz.der = p.raiz
                pilaB.push(arbol)
            pilaA.pop()
        else:
            if dato == "+" or dato == "-":
                bandera = True
                while bandera:
                    if pilaA.peek() != "(":
                        o = pilaA.pop()
                        p = pilaB.pop()
                        s = pilaB.pop()
                        arbol = BinaryTree(o)
                        arbol.raiz.izq = s.raiz
                        arbol.raiz.der = p.raiz
                        pilaB.push(arbol)
                        # pilaA.push(dato)
                    else:
                        # pilaA.push(dato)
                        bandera = False
                pilaA.push(dato)
            if dato == '*' or dato == '/':
                bandera = True
                while bandera:
                    if pilaA.peek() != "(" and pilaA.peek() != "-" and pilaA.peek() != "+":
                        o = pilaA.pop()
                        p = pilaB.pop()
                        s = pilaB.pop()
                        arbol = BinaryTree(o)
                        arbol.raiz.izq = s.raiz
                        arbol.raiz.der = p.raiz
                        pilaB.push(arbol)
                    else:
                        bandera = False
                pilaA.push(dato)

    return pilaB.peek()
    
def recorrido_postorden(raiz):
        res = []
        if raiz:
            res = recorrido_postorden(raiz.izq)
            res = res + recorrido_postorden(raiz.der)
            res.append(raiz.elem)
        return res

def evalcion_postfija(arr):
    operandos = ArrayStack()
    for i in range(0, len(arr)):
        if type(arr[i]).__name__ == "float":
            operandos.push(arr[i])
        if arr[i] == "+":
            a = operandos.pop()
            b = operandos.pop()
            operandos.push(b + a)
        if arr[i] == "-":
            a = operandos.pop()
            b = operandos.pop()
            operandos.push(b - a)
        if arr[i] == "/":
            a = operandos.pop()
            b = operandos.pop()
            if a==0 :
                operandos.push(0)
            else:
                r = b/a
                if r == 0:
                    print("Esta operación incluye una división entre cero, la cual no está permitida")
                    return False
                else:
                    operandos.push(r)

        if arr[i] == "*":
            operandos.push(operandos.pop() * operandos.pop())
    return operandos.peek()
            
    


operacion = ['(', float(3), '+', float(2), '*', float(4), '/', float(2), ")"]

op = ['(', float(5),'-',float(3), ')']

arbol = arbol_jerarquico(op)

# if type(arbol).__name__ == "BinaryTree":
#     print(evalcion_postfija(recorrido_postorden(arbol.raiz)))



# GUI

    