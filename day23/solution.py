def part1(cups):
    for _ in range(100):
        removed = cups[1:4]
        dest = cups[0] - 1
        if dest == 0:
            dest = 9
        while dest in removed:
            dest -= 1
            if dest == 0:
                dest = 9
        without = cups[:1] + cups[4:]
        destInd = without.index(dest)
        without = without[:destInd+1] + removed + without[destInd+1:]
        cups = without[1:] + without[:1]
    return "".join(str(x) for x in (cups[cups.index(1)+1:] + cups[:cups.index(1)]))


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def part2(cups):
    lookup = {}

    prev = None
    for i in range(len(cups)-1, -1, -1):
        new = Node(cups[i])
        new.next = prev
        lookup[cups[i]] = new
        prev = new

    for i in range(1000000, 9, -1):
        new = Node(i)
        new.next = prev
        lookup[i] = new
        prev = new

    lookup[cups[-1]].next = lookup[10]

    cur = lookup[cups[0]]

    for _ in range(10000000):
        remove1 = cur.next
        remove2 = remove1.next
        remove3 = remove2.next
        cur.next = remove3.next
        removed = {cur.val, remove1.val, remove2.val, remove3.val}
        cval = cur.val
        while cval in removed:
            cval -= 1
            if cval == 0:
                cval = 1000000
        targetLoc = lookup[cval]
        afterTarget = targetLoc.next

        targetLoc.next = remove1
        remove3.next = afterTarget

        cur = cur.next

    cup1 = lookup[1]
    remove1 = cup1.next
    remove2 = remove1.next

    return remove1.val * remove2.val


def main():
    cups = [int(x) for x in "942387615"]

    print(f"Part 1: {part1(cups)}\nPart 2: {part2(cups)}")


main()
