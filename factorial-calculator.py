'''
Factorial calculator
Author: Duong Vu Tuan Minh
Date: 22/5/2020
'''


def find_fac(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 'The number provide must larger or equal 0'
    else:
        res  = n*find_fac(n-1)
    return res

if __name__ == "__main__":
    while True:
        number = input('Please enter a number to find factorial\n')
        res = find_fac(int(number))
        print(res)
        choice = input('Do you want to find a factorial of another number?\n\t')
        if choice[0] == 'y':
            continue
        else:
            print('Thanks')
            break