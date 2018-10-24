import sys

def blackjack(a,b,c):
    integers = a, b, c

    eleven_exists = False

    for integer in integers:
        if integer == 11:
            eleven_exists = True
            
        if integer < 1 or integer > 11:
            # print('integer out of range - must be more than 0 and less than 12')
            return 'int_out_of_range'

    suma = a + b + c

    if eleven_exists:
        suma = suma - 10

    if suma <= 21:
        return suma

    return 'BUST'


test1 = blackjack(1, 2, 3)
test2 = blackjack(4, 5, 6)
test3 = blackjack(4, 11, 11)
test4 = blackjack(11, 11, 11)
test5 = blackjack(10, 10, 9)
test6 = blackjack(4, 11, 12)
test7 = blackjack(0, 11, 10)


if  test1 == 6:
    print('Test 1 successful.')
else:
    print('Test 1 failed.')

if  test2 == 15:
    print('Test 2 successful.')
else:
    print('Test 2 failed.')

if  test3 == 16:
    print('Test 3 successful.')
else:
    print('Test 3 failed.')

if  test4 == 'BUST':
    print('Test 4 successful.')
else:
    print('Test 4 failed.')

if  test5 == 'BUST':
    print('Test 5 successful.')
else:
    print('Test 5 failed.')

if  test6 == 'int_out_of_range':
    print('Test 6 successful.')
else:
    print('Test 6 failed.')

if  test7 == 'int_out_of_range':
    print('Test 7 successful.')
else:
    print('Test 7 failed.')

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)
print(test7)