#
# nice solution: http://www.checkio.org/mission/min-max/publications/Cjkjvfnby/python-3/sorted/
#

#def get_first_from_sorted(args, key, reverse):
    #if len(args) == 1:
        #args = iter(args[0])
    #return sorted(args, key=key, reverse=reverse)[0]

#def min(*args, key=None):
    #return get_first_from_sorted(args, key, False)

#def max(*args, key=None):
    #return get_first_from_sorted(args, key, True)

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        vars = args[0]
    else:
        vars = args[:]
    ans = None
    for arg in vars:
        if ans is None:
            ans = arg
            continue
        if key is not None:
            if key(arg) < key(ans):
                ans = arg
        else:
            if arg < ans:
                ans = arg
    return ans


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        vars = args[0]
    else:
        vars = args[:]
    ans = None
    for arg in vars:
        if ans is None:
            ans = arg
            continue
        if key is not None:
            if key(arg) > key(ans):
                ans = arg
        else:
            if arg > ans:
                ans = arg
    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min(abs(i) for i in range(-10, 10)) == 0, "Generator"
    assert max(abs(i) for i in range(-10, 10)) == 10, "Generator"
