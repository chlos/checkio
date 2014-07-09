def golf(number):
    for n in __import__("itertools").count(number+1):
        if all(n % d != 0 for d in range(2, n)) and str(n) == str(n)[::-1]:
            return n

assert golf(2) == 3
assert golf(13) == 101
assert golf(101) == 131
