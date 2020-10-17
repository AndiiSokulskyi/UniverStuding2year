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
            fid.set_id(f)
            f = file.readline().strip('\n')
            fid.set_country_code(f)
            f = file.readline().strip('\n')
            fid.set_passport_no(f)
            f = file.readline().strip('\n')
            fid.set_fname(f)
            f = file.readline().strip('\n')
            fid.set_lname(f)
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
                if i.get(dictio[j]) == iDn:
                    i.set(dictio[j], ed)

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