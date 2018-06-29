class Nodo_ABB:
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
                node.left = Nodo_ABB(nombre,apellido,email,numero)
                node.left.parent = node
            else:
                self._insertar(nombre,apellido,email,numero , node.left)
        elif apellido > node.apellido:
            if node.right == None:
                node.right = Nodo_ABB(nombre,apellido,email,numero)
                node.right.parent = node
            else:
                self._insertar(nombre,apellido,email,numero, node.right)
        else:
            print("El apellido ya a sido ingresado")
    def insertar_ABB(self, nombre,apellido,email,numero):
        if self.empty():
            self.root = Nodo_ABB(nombre,apellido,email,numero)
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
    def buscar_ABB(self, apellido):
        if self.empty():
          print ("Sin Raiz")
          return None
        else:
            return self._buscar(apellido, self.root)

    def imprimir_ABB(self, node):
        if node==None:
            pass
        else:
            self.imprimir_ABB(node.left)
            node.get_info()
            self.imprimir_ABB(node.right)
def deleteNode(root, apellido):
    def minValueNode( node):
      current = node
      while(current.left is not None):
        current = current.left  
      return current 
    if root is None:
        return root 
    if apellido < root.apellido:
        root.left = deleteNode(root.left, apellido)
    elif apellido > root.apellido:
        root.right = deleteNode(root.right, apellido)
    else:
        if root.left is None :
            temp = root.right 
            root = None
            return temp              
        elif root.right is None :
            temp = root.left 
            root = None
            return temp
        temp = minValueNode(root.right)
        root.apellido = temp.apellido
        root.right = deleteNode(root.right , temp.apellido)
    return root 
class Hashing:
  def __init__(self,size=26):
    self.size=size
    self.lista=[None]*size
  def hash1(self,key):
      return ord(key[0])-13
  def insertar_h(self, nombre,apellido,email,numero):
    pos=self.hash1(apellido)%self.size
    if self.lista[pos] is None:
      self.lista[pos]=ABB()
      self.lista[pos].insertar_ABB(nombre,apellido,email,numero)
    else:
      self.lista[pos].insertar_ABB(nombre,apellido,email,numero)
  def imprimir_h(self):
    def imprimir (node):
       if node is not None:
         imprimir(node.left)
         node.get_info()
         imprimir(node.right)
    for i in range (self.size):
      if self.lista[i] is not None:
        imprimir(self.lista[i].root)
      else:
        char = chr(i+65)
        print ("Sin Contacto en", char)
  def eliminar_h(self,apellido):
    pos=self.hash1(apellido)%self.size
    self.lista[pos].deleteNode(self.lista[pos].root, apellido)
  def buscar_h(self,apellido):
    pos=self.hash1(apellido)%self.size
    self.lista[pos].buscar_ABB(apellido)

