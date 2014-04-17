#!/usr/bin/env python
import itertools

def checkio(number):
    new_pigs = 0
    pigs = []
    for new_pigs in itertools.count(1):
        for _ in range(new_pigs):
            pigs.append(0)
        for i in range(len(pigs)):
            if number:
                pigs[i] += 1
                number -= 1
            else:
                return len([p for p in pigs if p])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
