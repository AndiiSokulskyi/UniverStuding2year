# Згенерувати послідовність дружніх чисел розмірності n.
# Дружніми числами називають два натуральні числа такі,
# що сума всіх дільників першого (за винятком самого числа) дорівнює другому числу,
# а сума всіх дільників другого числа (за винятком самого числа) дорівнює першому числу.
# Наприклад для 220 такими дільниками є числа 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 і 110 сума яких рівна 284,
# а для 284 дільниками є 1, 2, 4, 71, і 142 сума яких рівна 220. Отже (220,284) є парою дружніх чисел.

def DevisorsSum(k):
    sum = 0
    for i in range(1, k):
        if k % i == 0:
            sum += i
    return sum


def FriendNumbers(n):
    list = []
    a = 1
    while len(list) != n:
        for i in range(1, a):
            if(i == DevisorsSum(a)) & (a == DevisorsSum(i)):
                list.append((i, a))
        a += 1
    return list


def Validation(k):
    while k.isdigit()==False:
        k=input('Please enter a natural number: ')
    while int(k) < 1:
        k = input('Please enter a natural number: ')
    if k.isdigit() == False:
        Validation(k)
    newk = int(k)
    return newk


n = input('Enter number of friend numbers pairs: ')
n = Validation(n)
print(FriendNumbers(n))


