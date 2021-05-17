
from Strategy import *


def position(ll, pos):
    if ll.length() != 0:
        pos = NatValidation(input('Введіть позицію: '))
    else:
        print('Позиція - 0. ')
    return pos


def LinkListSort(list, K, rang):
    negat = LinkedList()
    poset = LinkedList()
    zeros = LinkedList()
    for i in range(list.length()):
        if list[i].get_data() > 0:
            poset.push_back(list[i].get_data())
        elif list[i].get_data() < 0:
            negat.push_back(list[i].get_data())
        elif list[i].get_data() == 0:
            zeros.push_back(list[i].get_data())
    list.lclear()
    for i in range(negat.length()):
        list.push_back(negat[i].get_data())
    for i in range(poset.length()):
        list.push_back(poset[i].get_data())
    for i in range(zeros.length()):
        list.push_back(zeros[i].get_data())
    if (negat.length() == 0) | (poset.length() == 0) | (zeros.length() == 0):
        for i in range(list.length()):
            if list[i].get_data() == K:
                list.linsert(i, random.randint(-rang, rang))
    return list


def strategy(ll):
    con = Context()
    print(' 1 - Генерувати за допомогою ітератора.', '\n',
          '2 - Зчитувати дані з файла', '\n',
          '8 - Вихід', '\n')
    oper = input('Enter from 1, 2 or 8: ')
    if oper == '8':
       return
    if oper == '1':
        pos = 0
        pos = position(ll, pos)
        con.set_strategy(Strategy_Iter)
    elif oper == '2':
        txt = "Text.txt"
        pos = 0
        pos = position(ll, pos)
        con.set_strategy(Strategy_File)
        ll = con.generation(ll, pos, txt)

    while True:
        if oper == '2':
            break
        print(' 1 - Генерувати за допомогою ітератора.', '\n',
              '2 - Зчитувати дані з файла', '\n',
              '3 - Генерувати дані', '\n',
              '8 - Вихід', '\n')
        oper = input('Enter from 1, 2, 3 or 8: ')
        if oper == '8':
            break
        if oper == '1':
            pos = position(ll, pos)
            con.set_strategy(Strategy_Iter)
        elif oper == '2':
            txt = "Text.txt"
            pos = position(ll, pos)
            con.set_strategy(Strategy_File)
            ll = con.generation(ll, pos, txt)
            break
        elif oper == '3':
            N = NatValidation(input('Введіть кількість пар дружніх чисел: '))
            ll = con.generation(ll, pos, N)
            break

    while True:
        print(' 1 - Генерувати за допомогою ітератора.', '\n',
              '2 - Зчитувати дані з файла', '\n',
              '3 - Генерувати дані', '\n',
              '4 - Видалити елемент за вказаною позицією', '\n',
              '5 - Видалити декілька елементів в межах початкової та кінцевої позиції', '\n',
              '6 - Метод для роботи зі списком', '\n',
              '7 - Вивести список', '\n',
              '8 - Вихід', '\n')
        oper = input('Enter from 1, 2, 3, 4, 5, 6, 7 or 8: ')
        if oper == '8':
            break
        if oper == '1':
            pos = position(ll, pos)
            con.set_strategy(Strategy_Iter)
        elif oper == '2':
            txt = "Text.txt"
            pos = position(ll, pos)
            con.set_strategy(Strategy_File)
            ll = con.generation(ll, pos, txt)
        elif oper == '3':
            N = NatValidation(input('Введіть кількість пар дружніх чисел: '))
            ll = con.generation(ll, pos, N)
        elif oper == '4':
            pos = position(ll, pos)
            if ll.length() != 0:
                ll.ldel(pos)
        elif oper == '5':
            pos1 = NatValidation(input('Введіть початкову позицію: '))
            pos2 = NatValidation(input('Введіть кінцеву позицію: '))
            if ll.length() != 0:
                if pos2 >= ll.length():
                    pos2 = ll.length()-1
                if pos1 < 0:
                    pos1 = 0
                if pos2 < pos1:
                    pos1, pos2 = pos2, pos1
                j = ll[pos2]
                while ll[pos1] != j:
                    ll.ldel(pos1)
                ll.ldel(pos1)
        elif oper == '6':
            K = input('Enter K: ')
            K = IntValidation(K)
            rang = input('Enter range of random: ')
            rang = NatValidation(rang)
            LinkListSort(ll, K, rang)
        elif oper == '7':
            ll.lprint()


ll = LinkedList()
strategy(ll)
