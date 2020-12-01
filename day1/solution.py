def readEntries(filename="input.txt"):
    with open(filename, "r") as filein:
        return [int(line.rstrip()) for line in filein]


def part1(entries):
    entriesset = set(entries)
    if 1010 in entries:
        return 1010 ** 2
    for i in entries:
        if (2020 - i) in entriesset:
            return f"{i} * {2020 - i} = {i * (2020  - i)}"


def part2(entries):
    entriesset = set(entries)
    for x, i in enumerate(entries[:-1]):
        for j in entries[x:]:
            if (2020 - (i + j)) in entriesset:
                return f"{i} * {j} * {2020 - (i + j)} = {i * j * (2020 - (i + j))}"


def main():
    entries = readEntries()
    print(part1(entries))
    print(part2(entries))


main()
