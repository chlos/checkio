#!/usr/bin/env python

#def checkio(data):
    #""" regex approach """
    #import re
    #if len(data)<10:
        #return False
    #if not re.search('[0-9]', data):
        #return False
    #if not re.search('[a-z]', data):
        #return False
    #if not re.search('[A-Z]', data):
        #return False
    #return True

def checkio(data):
    if len(data) < 10:
        return False
    digit_ok = upper_ok = lower_ok = False
    for char in data:
        if char.isupper():
            upper_ok = True
        elif char.islower():
            lower_ok = True
        elif char.isdigit():
            digit_ok = True
    if digit_ok and upper_ok and lower_ok:
        return True
    else:
        return False

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
