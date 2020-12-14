def readInsts(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return list(map(lambda x: x.split(" = "), infile.read().splitlines()))


def part1(insts):
    vals = {}
    mask = "X" * 36
    for inst in insts:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            curr = list(mask)
            ind = inst[0][4:-1]
            val = str(bin(int(inst[1])))[2:]
            val = "0" * (len(curr) - len(val)) + val
            for i in range(len(curr)):
                if curr[i] == "X":
                    curr[i] = val[i]
            vals[ind] = int("".join(curr), 2)
    return sum(vals.values())


def part2(insts):
    vals = {}
    mask = "0" * 36
    for inst in insts:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            curr = list(mask)
            ind = str(bin(int(inst[0][4:-1])))[2:]
            ind = "0" * (len(curr) - len(ind)) + ind
            val = int(inst[1])
            floating = []

            for i in range(len(curr)):
                if curr[i] == "0":
                    curr[i] = ind[i]
                if curr[i] == "X":
                    floating.append(i)

            for i in range(2 ** len(floating)):
                currind = curr[:]
                binstr = str(bin(i))[2:]
                binstr = "0" * (len(floating) - len(binstr)) + binstr
                for i, j in zip(floating, binstr):
                    currind[i] = j
                vals["".join(currind)] = val
    return sum(vals.values())


def main():
    insts = readInsts()
    print(f"Part 1: {part1(insts)}\nPart 2: {part2(insts)}")


main()
