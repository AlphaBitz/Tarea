from Lista_Time import Nodo_L
from Lista_Time import Lista
import time
from faker import Faker
fake = Faker()
lista=Lista()
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



