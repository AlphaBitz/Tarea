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
def eliminar_ABB(root, apellido):
        if root is None:
           return None
        if apellido < root.apellido:
           root.left = eliminar_ABB(root.left, apellido)
        elif apellido > root.apellido:
           root.right = eliminar_ABB(root.right, apellido)
        else:
            if root.left:
                new_root = root.left
                if root.right:
                    if new_root.right:
                        tmp = root.right
                        while tmp.left:
                            tmp = tmp.left
                        tmp.left = new_root.right
                        new_root.right = root.right
                    else:
                        new_root.right = root.right
            elif root.right:
                new_root = root.right
            else:
                new_root = None
            root = new_root
        return root 