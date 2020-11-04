import unittest
#from Prog6 import *
from Collection import *


class TestCase(unittest.TestCase):
    def setUp(self):
        self.cl = Collection()
        self.fid = ForeignID('16256496', 'ukr', 'AS123456', 'Andriy', 'Sokulskiy',
                             '2000-01-20', '2016-01-31', '2026-02-01')
        self.fid2 = ForeignID('48624563', 'pol', 'NK265485', 'Mykola', 'Kotsan',
                         '2000-09-27', '2014-10-07', '2024-10-28')
        self.fid3 = ForeignID('63245125', 'ukr', 'YT987456', 'Yurthik', 'Tyhonlyi',
                         '2000-06-06', '2018-01-20', '2028-01-21')

    def test_add_to_collec(self):
        self.cl.add_to_collec(self.fid3)
        self.assertIn(self.fid3, self.cl.get_collec())

    def test_add_from_file(self):
        file = open("TestFile.txt", "r")
        self.cl.add_from_file(file)
        file.close()
        for i in range(len(dictio)):
            self.assertEqual(self.fid.get(dictio[i]), self.cl.get_collec()[0].get(dictio[i]))
            self.assertEqual(self.fid2.get(dictio[i]), self.cl.get_collec()[1].get(dictio[i]))


    def test_add_to_file(self):
        self.cl.add_to_collec(self.fid)
        self.cl.add_to_collec(self.fid2)
        self.cl.add_to_collec(self.fid3)

        file = open("TestFile.txt", "w")
        self.cl.add_to_file(file)
        file.close()

        file = open("TestFile.txt", "r")
        self.cl.add_from_file(file)
        file.close()

        for i in range(len(dictio)):
            self.assertEqual(self.fid.get(dictio[i]), self.cl.get_collec()[0].get(dictio[i]))
            self.assertEqual(self.fid2.get(dictio[i]), self.cl.get_collec()[1].get(dictio[i]))
            self.assertEqual(self.fid3.get(dictio[i]), self.cl.get_collec()[2].get(dictio[i]))


    def test_delete_from_collec(self):
        self.cl.add_to_collec(self.fid)
        self.cl.add_to_collec(self.fid2)
        self.cl.add_to_collec(self.fid3)

        self.cl.delete_from_collec('pol')
        for i in range(len(dictio)):
            self.assertEqual(self.fid.get(dictio[i]), self.cl.get_collec()[0].get(dictio[i]))
            self.assertEqual(self.fid3.get(dictio[i]), self.cl.get_collec()[1].get(dictio[i]))
            self.assertEqual(len(self.cl.get_collec()), 2)


    def test_delete_from_file(self):
        self.cl.add_to_collec(self.fid)
        self.cl.add_to_collec(self.fid2)
        self.cl.add_to_collec(self.fid3)
        cl1 = Collection()

        file = open("TestFile.txt", "w")
        self.cl.delete_from_file(file, '63245125')
        file.close()

        file = open("TestFile.txt", "r")
        cl1.add_from_file(file)
        file.close()

        for i in range(len(dictio)):
            self.assertEqual(self.fid.get(dictio[i]), cl1.get_collec()[0].get(dictio[i]))
            self.assertEqual(len(cl1.get_collec()), 2)

    def test_edit_collec(self):
        self.cl.add_to_collec(self.fid)
        self.cl.add_to_collec(self.fid2)

        self.cl.edit_collec('country_code', 'pol')
        for i in range(len(dictio)):
            self.assertEqual('pol', self.cl.get_collec()[0].get(dictio[1]))
            self.assertEqual('pol', self.cl.get_collec()[1].get(dictio[1]))

    def test_edit_file(self):
        self.cl.add_to_collec(self.fid)
        self.cl.add_to_collec(self.fid2)

        cl1 = Collection()

        file = open("TestFile.txt", "w")
        self.cl.edit_file(file, 'country_code', 'pol')
        file.close()

        file = open("TestFile.txt", "r")
        cl1.add_from_file(file)
        file.close()

        self.cl.edit_collec('country_code', 'pol')
        for i in range(len(dictio)):
            self.assertEqual('pol', cl1.get_collec()[0].get(dictio[1]))
            self.assertEqual('pol', cl1.get_collec()[1].get(dictio[1]))

    def test_find_in_collec(self):
        self.cl.add_to_collec(self.fid)
        self.cl.add_to_collec(self.fid2)

    def test_sort_of_collec(self):
        self.cl.add_to_collec(self.fid)
        self.cl.add_to_collec(self.fid2)
        self.cl.add_to_collec(self.fid3)
        self.cl.sort_of_collec('0')
        cl1 = sorted(self.cl.collec, key=lambda col: col.get(dictio[int('0')]).upper())




if __name__ == '__main__':
    unittest.main()
