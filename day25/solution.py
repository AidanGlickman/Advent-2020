def readData(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return [int(x) for x in infile.read().splitlines()]


SUB = 7


def findLoop(pub):
    loop = 0
    val = 1
    while(val != pub):
        val *= SUB
        val %= 20201227
        loop += 1
    return loop


def trans(loop, pub):
    val = 1
    for _ in range(loop):
        val *= pub
        val %= 20201227
    return val


def part1(cardPub, doorPub):
    doorLoop = findLoop(doorPub)
    return trans(doorLoop, cardPub)


def part2(cardPub, doorPub):
    return "DONE!"


def main():
    cardPub, doorPub = readData()
    print(
        f"Part 1: {part1(cardPub, doorPub)}\nPart 2: {part2(cardPub, doorPub)}")


main()
