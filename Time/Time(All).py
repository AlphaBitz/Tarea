#Insercion:
#Tiempo Lista:10 contactos >1 seg -- 20 contactos >1 seg --100 contactos >1 seg -- 1000 contactos 5>x>4 segs
#Tiempo ABB: 10 contactos >1 seg -- 20 contactos >1 seg --100 contactos >1 seg -- 1000 contactos >4 segs
#tiempo AVL:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos >1 seg -- 1000 contactos >4 segs
#Tiempo Hash:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos >1 seg -- 1000 contactos 6>x>5 segs
#Busqueda:
#Tiempo Lista:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos 3>x>2 seg -- 1000 contactos 20 segs
#Tiempo ABB: 10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos >2 seg -- 1000 contactos 22 segs 
#tiempo AVL:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos >2 seg -- 1000 contactos 16 segs
#Tiempo Hash:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos >3 seg -- 1000 contactos 22 segs
#Eliminar:
#Tiempo Lista:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos 3>x>2 seg -- 1000 contactos 10 segs
#Tiempo ABB:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos >1 seg -- 1000 contactos ? segs
#tiempo AVL:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos >1 seg -- 1000 contactos 2 segs
#Tiempo Hash:10 contactos >1 seg -- 20 contactos >1 seg -- 100 contactos >1 seg -- 1000 contactos ? segs
from Lista import Nodo_L
from Lista import Lista
from ABB_Time import Nodo_ABB
from ABB_Time import eliminar_ABB
from Hashing_Time_Test import Hashing
from AVL_Time import AVL
from AVL_Time import Nodo
from ABB_Time import eliminar_ABB
import time
from faker import Faker
fake = Faker()
lista=Lista()
abb=ABB()
hashing=Hashing()
avl=AVL()
root=None
print("Inicio, Añadiendo 10 contactos a lista")
print(time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.insertar_L(nombre,apellido,email,numero)
print("Final, Añadiendo 10 contactos a lista")
print (time.asctime())
input()
print("Inicio, Añadiendo 20 contactos a lista")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.insertar_L(nombre,apellido,email,numero)
print("Final, Añadiendo 20 contactos a lista")
print (time.asctime())
input()
print("Inicio, Añadiendo 100 contactos a lista")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.insertar_L(nombre,apellido,email,numero)
print("Final, Añadiendo 100 contactos a lista")
print (time.asctime())
input() 
print("Inicio, Añadiendo 1000 contactos a lista")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.insertar_L(nombre,apellido,email,numero)
print("Final, Añadiendo 1000 contactos a lista")
print (time.asctime())
input()
print("Inicio, Añadiendo 10 contactos a ABB")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.insertar_ABB(nombre,apellido,email,numero)
print("Final, Añadiendo 10 contactos a ABB")
print (time.asctime())
input()
print("Inicio, Añadiendo 20 contactos a ABB")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.insertar_ABB(nombre,apellido,email,numero)
print("Final, Añadiendo 20 contactos a ABB")
print (time.asctime())
input()
print("Inicio, Añadiendo 100 contactos a ABB")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.insertar_ABB(nombre,apellido,email,numero)
print("Final, Añadiendo 100 contactos a ABB")
print (time.asctime())
input() 
print("Inicio, Añadiendo 1000 contactos a ABB")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.insertar_ABB(nombre,apellido,email,numero)
print("Final, Añadiendo 1000 contactos a ABB")
print (time.asctime())
input()  
print("Inicio, Añadiendo 10 contactos a AVL")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    root= avl.insertar_a(root,nombre,apellido,email,numero)
print("Final, Añadiendo 10 contactos a AVL")
print (time.asctime())
input()
print("Inicio, Añadiendo 20 contactos a AVL")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    root= avl.insertar_a(root,nombre,apellido,email,numero)
print("Final, Añadiendo 20 contactos a AVL")
print(time.asctime())
input()
print("Inicio, Añadiendo 100 contactos a AVL")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    root= avl.insertar_a(root,nombre,apellido,email,numero)
print("Final, Añadiendo 100 contactos a AVL")
print (time.asctime())
input() 
print("Inicio, Añadiendo 1000 contactos a AVL")
print (time.asctime())
for i in range(0,400):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    root= avl.insertar_a(root,nombre,apellido,email,numero)
print("Final, Añadiendo 1000 contactos a AVL")
print (time.asctime())
input()
print("Inicio, Añadiendo 10 contactos a Hash")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.insertar_h(nombre,apellido,email,numero)
print("Final, Añadiendo 10 contactos a Hash")
print (time.asctime())
input()
print("Inicio, Añadiendo 20 contactos a Hash")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.insertar_h(nombre,apellido,email,numero)
print("Final, Añadiendo 20 contactos a Hash")
print (time.asctime())
input()
print("Inicio, Añadiendo 100 contactos a Hash")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.insertar_h(nombre,apellido,email,numero)
print("Final, Añadiendo 100 contactos a Hash")
print (time.asctime())
input() 
print("Inicio, Añadiendo 1000 contactos a Hash")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.insertar_h(nombre,apellido,email,numero)
print("Final, Añadiendo 1000 contactos a Hash")
print (time.asctime())
input()
print("Inicio, Buscando 10 contactos en lista")
print(time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.buscar_L(apellido)
print("Final, Buscando 10 contactos en lista")
print (time.asctime())
input()
print("Inicio, Buscando 20 contactos en lista")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.buscar_L(apellido)
print("Final, Buscando 20 contactos en lista")
print (time.asctime())
input()
print("Inicio, Buscando 100 contactos en lista")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.buscar_L(apellido)
print("Final, Buscando 100 contactos en lista")
print (time.asctime())
input() 
print("Inicio, Buscando 1000 contactos en lista")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.buscar_L(apellido)
print("Final, Buscando 1000 contactos a lista")
print (time.asctime())
input()
print("Inicio, Buscando 10 contactos en ABB")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.buscar_ABB(abb.root,apellido)
print("Final, Buscando 10 contactos en ABB")
print (time.asctime())
input()
print("Inicio, Buscando 20 contactos en ABB")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.buscar_ABB(abb.root,apellido)
print("Final, Buscando 20 contactos en ABB")
print (time.asctime())
input()
print("Inicio, Buscando 100 contactos en ABB")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.buscar_ABB(abb.root,apellido)
print("Final, Buscando 100 contactos en ABB")
print (time.asctime())
input() 
print("Inicio, Buscando 1000 contactos en ABB")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.buscar_ABB(abb.root,apellido)
print("Final, Buscando 1000 contactos en ABB")
print (time.asctime())
input()  
print("Inicio, Buscando 10 contactos en AVL")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    avl.buscar_a(root,apellido)
print("Final, Buscando 10 contactos en AVL")
print (time.asctime())
input()
print("Inicio, Buscando 20 contactos en AVL")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    avl.buscar_a(root,apellido)
print("Final, Buscando 20 contactos en AVL")
print(time.asctime())
input()
print("Inicio, Buscando 100 contactos en AVL")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    avl.buscar_a(root,apellido)
print("Final, Buscando 100 contactos en AVL")
print (time.asctime())
input() 
print("Inicio, Buscando 1000 contactos en AVL")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    avl.buscar_a(root,apellido)
print("Final, Buscando 1000 contactos en AVL")
print (time.asctime())
input()
print("Inicio, Buscando 10 contactos en Hash")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.buscar_h(apellido)
print("Final, Buscando 10 contactos en Hash")
print (time.asctime())
input()
print("Inicio, Buscando 20 contactos en Hash")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.buscar_h(apellido)
print("Final, Buscando 20 contactos en Hash")
print (time.asctime())
input()
print("Inicio, Buscando 100 contactos en Hash")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.buscar_h(apellido)
print("Final, Buscando 100 contactos en Hash")
print (time.asctime())
input() 
print("Inicio, Buscando 1000 contactos en Hash")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.buscar_h(apellido)
print("Final, Buscando 1000 contactos en Hash")
print (time.asctime())
input()
print("Inicio, Eliminando 10 contactos a lista")
print(time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.eliminar_L(apellido)
print("Final, Eliminando 10 contactos a lista")
print (time.asctime())
input()
print("Inicio, Eliminando 20 contactos a lista")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.eliminar_L(apellido)
print("Final, Eliminando 20 contactos a lista")
print (time.asctime())
input()
print("Inicio, Eliminando 100 contactos a lista")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.eliminar_L(apellido)
print("Final, Eliminando 100 contactos a lista")
print (time.asctime())
input() 
print("Inicio, Eliminando 1000 contactos a lista")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    lista.eliminar_L(apellido)
print("Final, Eliminando 1000 contactos a lista")
print (time.asctime())
input()
print("Inicio, Eliminando 10 contactos a ABB")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    deleteNode(abb.root,apellido)
print("Final, Eliminando 10 contactos a ABB")
print (time.asctime())
input()
print("Inicio, Eliminando 20 contactos a ABB")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    deleteNode(abb.root,apellido)
print("Final, Eliminando 20 contactos a ABB")
print (time.asctime())
input()
print("Inicio, Eliminando 100 contactos a ABB")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    deleteNode(abb.root,apellido)
print("Final, Eliminando 100 contactos a ABB")
print (time.asctime())
input() 
print("Inicio, Eliminando 1000 contactos a ABB")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    deleteNode(abb.root,apellido)
print("Final, Eliminando 1000 contactos a ABB")
print (time.asctime())
input()  
print("Inicio, Eliminando 10 contactos a AVL")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    avl.eliminar_a(root,apellido)
print("Final, Eliminando 10 contactos a AVL")
print (time.asctime())
input()
print("Inicio, Eliminando 20 contactos a AVL")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    avl.eliminar_a(root,apellido)
print("Final, Eliminando 20 contactos a AVL")
print(time.asctime())
input()
print("Inicio, Eliminando 100 contactos a AVL")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    avl.eliminar_a(root,apellido)
print("Final, Eliminando 100 contactos a AVL")
print (time.asctime())
input() 
print("Inicio, Eliminando 1000 contactos a AVL")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    avl.eliminar_a(root,apellido)
print("Final, Eliminando 1000 contactos a AVL")
print (time.asctime())
input()
print("Inicio, Eliminando 10 contactos a Hash")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.eliminar_h(apellido)
print("Final, Eliminando 10 contactos a Hash")
print (time.asctime())
input()
print("Inicio, Eliminando 20 contactos a Hash")
print (time.asctime())
for i in range(0,20):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.eliminar_h(apellido)
print("Final, Eliminando 20 contactos a Hash")
print (time.asctime())
input()
print("Inicio, Eliminando 100 contactos a Hash")
print (time.asctime())
for i in range(0,100):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.eliminar_h(apellido)
print("Final, Eliminando 100 contactos a Hash")
print (time.asctime())
input() 
print("Inicio, Eliminando 1000 contactos a Hash")
print (time.asctime())
for i in range(0,1000):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    hashing.eliminar_h(apellido)
print("Final, Eliminando 1000 contactos a Hash")
print (time.asctime())
input()
