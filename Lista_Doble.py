# -*- coding: utf-8 -*-
# import node

class Node:
    def __init__(self,nombre,apellido,email,numero):
        self.nombre = nombre
        self.apellido=apellido
        self.email=email
        self.numero=numero
        self.next_node = None
        self.after_node =None
        self.contador= 0

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def insert(self,nombre,apellido,email,numero):
        n=Node(nombre,apellido,email,numero)
        

    def insert_first(self, element):
        if self.empty():
            self.head = Node(element)
            self.tail = self.head
        else:
            node = Node(element)
            node.next_node = self.head
            self.head = node

    def print_list(self):
        if self.empty():
             print("Lista vacia")
        else:
            temp = self.head
            i = 1
            seguir = True
            while seguir:
                print("Nodo {} contiene el número {}".format(i, temp.data))
                temp = temp.next_node
                i += 1
                if temp == None:
                    break

