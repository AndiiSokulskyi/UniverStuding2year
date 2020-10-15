# Клас ЗАКОРДОННИЙ ПАСПОРТ:
# id,
# country_code (e.g., ukr),
# passport_no (format: FU124356),
# name (first name and last name),
# date_of_issue,
# date_of_expire,
# date_of_birth.

from Validation import *

dictio={ 0 : 'id', 1 : 'country_code', 2 :'passport_no', 3 :'fname',4 : 'lname', 5 :'date_of_birth', 6 :'date_of_issue',7 : 'date_of_expire'}

class ForeignID:

    def __init__(self, id = None, country_code = None, passport_no = None,
                 fname = None, lname =None, date_of_birth = None,
                 date_of_issue = None ,date_of_expire = None):
        self.id = id
        self.country_code = country_code
        self.passport_no = passport_no
        self.fname = fname
        self.lname = lname
        self.date_of_birth = date_of_birth
        self.date_of_issue = date_of_issue
        self.date_of_expire = date_of_expire
        self.__valid()

    def __str__(self):
        strng=''
        for i in range(len(dictio)):
                strng += dictio[i] + ': ' + str(getattr(self, dictio[i])) + '\n'
        return strng

    def get(self, atrb):
        return getattr(self, atrb)

    def set(self, atrb, elem):
        setattr(self, atrb, elem)
        self.__valid()

    def __valid(self):
        self.id = Validation().id_valid(self.id)
        self.country_code = Validation().cc_valid(self.country_code)
        self.passport_no = Validation().pn_valid(self.passport_no)
        self.fname = Validation().alfa_valid(self.fname)
        self.lname = Validation().alfa_valid(self.lname)
        self.date_of_birth = Validation().birth_valid(self.date_of_birth)
        self.date_of_issue = Validation().issue_valid(self.date_of_issue, self.date_of_birth)
        self.date_of_expire = Validation().expire_valid(self.date_of_expire, self.date_of_issue)