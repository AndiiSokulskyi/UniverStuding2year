from datetime import date
from rest_framework.serializers import ValidationError
cc_dictio={ 0 : 'ukr', 1 : 'isr', 2 :'pol', 3 :'swz', 4 : 'itl'}

class OtherFieldValidator:
    def __init__(self, other_field):
        self.other_field = other_field

    def set_context(self, serializer_field):
        self.serializer_field = serializer_field

    def make_validation(self, field, other_field):
        pass

    def __call__(self, value):
        field = value
        serializer = self.serializer_field.parent
        raw_other_field = serializer.initial_data[self.other_field]

        try:
            other_field = serializer.fields[self.other_field].run_validation(raw_other_field)
        except ValidationError:
            return

        self.make_validation(field, other_field)


class Validation:

    @staticmethod
    def alfa_valid(alfa):
        if (alfa.isalpha() == False):
            raise ValidationError("It must be only letterts")
        else:
            return alfa

    @staticmethod
    def cc_valid(country_code):
        for i in range(len(cc_dictio)):
            if (country_code == cc_dictio[i]):
                return Validation.alfa_valid(country_code)
        raise ValidationError("It must be country code (small letters, less then 4)")

    @staticmethod
    def pn_valid(passport_no):
        if (len(passport_no) == 8) & passport_no[0:2].isupper() & passport_no[2:8].isdigit():
            return passport_no
        else:
            raise ValidationError("It must be passport № (First two - big letters, next 6 digits)")

    @staticmethod
    def date_valid(dmy):
        date = str(dmy)
        if (len(date) == 10) & date[0:4].isdigit() & date[5:7].isdigit() & date[8:10].isdigit() & (date[4] == '-') & (date[7] == '-'):
            if (0 < int(date[5:7]) < 13) & (0 < int(date[8:10]) < 32):
                if (date[5:7] == '02') & (int(date[8:10]) > 29):
                    raise ValidationError("Feb has max 29 days.")
                elif (date[5:7] == '02') & (int(date[8:10]) > 28) & (int(date[0:4])%4 != 0):
                    raise ValidationError("Feb has 28 days, when year is not intercalary.")
                elif ( date[5:7] == '04' or date[5:7] == '06' or date[5:7] == '09' or date[5:7] =='11' ) & ( int(date[8:10]) > 30 ):
                    raise ValidationError("Apl, Jun, Sep and Nov have max 29 days.")
                else:
                    return dmy
            else:
                raise ValidationError("Month has max 31 days and year has max 12 month")
        else:
            raise ValidationError("It must be date (xx.xx.xxxx)")

    @staticmethod
    def birth_valid(date_of_birth):
        if str(date.today()) > str(date_of_birth)> '1900-01-01':
            return Validation.date_valid(date_of_birth)
        else:
            raise ValidationError("This person is unborned or dead")

    class issue_valid(OtherFieldValidator):
        def make_validation(self, date_of_issue, date_of_birth):
            if date.today() > date_of_issue > date_of_birth:
                return Validation.date_valid(date_of_issue)
            else:
                raise ValidationError("This person can`t get forirgn passport before birth or in future")

    class expire_valid(OtherFieldValidator):
        def make_validation(self, date_of_expire, date_of_issue):
            if date_of_expire > date_of_issue:
                return Validation.date_valid(date_of_expire)
            else:
                raise ValidationError("Foreign passport can`t be expired before getting")