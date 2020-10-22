from Memento import *
from Validation import *

@txt_valid
def rid_writ(txt, mode):
    f = open(txt, mode)
    return f

menu = ''
cl = Collection()
MeM = Caretaker(cl)
while menu!= '0':
    print('0 - Завершити програму.', '\n',
          '1 - Додати до колекції.', '\n',
          '2 - Додати до колекції з файлу.', '\n',
          '3 - Додати колекцію до файлу.', '\n',
          '4 - Видалити з колекції.', '\n',
          '5 - Видалити з файлу.', '\n',
          '6 - Змінити в колекції.', '\n',
          '7 - Змінити у файлі.', '\n',
          '8 - Пошук.', '\n',
          '9 - Сортувати.', '\n',
          '10 - Назад.', '\n',
          '11 - Вперед.', '\n',
          )
    oper = input('Enter from 0 to 11: ')
    menu = ''
    if oper == '0':
        menu = oper
    while (menu != 'menu') & (menu !='0'):
        if oper == '1':
            idd = ForeignID()
            idd.set_id(input(dictio[0] + ': '))
            idd.set_country_code(input(dictio[1] + ': '))
            idd.set_passport_no(input(dictio[2] + ': '))
            idd.set_fname(input(dictio[3] + ': '))
            idd.set_lname(input(dictio[4] + ': '))
            idd.set_date_of_birth(input(dictio[5] + ': '))
            idd.set_date_of_issue(input(dictio[6] + ': '))
            idd.set_date_of_expire(input(dictio[7] + ': '))
            MeM.backup()
            cl.add_to_collec(idd)
            print(cl)
        elif oper == '2':
            file = rid_writ("Text.txt", "r")
            MeM.backup()
            cl.add_from_file(file)
            file.close()
            print(cl)
        elif oper == '3':
            file = rid_writ("Text.txt", "w")
            MeM.backup()
            cl.add_to_file(file)
            file.close()
        elif oper == '4':
            iDn = input('Введіть ідентифікатор по якому треба видалити: ')
            MeM.backup()
            cl.delete_from_collec(iDn)
            print(cl)
        elif oper == '5':
            iDn = input('Введіть ідентифікатор по якому треба видалити з файлу: ')
            file = rid_writ("Text.txt", "w")
            MeM.backup()
            cl.delete_from_file(file, iDn)
            file.close()
        elif oper == '6':
            iDn = input('Введіть ідентифікатор по якому треба змінити: ')
            ed = input('Введіть значення на яке треба змінити: ')
            MeM.backup()
            cl.edit_collec(iDn, ed)
            print(cl)
        elif oper == '7':
            iDn = input('Введіть ідентифікатор по якому треба змінити: ')
            ed = input('Введіть значення на яке треба змінити: ')
            file = rid_writ("Text.txt", "w")
            MeM.backup()
            cl.edit_file(file, iDn, ed)
            file.close()
        elif oper == '8':
            s = input('Введіть те, що хочете знайти: ')
            MeM.backup()
            print(cl.find_in_collec(s))
        elif oper == '9':
            print(' 0 : id', '\n',
                  '1 : country_code', '\n',
                  '2 : passport_no', '\n',
                  '3 : fname','\n',
                  '4 : lname', '\n',
                  '5 : date_of_birth', '\n',
                  '6 : date_of_issue', '\n',
                  '7 : date_of_expire', '\n')
            atrb = input('Введіть атрибут за яким сортувати:')
            MeM.backup()
            cl.sort_of_collec(atrb)
            print(cl)
        elif oper == '10':
            MeM.undo()
            print(cl)
        elif oper == '11':
            MeM.redo()
            print(cl)
        menu = input('If you want to exit to menu, print "menu", if you want to continue print anything and press Enter: ')