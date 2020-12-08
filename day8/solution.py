def readInst(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return infile.read().splitlines()


def resolve(inst):
    visited = set()
    ind = 0
    acc = 0

    while ind < len(inst):
        if ind in visited:
            return False, acc
        visited.add(ind)
        curr, val = inst[ind].split()
        if curr == "jmp":
            ind += int(val)
        else:
            if curr == "acc":
                acc += int(val)
            ind += 1

    return True, acc


def part1(inst):
    return resolve(inst)[1]


def part2(inst):
    for i, line in enumerate(inst):
        tokens = line.split()
        fixed = []
        if tokens[0] == "nop":
            fixed = inst[:i] + ["jmp " + tokens[1]] + inst[i+1:]
        elif tokens[0] == "jmp":
            fixed = inst[:i] + ["nop " + tokens[1]] + inst[i+1:]
        if fixed != []:
            resolved = resolve(fixed)
            if resolved[0]:
                return resolved[1]


def main():
    inst = readInst()
    print(f"Part 1: {part1(inst)}\nPart 2: {part2(inst)}")


main()
