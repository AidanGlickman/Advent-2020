def readEntries(filename="input.txt"):
    with open(filename, "r") as filein:
        return [int(line.rstrip()) for line in filein]


def part1(entries):
    entriesset = set(entries)
    if 1010 in entriesset:
        if entries.count(1010) > 1:
            return f"1010 * 1010 = {1010 ** 2}"
    else:
        entriesset.remove(1010)
    for i in entriesset:
        if (2020 - i) in entriesset:
            return f"{i} * {2020 - i} = {i * (2020  - i)}"


def part2(entries):
    entriesset = set(entries)
    for x, i in enumerate(entries[:-1]):
        for j in entries[x:]:
            if (2020 - (i + j)) in entriesset:
                if (2020 - (i + j) == i and entries.count(i) == 1) or (2020 - (i + j) == j and entries.count(j) == 1):
                    continue
                return f"{i} * {j} * {2020 - (i + j)} = {i * j * (2020 - (i + j))}"


def main():
    entries = readEntries()
    print(part1(entries))
    print(part2(entries))


main()
