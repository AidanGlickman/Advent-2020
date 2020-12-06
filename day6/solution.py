def readGroups(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return infile.read().split('\n\n')


def part1(groups):
    count = 0
    for group in groups:
        unique = set("".join(group.split()))
        count += len(unique)
    return count


def part2(groups):
    count = 0
    for group in groups:
        people = list(map(set, group.split("\n")))
        count += len(people[0].intersection(*people[1:]))
    return count


def main():
    groups = readGroups()
    print(f"Part 1: {part1(groups)}\nPart 2: {part2(groups)}")


main()
