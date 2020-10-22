#Варіант 2
from Employee import *
from Validation import Valid

menu = ''
cl = Collection()
while menu!= '0':
    print('0 - Завершити програму.', '\n',
          '1 - Додати до колекції.', '\n',
          '2 - Додати до колекції з файлу.', '\n',
          )
    oper = input('Enter from 0 to 11: ')
    menu = ''
    if oper == '0':
        menu = oper
    while (menu != 'menu') & (menu !='0'):
        if oper == '1':
            idd = Employee()
            idd.set_name(input('Enter name:'))
            idd.set_salary(input('Enter name:'))
            idd.set_fwd(input('Enter name:'))
            idd.set_lwd(input('Enter name:'))
            cl.add_to_collec(idd)
            print(cl)
        elif oper == '2':
            file = Valid().file_existing("Text.txt", "r")
            cl.add_from_file(file)
            file.close()
            print(cl)
        menu = input('If you want to exit to menu, print "menu", if you want to continue print anything and press Enter: ')