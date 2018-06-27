class Node:
    def __init__(self, nombre,apellido,email,numero):
        self.left = None
        self.right = None
        self.nombre=nombre
        self.apellido = apellido
        self.email=email
        self.numero=numero
        self.parent = None 
    def get_info(self):
      print (self.nombre,self.apellido,self.email,self.numero)
      return

class ABB:
    def __init__(self):
        self.root = None
    def empty(self):
        return self.root == None
    def _insertar(self,nombre,apellido,email,numero , node):
        if apellido < node.apellido:
            if node.left == None:
                node.left = Node(nombre,apellido,email,numero)
                node.left.parent = node
            else:
                self._insertar(nombre,apellido,email,numero , node.left)
        elif apellido > node.apellido:
            if node.right == None:
                node.right = Node(nombre,apellido,email,numero)
                node.right.parent = node
            else:
                self._insertar(nombre,apellido,email,numero, node.right)
        else:
            print("El apellido ya a sido ingresado")
    def insertar(self, nombre,apellido,email,numero):
        if self.empty():
            self.root = Node(nombre,apellido,email,numero)
        else:
            self._insertar(nombre,apellido,email,numero, self.root)
    def _buscar(self, apellido, node):
        if node.apellido == None:
           return node 
        elif apellido == node.apellido:
            print ("Nodo Encontrado:")
            node.get_info()
            return node 
        elif apellido < node.apellido and node.left != None:
            return self._buscar(apellido, node.left)
        elif apellido > node.apellido and node.right != None:
            return self._buscar(apellido, node.right)
        print("No encontrado")
    def buscar(self, apellido):
        if self.empty():
          print ("Sin Raiz")
          return None

        else:
            return self._buscar(apellido, self.root)
    def eliminar(self, apellido): 
        if self.empty():
            print ("Sin Raiz")
            return None
        return self.eliminar_nodo(self.buscar(apellido))

    def eliminar_nodo(self, node):
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        def number_children(n):
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = node.parent 
        node_children = number_children(node)

        if node_children == 0:
            print ("Sin padres")
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        if node_children == 1:
            print ("1 Hijo")
            if node.left != None:
                child = node.left
            else:
                child = node.right
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child
            child.parent = node_parent
        if node_children == 2:
            print ("2 Hijos")
            successor = min_value_node(node.right)
            node.apellido = successor.apellido 
            self.eliminar_nodo(successor)
        

    def imprimir(self, node): #Implementar
        if node is not None:
            self.imprimir(node.left)
            node.get_info()
            self.imprimir(node.right)
def imprimir (node):
  if node is not None:
    imprimir(node.left)
    node.get_info()
    imprimir(node.right)      
def hash1(key):
  return ord(key[0])-13
class Hash:
  def __init__(self,size=26):
    self.size=size
    self.lista=[None]*size
  def insertar_h(self, nombre,apellido,email,numero):
    pos=hash1(apellido)%self.size
    if self.lista[pos] is None:
      self.lista[pos]=ABB()
      self.lista[pos].insertar(nombre,apellido,email,numero)
    else:
      self.lista[pos].insertar(nombre,apellido,email,numero)
  def imprimir_h(self):
    for i in range (self.size):
      if self.lista[i] is not None:
        imprimir(self.lista[i].root)
      else:
        char = chr(i+65)
        print ("Sin Contacto en", char)
  def eliminar_h(self,apellido):
    pos=hash1(apellido)%self.size
    self.lista[pos].eliminar(apellido)
  def buscar_h(self,apellido):
    pos=hash1(apellido)%self.size
    self.lista[pos].buscar(apellido)
  
  
