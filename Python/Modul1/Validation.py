from datetime import date

class Valid:

    @staticmethod
    def date_valid(date):
        if date != None:
            if (0 < date.get_month() < 13) & (0 < date.get_day() < 32):
                if (date.get_month() == 2) & (date.get_day() > 29):
                    print('Feb has max 29 days.')
                    return None
                elif (date.get_month() == 2) & (date.get_day() > 28) & (date.get_year()%4 != 0):
                    print('Feb has 28 days, when year is not intercalary.')
                    return None
                elif ( date.get_month() == 4 or date.get_month() == 6 or date.get_month() == 9 or date.get_month() ==11 ) & ( date.get_day() > 30 ):
                    print('Apl, Jun, Sep and Nov have max 29 days.')
                    return None
                else:
                    return date
            else:
                print('Month has max 31 days and year has max 12 month')
                return None

    @staticmethod
    def NaturalValidation(k):
        if (k.isdigit() == False) or (int(k) < 1):
            print('Please enter a natural number: ')
            return None
        newk = int(k)
        return newk

    @staticmethod
    def fwd_valid(date):
        if date!= None:
            date = Valid().date_valid(date)
            if ((date.get_year() <= 2015) and (date.get_month() <= 8) and (date.get_day() < 5)) or (date.get_year() < 2015) :
                print('Min First Working Date is 05.08.2015')
                return None
            else:
                return date

    @staticmethod
    def lwd_valid(date, fwd):
        if  date != None:
            date = Valid().fwd_valid(date)
            if ((fwd.get_year() == date.get_year()) and ((date.get_month() - fwd.get_month() >= 3))) or ((date.get_year()-fwd.get_year() ==1) \
            and ((fwd.get_month() == 10 and fwd.get_month()>=1)or(fwd.get_month() == 11 and fwd.get_month()>=2)or(fwd.get_month() == 12 and fwd.get_month()>=3))) \
            or (date.get_year()-fwd.get_year()>1):
                return date
            else:
                print('Wrong Last Working Date is 05.08.2015')
                return None

    @staticmethod
    def name_valid(name):
        if name != None:
            if (name.isalpha() == False):
                print ('It must be only letterts')
                return None
            else:
                return name

    @staticmethod
    def salary_valid(sallary):
        if sallary != None:
            if (sallary[0:-3].isdigit() == True) and ((sallary[-3]=='.') or(sallary[-3]==',')) and (sallary[-2: 0].isdigit() == True):
                return float(sallary)
            else:
                print('It must be xxxxxx.xx')
                return None

    @staticmethod
    def txt_valid(txt):
        if txt.endswith('.txt'):
            return txt
        else:
            raise ValueError('It is not txt file.')

    @staticmethod
    def file_existing(file, mode="r"):
        try:
            f = open(Valid().txt_valid(file), mode)
        except IOError:
            raise IOError('File don`t exist.')
        return f