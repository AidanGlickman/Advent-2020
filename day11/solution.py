def readGrid(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return list(map(list, infile.read().splitlines()))


def run(grid, check, tol):
    while True:
        toFill = []
        toEmpty = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                if curr == ".":
                    continue
                adjCount = check(grid, i, j)
                if curr == "L" and adjCount == 0:
                    toFill.append((i, j))
                elif curr == "#" and adjCount >= tol:
                    toEmpty.append((i, j))
        for seat in toFill:
            grid[seat[0]][seat[1]] = "#"
        for seat in toEmpty:
            grid[seat[0]][seat[1]] = "L"
        if len(toFill) + len(toEmpty) == 0:
            return sum(map(lambda x: x.count("#"), grid))


def checkAdj(grid, i, j):
    count = 0
    for y in range(max(0, i-1), min(len(grid), i+2)):
        for x in range(max(0, j-1), min(len(grid[1]), j+2)):
            if not(y == i and x == j) and grid[y][x] == "#":
                count += 1
    return count


def part1(grid):
    return run(grid, checkAdj, 4)


DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def checkVis(grid, i, j):
    count = 0
    for dir in DIRS:
        curr = [i + dir[0], j + dir[1]]
        found = False
        while (0 <= curr[0] < len(grid)) and (0 <= curr[1] < len(grid[0])) and not found:
            currVal = grid[curr[0]][curr[1]]
            if currVal == "#":
                count += 1
                found = True
            elif currVal == "L":
                found = True
            else:
                curr[0] += dir[0]
                curr[1] += dir[1]
    return count


def part2(grid):
    return run(grid, checkVis, 5)


def main():
    grid = readGrid()
    from copy import deepcopy
    print(f"Part 1: {part1(deepcopy(grid))}\nPart 2: {part2(grid)}")


main()
