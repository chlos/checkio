#!/usr/bin/env python

#def checkio(text):
    #"""
    #We iterate through latyn alphabet and count each letter in the text.
    #Then 'max' selects the most frequent letter.
    #For the case when we have several equal letter,
    #'max' selects the first from they.

    #http://www.checkio.org/mission/most-wanted-letter/publications/bryukh/python-3/max-count/
    #"""
    #import string
    #text = text.lower()
    #return max(string.ascii_lowercase, key=text.count)

#def checkio(text):
    #"""
    #http://www.checkio.org/mission/most-wanted-letter/publications/alaf/python-27/first/
    #"""
    #text = ''.join(i for i in text.lower() if i.isalpha())
    #return max(set(text), key=text.count)

#def checkio(text):
    #"""
    #http://www.checkio.org/mission/most-wanted-letter/publications/ForeverYoung/python-3/first/
    #"""
    #from collections import Counter
    #count = Counter([x for x in text.lower() if x.isalpha()])
    #m = max(count.values())
    #return sorted([x for (x, y) in count.items() if y == m])[0]

def checkio(text):
    freqs = {}
    for ch in text:
        if ch.isalpha():
            try:
                freqs[ch.lower()] += 1
            except KeyError:
                freqs[ch.lower()] = 1
    freq_max = max(freqs.items(), key=lambda x: x[1])[1]
    most_freq_chars = [ch for ch, fr in freqs.items() if fr == freq_max]
    return sorted(most_freq_chars)[0]

if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
