from ForeignID import *

class Collection:

    def __init__(self):
        self.collec = []

    def __str__(self):
        strng = ''
        for i in self.collec:
            strng += str(i) + '\n'
        return strng

    def add_to_collec(self, elem):
        self.collec.append(elem)

    def add_from_file(self, file):
        while True:
            fid = ForeignID()
            f = file.readline().strip('\n')
            if not f:
                break
            for i in range (5):
                getattr(fid, dictio1[i])(f)
                f = file.readline().strip('\n')
            fid.set_date_of_birth(f, None)
            f = file.readline().strip('\n')
            fid.set_date_of_issue(f, fid.get('date_of_birth'))
            f = file.readline().strip('\n')
            fid.set_date_of_expire(f, fid.get('date_of_issue'))
            f = file.readline().strip('\n')
            self.add_to_collec(fid)

    def add_to_file(self, file):
        for i in self.collec:
            for j in range(8):
                file.write(getattr(i, dictio[j]))
                file.write('\n')
            file.write('\n')

    def delete_from_collec(self, iDn):
        del_em = []
        for i in self.collec:
            for j in range(8):
                if i.get(dictio[j]) == iDn:
                    del_em.append(i)
                    break
        for k in del_em:
            self.collec.remove(k)

    def delete_from_file(self, file, iDn):
        self.delete_from_collec(iDn)
        self.add_to_file(file)

    def edit_collec(self, iDn, ed):
        for i in self.collec:
            for j in range(8):
                if dictio[j] == iDn:
                    getattr(i, dictio1[j])(ed)


    def edit_file(self, file, iDn, ed):
        self.edit_collec(iDn, ed)
        self.add_to_file(file)

    def find_in_collec(self, string):
        tempo = Collection()
        for i in self.collec:
            for j in range(len(dictio)):
                if string == str(i.get(dictio[j]))[0:len(string)]:
                    tempo.add_to_collec(i)
        if tempo == []:
            return
        else:
            return tempo

    def sort_of_collec(self, atrb):
        self.collec = sorted(self.collec, key=lambda col: col.get(dictio[int(atrb)]).upper())

    def save(self):
        return Memento(self.collec)

    def restore(self, mem=None):
        self.collec = mem.get_collection()


class Memento:
    def __init__(self, collection):
        self._collection = []
        for i in collection:
            fid = ForeignID(i.get(dictio[0]), i.get(dictio[1]), i.get(dictio[2]), i.get(dictio[3]),
                            i.get(dictio[4]), i.get(dictio[5]), i.get(dictio[6]), i.get(dictio[7]))
            self._collection.append(fid)

    def get_collection(self):
        return self._collection


class Caretaker:
    def __init__(self, collection=None):
        self._mementos = []
        self._remementos = []
        self._collection = collection

    def backup(self):
        if len(self._mementos) == 5:
            for i in range(4):
                self._mementos[i] = self._mementos[i+1]
            self._mementos[4] = self._collection.save()
        self._mementos.append(self._collection.save())

    def undo(self):
        if len(self._mementos) == 0:
            return
        self._remementos.append(self._collection.save())
        memo = self._mementos.pop()
        try:
            self._collection.restore(memo)
        except Exception:
            self.undo()

    def redo(self):
        if len(self._remementos) == 0:
            return
        rememo = self._remementos.pop()
        try:
            self._collection.restore(rememo)
        except Exception:
            self.redo()
