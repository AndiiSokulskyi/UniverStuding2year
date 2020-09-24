# Задано масив з N цілих чисел.
# Сформувати масив таким чином, щоб спочатку були всі від’ємні елементи масиву, потім додатні і, після них нульові, зберігши порядок.
# Якщо якоїсь групи чисел не існує, то після кожного числа, що дорівнює K вставити рандомне число х цієї групи.
# Наприклад, -5 0 -4 0 -5 -6 0. K= -5. Немає додатних чисел. -5 7 -4 -5 6 -6 0 0 0.
# Числа 7 і 6 - рандомні, після кожного -5.

import random


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


def StrangeSort(array):
    negat=[]
    poset=[]
    zeros=[]
    for i in range(0, len(array)):
        if array[i] > 0:
            poset.append(array[i])
        elif array[i] < 0:
            negat.append(array[i])
        elif array[i] == 0:
            zeros.append(array[i])
    array.clear()
    for i in range(0, len(negat)):
        array.append(negat[i])
    for i in range(0, len(poset)):
        array.append(poset[i])
    for i in range(0, len(zeros)):
        array.append(zeros[i])
    if (len(negat)==0)|(len(poset)==0)|(len(zeros)==0):
        K = input('Enter K: ')
        K = IntValidation(K)
        addlen=0
        for i in range(0, len(array)):
            if array[i] == K:
                addlen+=1
        for i in range(0, len(array)+addlen):
            if array[i] == K:
                array.insert(i+1, random.randint(-1000, 1000))
    return array


N = input('Enter N: ')
N = NaturalValidation(N)
array = []
for i in range (0, N):
    array.append(IntValidation(input('Enter element of array: ')))

print(StrangeSort(array))
