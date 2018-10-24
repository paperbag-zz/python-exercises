# coding: utf-8
def find_excluded_sum(arr, start, end):
    numbers = arr
    found_numbers = []

    for number in numbers:
        if  number < start:
            found_numbers.append(number)
        if number > end:
            found_numbers.append(number)

    sum_of_found_numbers = sum(found_numbers)

    print(sum_of_found_numbers)


find_excluded_sum([-1, -10, -50, 10,6.2, 5.4, 7.8, 8.1, 7.023, 3,6.111, 49, 100, 420, 1, 0, -3, 8], 6, 9)
find_excluded_sum([1, 3, 5], 6, 9)
find_excluded_sum([4, 5, 6, 7, 8, 9 ], 6, 9)
find_excluded_sum([2, 1, 6, 9, 11], 6, 9)
