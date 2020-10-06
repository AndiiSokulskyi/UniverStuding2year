#Переписати завдання за допомогою Linked List.
# Задано масив з N цілих чисел.
# Сформувати масив таким чином, щоб спочатку були всі від’ємні елементи масиву, потім додатні і, після них нульові, зберігши порядок.
# Якщо якоїсь групи чисел не існує, то після кожного числа, що дорівнює K вставити рандомне число х цієї групи.
# Наприклад, -5 0 -4 0 -5 -6 0. K= -5. Немає додатних чисел. -5 7 -4 -5 6 -6 0 0 0.
# Числа 7 і 6 - рандомні, після кожного -5.

import random
from LinkedList import *

def NaturalValidation(k):
    while k.isdigit() == False:
        k = input('Please enter a natural number: ')
    while int(k) < 1:
        k = input('Please enter a natural number: ')
    if k.isdigit() == False:
        NaturalValidation(k)
    newk = int(k)
    return newk


def IntValidation(k):
    while (k.isdigit() == False) & ((k.startswith('-')==False) | (k[1:].isdigit() == False)):
            k = input('Please enter a integer number: ')
    newk = int(k)
    return newk


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

menu = ''
while menu!= '3':
    print('1 - Заповнити список вручну.', '\n', '2 - Заповнити список рандомними числами', '\n', '3 - Завершити програму.')
    oper = input('Enter 1 or 2 or 3: ')
    if oper == '1':
        while menu != 'menu':
            N = input('Enter N: ')
            N = NaturalValidation(N)
            list = LinkedList()
            for i in range (0, N):
                list.push_back(IntValidation(input('Enter element of array: ')))
            K = input('Enter K: ')
            K = IntValidation(K)
            rang = input('Enter range of random: ')
            rang = NaturalValidation(rang)
            list = LinkListSort(list, K, rang)
            list.lprint()
            menu = input('If you want to exit to menu, print "menu", if you want to continue print anything and press Enter: ')
    elif oper == '2':
        while menu != 'menu':
            N = input('Enter N: ')
            N = NaturalValidation(N)
            list = LinkedList()
            rang = input('Enter range of random: ')
            rang = NaturalValidation(rang)
            for i in range(0, N):
                list.push_back(random.randint(-rang, rang))
            list.lprint()
            K = input('Enter K: ')
            K = IntValidation(K)
            list = LinkListSort(list, K, rang)
            list.lprint()
            menu = input('If you want to exit to menu, print "menu", if you want to continue print anything and press Enter: ')
    elif oper == '3':
        menu = oper
