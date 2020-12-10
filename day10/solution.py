def readAdapters(inpath="input.txt"):
    with open(inpath, 'r') as infile:
        return [0] + sorted(list(map(int, infile.read().splitlines())))


def part1(adapters):
    diffs = {1: 0, 2: 0, 3: 1}
    for i in range(1, len(adapters)):
        diffs[adapters[i] - adapters[i - 1]] += 1
    return diffs[1] * diffs[3]


def part2(adapters):
    paths = [1] + [0] * (len(adapters) - 1)
    for i, adapter in enumerate(adapters):
        for j in range(i - 3, i):
            if(adapter - adapters[j] <= 3):
                paths[i] += paths[j]

    return paths[-1]


def main():
    adapters = readAdapters()
    print(f"Part 1: {part1(adapters)}\nPart 2: {part2(adapters)}")


main()
