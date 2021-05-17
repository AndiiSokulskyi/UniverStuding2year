# Про короля та дерева


def Woodcutter(n, m):
    count=0
    if m == 0:
        count=0
    elif m==1:
        count==2
    else:
        for i in range(1, ( n//(m-1))):
            count+= n-i
    return count


def Validation(k):
    while k.isdigit()==False:
        k=input('Please enter a natural number or 0: ')
    while (int(k) <0) | (int(k) >1000):
        k = input('Please enter a number from 0 to 1000: ')
    if k.isdigit() == False:
        Validation(k)
    newk = int(k)
    return newk


n=input('Enter the initial number of trees:')
n=Validation(n)
m=input('Enter the final number of trees:')
m=Validation(m)

while m > n:
    m = input('The final number of trees can`t be bigger then initial, please enter m < n :')
    m = Validation(m)

print('The number of ways how king can cut his trees: ', Woodcutter(n, m))



