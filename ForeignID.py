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
dictio1={ 0 : 'set_id', 1 : 'set_country_code', 2 :'set_passport_no', 3 :'set_fname',4 : 'set_lname', 5 :'set_date_of_birth', 6 :'set_date_of_issue',7 : 'set_date_of_expire'}

class ForeignID:

    def __init__(self, id = None, country_code = None, passport_no = None,
                 fname = None, lname =None, date_of_birth = None,
                 date_of_issue = None ,date_of_expire = None):

        self.set_id(id)
        self.set_country_code(country_code)
        self.set_passport_no(passport_no)
        self.set_fname(fname)
        self.set_lname(lname)



    def __str__(self):
        strng=''
        for i in range(len(dictio)):
                strng += dictio[i] + ': ' + str(getattr(self, dictio[i])) + '\n'
        return strng

    def get(self, atrb):
        return getattr(self, atrb)

