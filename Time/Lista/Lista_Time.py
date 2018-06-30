class Nodo_L:
    def __init__(self,nombre,apellido,email,numero):
        self.nombre = nombre
        self.apellido=apellido
        self.email=email
        self.numero=numero
        self.next = None
    def get_info(self):
      print(self.nombre,self.apellido,self.email,self.numero)
      return        
class Lista:
    def __init__(self):
        self.head = None
        self.contador=0
    def insertar_L(self,nombre,apellido,email,numero):
        n=Nodo_L(nombre,apellido,email,numero)
        if self.head is None:
            self.head=n
            self.contador += 1
            return "ingresado como cabeza"
        else:
            aux=self.head
            while aux is not None:
                if aux.apellido>n.apellido:
                   n.next=aux
                   self.head=n
                   self.contador += 1
                   return "Ingresado atras"
                if aux.apellido==n.apellido:
                  return False
                if n.apellido>aux.apellido and aux.next is None:
                  aux.next=n
                  self.contador += 1
                  return
                if n.apellido>aux.apellido and n.apellido<aux.next.apellido:
                  n.next=aux.next
                  aux.next=n
                  self.contador += 1
                  return
                aux=aux.next
    def buscar_L(self,apellido):
      if self.head is None:
        print ("Lista Vacia")
      else:
        pointer=self.head
        a=False
        while pointer is not None:
          if apellido==pointer.apellido:
            print("Contacto Encontrado")
            return
          pointer=pointer.next   
        print ("Apellido no encontrado")
        return
    def imprimir_L(self):
        if self.head is None:
             print("Lista vacia")
             return
        else:
            pointer = self.head
            while pointer is not None:
                pointer.get_info()
                pointer=pointer.next
    def eliminar_L (self,apellido):
      if self.head is None:
        print ("Lista vacia")
        return
      if self.head.apellido==apellido:
        self.head=self.head.next
        self.contador -= 1
        print ("Apellido eliminado")
        return
      else:
        prev=self.head
        temp=self.head.next
        while temp is not None:
          if temp.apellido==apellido:
            prev.next=temp.next
            self.contador -= 1
            print ("Apellido eliminado")
            return
          prev=prev.next
          temp=temp.next
        print ("Apellido no encontrado")

