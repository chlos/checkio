#!/usr/bin/env python

def checkio(game_result):
    ln = len(game_result)
    lines = [list(line) for line in game_result]
    cols = [[line[col] for line in game_result] \
                        for col in range(0, ln)]
    diags = [[], []]
    for i in range(0, ln):
        diags[0].append(game_result[i][i])
        diags[1].append(game_result[i][ln - 1 - i])
    for var in lines + cols + diags:
        if len(set(var)) == 1:
            winner = var[0]
            if winner in ["X", "x", "O", "o"]:
                return winner
    return "D"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio([
        "...",
        "XXX",
        "OO."]) == "X", "Xs wins, not dots"
