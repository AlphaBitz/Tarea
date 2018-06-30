from AVL import Nodo
from AVL import AVL
import time
from faker import Faker
fake = Faker()    
avl = AVL()
root=None
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
avl.imprimir_a(root)
