from copy import deepcopy


def readDecks(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return [[int(x) for x in group.splitlines()[1:]] for group in infile.read().split("\n\n")]


def getScore(deck):
    ans = 0
    for i, val in enumerate(deck[::-1]):
        ans += val * (i+1)
    return ans


def part1(decks):
    while min(len(deck) for deck in decks) > 0:
        curr = [deck.pop(0) for deck in decks]
        roundWin = curr.index(max(curr))
        decks[roundWin].extend(sorted(curr, reverse=True))
    return getScore(max(decks))


class Game2:
    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.history = set()

    def game(self):
        while self.deck1 and self.deck2:
            if (tuple(self.deck1), tuple(self.deck2)) in self.history:
                return 1
            else:
                self.history.add((tuple(self.deck1), tuple(self.deck2)))
            curr1 = self.deck1.pop(0)
            curr2 = self.deck2.pop(0)
            if curr1 > len(self.deck1) or curr2 > len(self.deck2):
                if curr1 > curr2:
                    self.deck1 += [curr1, curr2]
                else:
                    self.deck2 += [curr2, curr1]
            else:
                sub = Game2(self.deck1[:curr1], self.deck2[:curr2]).game()
                if sub == 1:
                    self.deck1 += [curr1, curr2]
                else:
                    self.deck2 += [curr2, curr1]
        return 1 if self.deck1 else 2


def part2(decks):
    game = Game2(decks[0], decks[1])
    winnerNum = game.game()
    winner = game.deck1 if winnerNum == 1 else game.deck2
    return getScore(winner)


def main():
    decks = readDecks()
    print(f"Part 1: {part1(deepcopy(decks))}\nPart 2: {part2(decks)}")


main()
