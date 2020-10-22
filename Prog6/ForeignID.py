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
        for i in range(len(dictio)):
            setattr(self, dictio[i], None)
        self.set_id(id)
        self.set_country_code(country_code)
        self.set_passport_no(passport_no)
        self.set_fname(fname)
        self.set_lname(lname)
        self.set_date_of_birth(date_of_birth, None)
        self.set_date_of_issue(date_of_issue, self.date_of_birth)
        self.set_date_of_expire(date_of_expire, self.date_of_issue)


    def __str__(self):
        strng=''
        for i in range(len(dictio)):
                strng += dictio[i] + ': ' + str(getattr(self, dictio[i])) + '\n'
        return strng

    def get(self, atrb):
        return getattr(self, atrb)

    @id_valid
    def set_id(self, elem):
        self.id = elem

    @cc_valid
    def set_country_code(self, elem):
        self.country_code = elem

    @pn_valid
    def set_passport_no(self, elem):
        self.passport_no = elem

    @alfa_valid
    def set_fname(self, elem):
        self.fname = elem

    @alfa_valid
    def set_lname(self, elem):
        self.lname = elem

    @birth_valid
    @date_valid
    def set_date_of_birth(self, elem, date):
        self.date_of_birth = elem

    @issue_valid
    @date_valid
    def set_date_of_issue(self, elem, date):
        self.date_of_issue = elem

    @expire_valid
    @date_valid
    def set_date_of_expire(self, elem, date):
        self.date_of_expire = elem