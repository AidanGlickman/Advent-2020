DIRECTIONS = {"e": [2, 0], "se": [1, -1], "sw": [-1, -1],
              "w": [-2, 0], "nw": [-1, 1], "ne": [1, 1]}


def readData(inpath="input.txt"):
    with open(inpath, "r") as infile:
        paths = []
        for line in infile.read().splitlines():
            instructions = []
            curr = ""
            for i in line:
                if curr + i in DIRECTIONS.keys():
                    instructions.append(curr + i)
                    curr = ""
                else:
                    curr = i
            paths.append(instructions)
        return paths


def initBoard(paths):
    flipped = set()
    for path in paths:
        coords = [0, 0]
        for inst in path:
            curr = DIRECTIONS[inst]
            for i in range(len(coords)):
                coords[i] += curr[i]
        tuped = tuple(coords)
        if tuped not in flipped:
            flipped.add(tuped)
        else:
            flipped.remove(tuped)
    return flipped


def part1(data):
    return len(initBoard(data))


def part2(data):
    black = initBoard(data)
    for _ in range(100):
        neighbored = {}
        for tile in black:
            if tile not in neighbored:
                neighbored[tile] = 0
            for token in DIRECTIONS.keys():
                curr = list(tile)
                for j in range(len(curr)):
                    curr[j] += DIRECTIONS[token][j]
                curr = tuple(curr)
                if curr not in neighbored.keys():
                    neighbored[curr] = 1
                else:
                    neighbored[curr] += 1
        newBlack = set()
        for tile in neighbored:
            if (tile in black and neighbored[tile] in [1, 2]) or \
                    (tile not in black and neighbored[tile] == 2):
                newBlack.add(tile)
        black = newBlack
    return len(black)


def main():
    data = readData()
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")


main()
