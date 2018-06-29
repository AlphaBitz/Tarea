#Tiempo Lista:10 contactos >1 seg, 20 contactos >1 seg,100 contactos >1 seg, 1000 contactos 5>x>4 segs
#Tiempo ABB: 10 contactos >1 seg, 20 contactos >1 seg,100 contactos >1 seg, 1000 contactos >4 segs
#tiempo AVL:10 contactos >1 seg, 20 contactos >1 seg,100 contactos >1 seg, 1000 contactos >4 segs
#Tiempo Hash:10 contactos >1 seg, 20 contactos >1 seg,100 contactos >1 seg,1000 contactos 6>x>5 segs
from Lista import Nodo_L
from Lista import Lista
from ABB import Nodo_ABB
from ABB import ABB
from Hashing import Hashing
from AVL import AVL
from AVL import Nodo
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

