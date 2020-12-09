def readCipher(inpath="input.txt"):
    with open(inpath, 'r') as infile:
        return list(map(int, infile.read().splitlines()))


def isValid(i, cipher):
    target = cipher[i]
    prev = cipher[i-25: i]
    if prev.count(target/2) > 1:
        return True
    prevSet = set(prev)
    prevSet.discard(target/2)
    for num in prevSet:
        if target-num in prevSet:
            return True
    return False


def part1(cipher):
    for i in range(25, len(cipher)):
        if not isValid(i, cipher):
            return cipher[i]


def part2(cipher):
    target = part1(cipher)
    for i, num in enumerate(cipher):
        run = [num]
        next = i+1
        while sum(run) < target:
            run.append(cipher[next])
            next += 1
        if len(run) >= 2 and sum(run) == target:
            return min(run) + max(run)


def main():
    cipher = readCipher()
    print(f"Part 1: {part1(cipher)}\nPart 2: {part2(cipher)}")


main()
