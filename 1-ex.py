# coding: utf-8
#
#warmup 1 challenge for udemy python bootcamp course
#
## LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd\n"
def lesser(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        if a % 2 == 1 and b % 2 == 1:
            return max(a,b)
        else:
            if a % 2 == 1 or b % 2 == 1:
                return max(a,b)
            
