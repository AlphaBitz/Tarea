class Nodo():
    def __init__(self, nombre,apellido,email,numero):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.numero=numero
        self.left = None
        self.right = None
        self.altura = 1
    def get_info(self):
      print (self.nombre,self.apellido,self.email,self.numero)
      return
class AVL():
    def insertar_a(self,root,nombre,apellido,email,numero):
      if root is None:
            return Nodo(nombre,apellido,email,numero)
      elif root.apellido==apellido:
        print ("Ya existe el apellido:", root.apellido)
        return root
      elif apellido < root.apellido:
            root.left = self.insertar_a(root.left, nombre,apellido,email,numero)
      else:
            root.right = self.insertar_a(root.right, nombre,apellido,email,numero)  #Actua de la misma manera que un ABB
      root.altura = 1 + max(self.get_altura(root.left),self.get_altura(root.right)) #Actualiza la altura del nodo anterior
      balance = self.get_balance(root)  #Obtiene el balance, Si esta desbalanceado, busca el caso correcto para balancear
      if balance > 1 and apellido < root.left.apellido: #LL
            return self.rightRotate(root)
      if balance < -1 and apellido > root.right.apellido: #RR
            return self.leftRotate(root)
      if balance > 1 and apellido > root.left.apellido: #LR
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
      if balance < -1 and apellido < root.right.apellido: #RL
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
      return root
    def valor_min(self, root):
        if root is None or root.left is None:
            return root
        return self.valor_min(root.left)
    def eliminar_a(self, root, apellido):
        if root is None:
            return root
        elif apellido < root.apellido:
            root.left = self.eliminar_a(root.left, apellido)
        elif apellido > root.apellido:
            root.right = self.eliminar_a(root.right, apellido) #Actua de la misma manera que un ABB
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.valor_min(root.right)
            root.apellido = temp.apellido
            root.right = self.eliminar_a(root.right,temp.apellido)
        if root is None: #Si el arbol tiene un nodo, lo retorna
            return root  
        root.height = 1 + max(self.get_altura(root.left), self.get_altura(root.right))   #Actualiza la altura 
        balance = self.get_balance(root) #Obtiene el factor de balance
        if balance > 1 and self.get_balance(root.left) >= 0: #LL
            return self.rightRotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0: #RR
            return self.leftRotate(root)
        if balance > 1 and self.get_balance(root.left) < 0: #LR
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.get_balance(root.right) > 0: #RL
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def leftRotate(self, z):
        y = z.right
        T2 = y.left #Realiza la Rotacion
        y.left = z
        z.right = T2 #Actualiza la altura
        z.altura = 1 + max(self.get_altura(z.left),
                         self.get_altura(z.right))
        y.altura = 1 + max(self.get_altura(y.left),
                         self.get_altura(y.right)) 
        return y #Devuelve la nueva raiz
    def rightRotate(self, z):
        y = z.left
        T3 = y.right #Realiza la Rotacion
        y.right = z
        z.left = T3 #Actualiza la altura
        z.altura = 1 + max(self.get_altura(z.left),
                        self.get_altura(z.right))
        y.altura = 1 + max(self.get_altura(y.left),
                        self.get_altura(y.right))
        return y #Devuelve la nueva raiz
    def get_altura(self, root):
        if root is None:
            return 0
        return root.altura
    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_altura(root.left) - self.get_altura(root.right) 
    def imprimir_a(self, root): #Inorder Corriente
        if root is None:
            return
        self.imprimir_a(root.left)
        root.get_info()
        self.imprimir_a(root.right)
    def buscar_a(self,root,apellido): #Similar al del arbol ABB
        if root is None:
            print ("Sin Raiz")
            return None
        else:
         if root.apellido == None:
           return  
         elif apellido == root.apellido:
            print ("Nodo Encontrado:")
            root.get_info()
            return  
         elif apellido < root.apellido and root.left != None:
            return self.buscar_a(root.left,apellido)
         elif apellido > root.apellido and root.right != None:
            return self.buscar_a(root.right,apellido)
         print ("No encontrado")     
