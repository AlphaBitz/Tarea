# -*- coding: utf-8 -*-
# import node

class Node:
    def __init__(self,nombre,apellido,email,numero):
        self.nombre = nombre
        self.apellido=apellido
        self.email=email
        self.numero=numero
        self.next = None
        self.prev = None

class Lista:
    def __init__(self):
        self.head = None
        self.contador=0
        
    def empty(self):
        return self.head == None
    
    def insert(self,nombre,apellido,email,numero):
        n=Node(nombre,apellido,email,numero)
        if self.empty:
            n=self.head
            self.contador++
            return
        else:
            aux=self.head
            while aux.next:
                if aux.apellido<n.apellido:
                    n.next=aux.next
                    n.prev=aux
                    aux.next=n
                    n.next.prev=n
                    self.contador++
                    return
                elif aux.apellido==n.apellido:
                    return "Apellido Repetido"   
        
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

