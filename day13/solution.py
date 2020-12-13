from math import prod


def readNotes(inpath="input.txt"):
    with open(inpath, "r") as infile:
        lines = infile.read().splitlines()
        return int(lines[0]), lines[1].split(",")


def calcDist(earliest, i):
    return i * (earliest // i + 1) - earliest


def part1(earliest, ids):
    idlist = list(map(int, filter(lambda x: x != "x", ids)))
    closest = [ids[0], calcDist(earliest, idlist[0])]
    for i in idlist[1:]:
        currDist = calcDist(earliest, i)
        if currDist < closest[1]:
            closest = [i, currDist]
    return closest[0] * closest[1]


def chiRem(n, a):
    sum = 0
    product = prod(n)
    for i, j in zip(n, a):
        p = product // i
        sum += j * modInv(p, i) * p
    return sum % product


def modInv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part2(ids):
    n = []
    a = []
    for i in range(0, len(ids)):
        t = ids[i]
        if t != "x":
            n.append(int(t))
            a.append(int(t)-i)
    return chiRem(n, a)


def main():
    earliest, ids = readNotes()
    print(f"Part 1: {part1(earliest, ids)}\nPart 2: {part2(ids)}")


main()
