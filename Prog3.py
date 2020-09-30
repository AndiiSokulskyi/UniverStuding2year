def NaturalValidation(k):
    while k.isdigit() == False:
        k = input('Please enter a natural number: ')
    while int(k) < 1:
        k = input('Please enter a natural number: ')
    if k.isdigit() == False:
        NaturalValidation(k)
    newk = int(k)
    return newk


def XMatrixCreating(n):
    matrix=[[0]*n]
    for i in range(0, n-1):
       matrix.append([0]*n)
    matrix[0][0] = 1
    for i in range(0, n):
        matrix[i][i]=1
        matrix[i][-1-i] = 1
    return matrix

menu=''
while menu!='exit':
    oper=input('If you want to start testing programe, print "start" and press Enter, if you want to fihish runnig print "exit" and press Enter: ')
    menu=oper
    if oper=='start':
        while menu!='menu':
            n=NaturalValidation(input('Enter matrix size: '))
            matrix = XMatrixCreating(n)
            for i in range(0, n):
                print(matrix[i])
            menu=input('If you want to exit to menu, print "menu", if you want to continue print anything and press Enter: ')