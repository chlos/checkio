#!/usr/bin/env python

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    def get_digits(n, l=None):
        if l is None:
            l = []
        l.append(n % 10)
        n = n // 10
        if n:
            return get_digits(n, l)
        else:
            return l

    words = ''
    digits = get_digits(number)
    while len(digits) < 3:
        digits.append(0)

    tens = digits[1] * 10 + digits[0]
    if tens in range(1, 10):
        words += FIRST_TEN[digits[0] - 1]
    elif tens == 10:
        words += SECOND_TEN[0]
    elif tens in range(11, 20):
        words += SECOND_TEN[digits[0]]
    elif tens in range(20, 100):
        if digits[0]:
            words += OTHER_TENS[digits[1] - 2] + ' ' + FIRST_TEN[digits[0] - 1]
        else:
            words += OTHER_TENS[digits[1] - 2]

    hundrs = digits[2]
    if hundrs:
        words = FIRST_TEN[hundrs - 1] + ' ' + HUNDRED + ' ' + words

    return words.strip()

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces " \
                                                #"at the end of string"
