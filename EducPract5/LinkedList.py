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

    def ldel(self, indx):
        if indx == 0:
            self.lclear()
        else:
            tempo = self[indx-1]
            tempo.NextPtr = tempo.NextPtr.NextPtr

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