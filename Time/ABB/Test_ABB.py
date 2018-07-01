import time
from ABB_Time import ABB
from ABB_Time import Nodo_ABB
from ABB_Time import eliminar_ABB
from faker import Faker
fake = Faker()
abb=ABB()
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
print("Inicio, Buscando 10 contactos en ABB")
print (time.asctime())
for i in range(0,10):
    b=fake.name().split(" ")
    nombre=b[0]
    apellido=b[1]
    email=fake.email()
    numero=fake.address()
    abb.buscar_ABB(apellido)
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
    abb.buscar_ABB(apellido)
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
    abb.buscar_ABB(apellido)
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
    abb.buscar_ABB(apellido)
print("Final, Buscando 1000 contactos en ABB")
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
    eliminar_ABB(abb.root,apellido) 
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
    eliminar_ABB(abb.root,apellido) 
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
    eliminar_ABB(abb.root,apellido) 
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
    eliminar_ABB(abb.root,apellido) 
print("Final, Eliminando 1000 contactos a ABB")
print (time.asctime())
input()
