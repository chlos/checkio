#!/usr/bin/env python

#def checkio(data):
    #""" collections approach """
    #from collections import Counter
    #l_non_unique_elements = [e for e, c in Counter(data).items() if c > 1]
    #l_unique_removed = [e for e in data if e in l_non_unique_elements]
    #return l_unique_removed

def checkio(data):
    return [e for e in data if data.count(e) > 1]

if __name__ == '__main__':
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
    assert checkio([1, 2, 3, 4, 5]) == []
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
