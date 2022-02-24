import random


def link(a, b):
    print(f'\nCurrent Link: {a}')
    if a < b:
        if (a%2) == 0:
            a+=(a/2)
        else:
            a+=(random.randint(1,3)*round(b*0.1))
    else:
        a-=random.randint(1,3);
    
    print(f'Next Link: {a}')
    
    if a != b:
        link(a, b)
    

a = int(input('Enter 1st link: '))
b = int(input('Enter last link: '))

link(a,b)
