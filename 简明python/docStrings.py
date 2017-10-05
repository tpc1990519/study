def pringMax(x,y):
    '''prints ths maximum
    the two values must be integers.'''
    x = int(x)
    y = int(y)
    if x>y:
        print(x)
    else:
        print(y)
    '''the end'''
pringMax(3,5)
print(pringMax.__doc__)
print(help(pringMax))
