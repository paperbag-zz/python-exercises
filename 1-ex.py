# coding: utf-8
def lesser(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        if a % 2 == 1 and b % 2 == 1:
            return max(a,b)
        else:
            if a % 2 == 1 or b % 2 == 1:
                return max(a,b)
            
