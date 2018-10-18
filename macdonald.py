# coding: utf-8
def macd(name):
    if name == '':
        return name
    elif name[0].isalpha():
        return name[0].upper() + name[1:3].lower() + name[3].upper() + name[4:].lower()
    
