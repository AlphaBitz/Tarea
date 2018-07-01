from Lista import Nodo_L
from Lista import Lista
from ABB import Nodo_ABB
from ABB import ABB
from ABB import eliminar_ABB
from Hashing import Hashing
from AVL import AVL
from AVL import Nodo

class Estructura:
  def menu1(self):
   print("Bienvenido!")
   print ("Seleccione el tipo de estructura:")
   print("1.Lista Simple")
   print("2.Arbol Binario de Busqueda")
   print("3.AVL")
   print("4.Hashing")
   opcion1=input("Ingrese su selección:")
   return opcion1
  def menu2(self,opcion1):
    print ()
    print ("¿Que acción desea realizar?")
    print ("1.Añadir contacto")
    print ("2.Eliminar contacto")
    print ("3.Buscar contacto")
    print ("4.Imprimir contactos")
    opcion2=input ("Ingrese su selección:")
    return opcion2
  def menuanadir(self,opcion1,opcion2,lista,abb,hashing,avl,root):
        print (opcion2)
        if opcion2=="1":
          print ()
          print("Ingrese los datos:")
          nombre=input("Nombre:")
          apellido=input("Apellido:")
          email=input("Email:")
          numero=input("Numero:")
          if opcion1=="1":
            lista.insertar_L(nombre,apellido,email,numero)
          if opcion1=="2":
                 abb.insertar_ABB(nombre,apellido,email,numero)
          if opcion1=="3":
                 root = avl.insertar_a (root, nombre,apellido,email,numero)
          if opcion1=="4":
                 hashing.insertar_h(nombre,apellido,email,numero)
  def menueliminar(self,opcion1,opcion2,lista,abb,hashing,avl,root):
         if opcion2=="2":
            print ()
            eliminar=input("Ingrese el apellido a eliminar:")
            if opcion1=="1":
              lista.eliminar_L(eliminar)
            if opcion1=="2":
               deleteNode(abb.root,eliminar)
            if opcion1=="3":
                 avl.eliminar_a(root,eliminar)
            if opcion1=="4":
                 hashing.eliminar_h(eliminar)
  def menubuscar (self,opcion1,opcion2,lista,abb,hashing,avl,root):
          if opcion2=="3":
             print ()
             buscar=input("Ingrese el apellido a buscar:")
             if opcion1=="1":
               lista.buscar_L(buscar)
             if opcion1=="2":
                 abb.buscar_ABB(buscar)
             if opcion1=="3":
                 avl.buscar_a(root,buscar)
             if opcion1=="4":
                 hashing.buscar_h(buscar)
  def menuimprimir(self,opcion1,opcion2,lista,abb,hashing,avl,root):
          if opcion2=="4":
              print ()
              print ("A continuación se imprimira la lista:")
              if opcion1=="1":
                lista.imprimir_L()
              if opcion1=="2":
                 abb.imprimir_ABB(abb.root)
              if opcion1=="3":
                 avl.imprimir_a(root)
              if opcion1=="4":
                 hashing.imprimir_h()
  def salir(self):
      print ()
      salir=input("¿Desea Salir?, Ingrese Si o No:")
      if salir=="Si" or salir=="si":
          print ("¡Hasta luego!")
          input()
          return False
      else:
          return True
      

a=Estructura()
lista=Lista()
abb=ABB()
hashing=Hashing()
avl=AVL()
root=None
b=True
opcion1=a.menu1()
while b:
    opcion2=a.menu2(opcion1)
    a.menuanadir(opcion1,opcion2,lista,abb,hashing,avl,root)
    a.menueliminar(opcion1,opcion2,lista,abb,hashing,avl,root)
    a.menubuscar(opcion1,opcion2,lista,abb,hashing,avl,root)
    a.menuimprimir(opcion1,opcion2,lista,abb,hashing,avl,root)
    b=a.salir()
