#!/usr/bin/env python

def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """

    # returns 0 if you get out of pyramid
    def get_cost(costs, i, j):
        if j < 0 or i < 0:
            return 0
        try:
            return costs[i][j]
        except IndexError:
            return 0

    costs = []  # max costs of i,j-position
    for i in range(0, len(pyramid)):
        costs.append([])
        for j in range(0, len(pyramid[i])):
            if i == j == 0:
                costs[i].append(pyramid[i][j])
            else:
                cij = pyramid[i][j] + max(get_cost(costs, i - 1, j - 1),
                                            get_cost(costs, i - 1, j))
                costs[i].append(cij)
    return max(costs[-1])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
