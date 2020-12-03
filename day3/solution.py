def findtrees(inarr, y, x):
    curry = 0
    currx = 0
    count = 0
    while curry < len(inarr):
        if inarr[curry][currx % len(inarr[0])] == "#":
            count += 1
        curry += y
        currx += x
    return count


def part1(inarr):
    return findtrees(inarr, 1, 3)


def part2(inarr):
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    treeprod = 1
    for i in slopes:
        treeprod *= findtrees(inarr, i[0], i[1])
    return treeprod


def main():
    with open("input.txt", "r") as infile:
        inarr = list(map(lambda x: x.rstrip(), infile.readlines()))

    print(f"Part 1: {part1(inarr)}\nPart 2: {part2(inarr)}")


main()
