# Згенерувати послідовність дружніх чисел розмірності n.
# Дружніми числами називають два натуральні числа такі,
# що сума всіх дільників першого (за винятком самого числа) дорівнює другому числу,
# а сума всіх дільників другого числа (за винятком самого числа) дорівнює першому числу.
# Наприклад для 220 такими дільниками є числа 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 і 110 сума яких рівна 284,
# а для 284 дільниками є 1, 2, 4, 71, і 142 сума яких рівна 220. Отже (220,284) є парою дружніх чисел.
from Generator import *
from Iterator import *

def Validation(k):
    while k.isdigit()==False:
        k=input('Please enter a natural number: ')
    while int(k) < 1:
        k = input('Please enter a natural number: ')
    if k.isdigit() == False:
        Validation(k)
    newk = int(k)
    return newk


menu = ''
while menu!= '3':
    print('1 - Use generator.', '\n', '2 - Use iterator.', '\n', '3 - Завершити програму.')
    oper = input('Enter 1 or 2 or 3: ')
    print(oper)
    if oper == '1' or oper == '2':
        menu = ''
        while menu != 'menu':
            N = input('Enter number of friend numbers pairs: ')
            N = Validation(N)
            if oper == '1':
                for i in fn_generator(N):
                    print(i)
            if oper == '2':
                itr = GN_Iterator()
                for i in range(N):
                    print(next(itr))
            menu = input('If you want to exit to menu, print "menu", if you want to continue print anything and press Enter: ')
    elif oper == '3':
        menu = oper


