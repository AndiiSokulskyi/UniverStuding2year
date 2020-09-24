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


def BinarySearch(array, value):
    temp=[]
    indx = []
    searchOp=0
    allOp=0
    for i in range(0, len(array)):
        temp.append((array[i], i))
        allOp+=1
    temp.sort()
    allOp += 1

    mid = len(temp) // 2
    low = 0
    high = len(temp) - 1
    while temp[mid][0] != value and low <= high:
        if value > temp[mid][0]:
            low = mid + 1
            searchOp+=1
        else:
            high = mid - 1
            searchOp+=1
        mid = (low + high) // 2
        searchOp += 1
    if low > high:
        print("No value")
        allOp += 1
    indx.append(mid)
    allOp += 1

    mid1 = mid2 = mid
    searchOp += 1
    while (temp[mid1][0] == temp[mid1-1][0]) & (mid1 != 0):
        mid1 -= 1
        searchOp += 1
        indx.append(mid1)
        allOp += 1
    while (temp[mid2][0] == temp[mid2 + 1][0]) & (mid1 != len(temp)-1):
        mid2 += 1
        searchOp += 1
        indx.append(mid2)
        allOp += 1

    for i in range(0, len(indx)):
        indx[i]=temp[indx[i]][1]
        allOp += 1

    indx.sort()
    allOp += 1
    allOp+=searchOp
    print('Number of search operations: ', searchOp)
    print('Number of all operations: ', allOp)
    return indx


N = input('Enter N: ')
N = NaturalValidation(N)
array = []
for i in range (0, N):
    array.append(IntValidation(input('Enter element of array: ')))



array1 = StrangeSort(array)
print(array1)

value = input('Enter value you want to find: ')
value=IntValidation(value)

print('Indexes of elements you need: ', BinarySearch(array1, int(value)))
