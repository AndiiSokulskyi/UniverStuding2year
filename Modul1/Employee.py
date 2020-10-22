#Створити клас Employee, який містить такі поля
# 1. Name (Тільки літери)
# 2. Salary (Число з 2 знаками після коми)
# 3. FirstWorkingDate (Клас Date, що містить 3 поля: день (1-31 / 1-30 / 1-29 / 1-28), місяць (1-12) рік (2020+). Min: 05.08.2015
# 4. LastWorkingDate Null or (Клас Date, що містить 3 поля: день (1-31 / 1-30 / 1-29 / 1-28), місяць (1-12) рік (2020+). Min: StartDate + 3 months
#Створити такі методи:
# 1. Зчитати масив (клас для роботи з масивом екземплярів класу Employee) Employee з файла (1)
# 2. Додати новий Employee. В один місяць може влаштуватись на роботу і звільнитись не більше, ніж 20% всього персоналу(3)
# 3. Додати валідацію на поля Name, Salary, FirstWorkingDate, LastWorkingDate (2.5)
# 4. Обрахувати витрати компанії на заробітню платню сумарно всіх працівників (вважається, що кожних 6 місяців працівник отримує заробітню платню вищу на 15%) (1.5)
# 5. Всіх працівників, які відпрацювали рівно 1, 2, … років потрібно записати в інший файл: Ім’я працівника, 1 рік і так далі  (1.5)
# 6. Вивести всі Employee на екран (0.5)


from Validation import Valid

class Date:

    def __init__(self, day = None, month = None, year = None):
        self.day = Valid().NaturalValidation(day)
        self.month = Valid().NaturalValidation(month)
        self.year = Valid().NaturalValidation(year)

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def set_day(self, day):
        self.day = Valid().NaturalValidation(day)

    def set_month(self, month):
        self.month = Valid().NaturalValidation(month)

    def set_year(self, year):
        self.year = Valid().NaturalValidation(year)



class Employee:

    def __init__(self, Name = None, Salary = None, FirstWorkingDate = None, LastWorkingDate = None):
        self.name = Valid().name_valid(Name)
        self.salary = Valid().salary_valid(Salary)
        self.fwd = Valid().fwd_valid(FirstWorkingDate)
        self.lwd = Valid().lwd_valid(LastWorkingDate, self.fwd)

    def __str__(self):
        strng = 'Name' + ': ' + self.name + '\n'
        strng += 'Salary' + ': ' + self.salary + '\n'
        strng += 'First Working Date' + ': ' + self.fwd + '\n'
        strng += 'Last Working Date' + ': ' + self.lwd + '\n'
        return strng

    def set_name(self, Name):
        self.name = Valid().name_valid(Name)

    def set_salary(self, Salary):
        self.salary = Valid().salary_valid(Salary)

    def set_fwd(self, FirstWorkingDate):
        self.fwd = Valid().fwd_valid(FirstWorkingDate)

    def set_lwd(self, LastWorkingDate):
        self.lwd = Valid().lwd_valid(LastWorkingDate, self.fwd)

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def get_fwd(self):
        return self.fwd

    def get_lwd(self):
        return self.lwd


class Collection:

    def __init__(self):
        self.collec = []

    def __str__(self):
        strng = ''
        for i in self.collec:
            strng += str(i) + '\n'
        return strng

    def add_to_collec(self, elem):
        counter = 0
        for i in self.collec:
            if elem.get_fwd().get_month() == i.get_fwd().get_month():
                counter += 1
        if 5 * counter < len(self.collec):
            self.collec.append(elem)

    def add_from_file(self, file):
        while True:
            fid = Employee()
            f = file.readline().strip('\n')
            if not f:
                break
            fid.set_name(f)
            f = file.readline().strip('\n')
            fid.set_salary(f)
            dat = Date()
            f = file.readline().strip('\n')
            fid.set_fwd(f)
            f = file.readline().strip('\n')
            fid.set_lwd(f)
            f = file.readline().strip('\n')
            self.collec.append(f)

    def add_to_file(self, file):
        for i in self.collec:
            file.write(i.get_name())
            file.write('\n')
            file.write(i.get_salary())
            file.write('\n')
            file.write(i.get_fwd())
            file.write('\n')
            file.write(i.get_lwd())
            file.write('\n')
            file.write('\n')