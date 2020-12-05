def readSeats(inpath="input.txt"):
    with open(inpath, 'r') as infile:
        return infile.read().splitlines()


def getSeatLocation(seat):
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
    return row, col


def getSeatId(seat):
    row, col = getSeatLocation(seat)
    return row * 8 + col


def part1(seats):
    maxVal = 0
    for seat in seats:
        seatId = getSeatId(seat)

        if seatId > maxVal:
            maxVal = seatId
    return maxVal


def part2(seats):
    unseen = list(range(part1(seats) + 1))
    for seat in seats:
        unseen.remove(getSeatId(seat))
    return unseen[-1]


def main():
    seats = readSeats()
    print(f"Part 1: {part1(seats)}\nPart 2: {part2(seats)}")


main()
