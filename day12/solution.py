def readInsts(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return infile.read().splitlines()


DIRS = {"N": (1, 0), "E": (0, 1), "S": (-1, 0), "W": (0, -1)}
ROTS = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}


def part1(insts):
    pos = [0, 0]
    face = 90
    for inst in insts:
        dirc = inst[:1]
        val = int(inst[1:])
        if dirc == "F":
            y, x = ROTS[face]
            pos[0] += y * val
            pos[1] += x * val
        elif dirc == "L":
            face = (face - val) % 360
        elif dirc == "R":
            face = (face + val) % 360
        else:
            y, x = DIRS[dirc]
            pos[0] += y * val
            pos[1] += x * val
    return abs(pos[0]) + abs(pos[1])


def rotateWaypoint(way, val):
    tmp = way[0]
    if val == 90:
        way[0] = 0 - way[1]
        way[1] = tmp
    elif val == 180:
        way[0] = 0 - way[0]
        way[1] = 0 - way[1]
    elif val == 270:
        way[0] = way[1]
        way[1] = 0 - tmp


def part2(insts):
    ship = [0, 0]
    way = [1, 10]
    for inst in insts:
        dirc = inst[:1]
        val = int(inst[1:])
        if dirc == "F":
            y, x = way
            ship[0] += y * val
            ship[1] += x * val
        elif dirc == "L":
            rotateWaypoint(way, (0 - val) % 360)
        elif dirc == "R":
            rotateWaypoint(way, val)
        else:
            y, x = DIRS[dirc]
            way[0] += y * val
            way[1] += x * val
    return abs(ship[0]) + abs(ship[1])


def main():
    insts = readInsts()
    print(f"Part 1: {part1(insts)}\nPart 2: {part2(insts)}")


main()
