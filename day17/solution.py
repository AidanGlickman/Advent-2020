from itertools import product


def readInit(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return infile.read().splitlines()


def initOn(init, dimensions):
    on = set()
    for i, row in enumerate(init):
        for j, val in enumerate(row):
            if val == '#':
                on.add(tuple([i, j] + [0] * (dimensions-2)))
    return on


def iter(init, dimensions, steps):
    on = initOn(init, dimensions)
    for _ in range(steps):
        c = {}
        for loc in on:
            for neighbor in product([-1, 0, 1], repeat=dimensions):
                new = tuple(map(sum, zip(loc, neighbor)))
                if new != loc:
                    if new not in c.keys():
                        c[new] = 1
                    else:
                        c[new] += 1
        stayOn = set(
            [loc for loc in on if loc in c.keys() and c[loc] in [2, 3]])
        turnOn = set([loc for loc, v in c.items()
                      if loc not in on and v == 3])
        on = stayOn | turnOn
    return len(on)


def part1(init):
    return iter(init, 3, 6)


def part2(init):
    return iter(init, 4, 6)


def main():
    init = readInit()
    print(f"Part 1: {part1(init)}\nPart 2: {part2(init)}")


main()
