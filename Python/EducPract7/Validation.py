def NatValidation(k):
    while k.isdigit()==False:
        k = input('Please enter a natural number: ')
    while int(k) < 1:
        k = input('Please enter a natural number: ')
    if k.isdigit() == False:
        NatValidation(k)
    newk = int(k)
    return newk


def IntValidation(k):
    while (k.isdigit() == False) & ((k.startswith('-')==False) | (k[1:].isdigit() == False)):
            k = input('Please enter a integer number: ')
    newk = int(k)
    return newk


def TxtIntValidation(k):
    if (k.isdigit() == False) & ((k.startswith('-') == False) | (k[1:].isdigit() == False)):
        print('VALUE_ERROR!!! It must be a integer number.')
        newk = 'Incorect'
    else:
        newk = int(k)
    return newk


def txt_valid(txt):
    if txt.endswith('.txt'):
        return txt
    else:
        raise ValueError('It is not txt file.')


def file_existing(file, mode = "r"):
    try:
        f = open(txt_valid(file), mode)
    except IOError:
        raise IOError('File don`t exist.')
    return f