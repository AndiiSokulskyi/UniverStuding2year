from Strategy import *
from random import randint
from threading import Thread


def position(ll, pos):
    if ll.length() != 0:
        pos = IntValidation(input('Введіть позицію: '))
        if pos < 0:
            pos = 0
        elif pos >=ll.length():
            pos = ll.length()-1
    else:
        print('Позиція - 0. ')
    return pos


def LinkListSort(list, K, rang, obs):
    temp_l = list.copy()
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
                list.linsert(i, randint(-rang, rang))
    e = Event("change", temp_l, 0, list, list.length()-1)
    e.notify(obs)
    return list


def threading_start_join(func, lists, *args):
    for list in lists:
        th = Thread(target=func, args=(list, *args))
        th.start()
        th.join()


def dell(ll, pos, obs, pos2=None):
    ll.ldel(pos, obs, pos2)


def actions(ll, ll1, obs):
    while True:
        print(' 4 - Видалити елемент за вказаною позицією', '\n',
              '5 - Видалити декілька елементів в межах початкової та кінцевої позиції', '\n',
              '6 - Метод для роботи зі списком', '\n',
              '7 - Вивести список', '\n',
              '8 - Вихід', '\n')
        oper = input('Enter from 4, 5, 6, 7 or 8: ')
        if oper == '8':
            break
        if oper == '4':
            pos = IntValidation(input('Введіть позицію: '))
            threading_start_join(dell, [ll, ll1], pos, obs)
        elif oper == '5':
            pos1 = IntValidation(input('Введіть початкову позицію: '))
            pos2 = IntValidation(input('Введіть кінцеву позицію: '))
            threading_start_join(dell, [ll, ll1], pos1, obs, pos2)
        elif oper == '6':
            K = input('Enter K: ')
            K = IntValidation(K)
            rang = input('Enter range of random: ')
            rang = NatValidation(rang)
            threading_start_join(LinkListSort, [ll, ll1], K, rang, obs)
        elif oper == '7':
            print("first list: ")
            ll.lprint()
            print("\nfirst list: ")
            ll1.lprint()

    obs.logger_print_in_file("ObserverFile.txt")


def creation(ll, obs):
    con = Context()
    print(' 1 - Генерувати за допомогою ітератора.', '\n',
          '2 - Зчитувати дані з файла', '\n',
          '8 - Закінчити створення списку', '\n')
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
        ll = con.generation(ll, pos, txt, obs)

    while True:
        print(' 1 - Генерувати за допомогою ітератора.', '\n',
              '2 - Зчитувати дані з файла', '\n',
              '3 - Генерувати дані', '\n',
              '8 - Закінчити створення списку', '\n')
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
            ll = con.generation(ll, pos, txt, obs)
        elif oper == '3':
            N = NatValidation(input('Введіть кількість пар дружніх чисел: '))
            ll = con.generation(ll, pos, N, obs)


obs = Observer()
ll = LinkedList()
ll1 = LinkedList()
creation(ll, obs)
creation(ll1, obs)
actions(ll, ll1, obs)
