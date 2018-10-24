def spy_game(numbers):
    spy_caught = ['', '', '']

    for number in numbers:
        if spy_caught == ['', '', ''] and number == 0:
            spy_caught = ['0', '', '']
        if spy_caught == ['0', '', ''] and number == 0:
            spy_caught = ['0', '0', '']
        if spy_caught == ['0', '0', ''] and number == 7:
            spy_caught = ['0', '0', '7']


    if spy_caught == ['0', '0', '7']:
        return True

    return False

spy_game([])

if spy_game([1,4,7,8,3,4,0,2,8,9,0,3,4,1,3,7,9]):
    print('Spy Game 1', True)
else:
    print('Spy Game 1', False)
if spy_game([1,4, 0,0,7,8,3,4,2,3,4,8,9,1,3,7,9]):
    print('Spy Game 2', True)
else:
    print('Spy Game 2', False)
if spy_game([1,4,7,8,3,4,2,8,9,3,4,1,3,7,9]):
    print('Spy Game 3', True)
else:
    print('Spy Game 3', False)
if spy_game([8,9,3,4,1,3,7,9,1,4,7,8,3,4,2]):
    print('Spy Game 4', True)
else:
    print('Spy Game 4', False)
if spy_game([1,4,7,8,3,4,2,8,9,3,4,1,3,7,9]):
    print('Spy Game 5', True)
else:
    print('Spy Game 5', False)
