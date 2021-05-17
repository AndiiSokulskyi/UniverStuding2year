from Observer import *

class Node:

    def __init__(self, data, NextPtr = None):
        self.data = data
        self.NextPtr = NextPtr

    def get_data(self):
        return self.data

class LinkedList:

    def __init__(self):
        self.head = None

    def __getitem__(self, indx):
        id = 0
        tempo = self.head
        while id != indx:
            tempo = tempo.NextPtr
            id += 1
        return tempo

    def __str__(self):
        strng = ''
        for i in range(0, self.length()):
            strng += ' ' + str(self[i].get_data())
        return strng


    def push_back(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            tempo = self.head
            while (tempo.NextPtr != None):
                tempo = tempo.NextPtr
            tempo.NextPtr = Node(data)

    def pop(self):
        tempo = self.head
        if tempo == None:
            return None
        while (tempo.NextPtr != None):
            prev = tempo
            tempo = tempo.NextPtr
        elem = tempo.data
        prev.NextPtr = None
        return elem

    def copy(self):
        ll = LinkedList()
        for i in range(self.length()):
            ll.push_back(self[i].get_data())
        return ll


    def lclear(self):
        self.head = None

    def lprint(self):
        tempo = self.head
        while tempo != None:
            print(tempo.get_data())
            tempo = tempo.NextPtr

    def length(self):
        len = 0
        tempo = self.head
        while tempo != None:
            tempo = tempo.NextPtr
            len += 1
        return len

    def linsert(self, indx, data):
        tempo = self[indx]
        newelem = Node(data)
        newelem.NextPtr = tempo.NextPtr
        tempo.NextPtr = newelem

    def ldel(self, indx, obs, indx2=None):
        if self.length() != 0:
            temp_l = self.copy()
            if indx2==None:
                if indx == 0:
                    self.head = self[1]
                else:
                    tempo = self[indx-1]
                    tempo.NextPtr = tempo.NextPtr.NextPtr
                e = Event("delete", temp_l, indx, self)
                e.notify(obs)
            else:
                while indx2 >= self.length():
                    indx2 = self.length()-1
                if indx < 0:
                    indx = 0
                if indx2 < indx:
                    indx, indx2 = indx2, indx
                j = self[indx2]
                while self[indx] != j:
                    if indx == 0:
                        self.head = self[1]
                    else:
                        tempo = self[indx - 1]
                        tempo.NextPtr = tempo.NextPtr.NextPtr
                tempo = self[indx - 1]
                tempo.NextPtr = tempo.NextPtr.NextPtr
                e = Event("delete", temp_l, indx, self, indx2)
                e.notify(obs)


    def lsort(self):
       tempo = self.head
       if tempo == None:
           return
       while tempo!= None:
           temp1 = self.head
           while temp1 != None:
               if temp1.data > tempo.data:
                   temp1.data, tempo.data = tempo.data, temp1.data
               temp1 = temp1.NextPtr
           tempo = tempo.NextPtr