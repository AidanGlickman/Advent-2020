class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}

    def __str__(self):
        return f"{self.id}: {self.adjacent}"

    def addAdjacent(self, other, weight):
        self.adjacent[other] = weight

    def getParents(self):
        parents = {}
        for i in self.adjacent.keys():
            if self.adjacent[i] < 0:
                parents[i] = self.adjacent[i]
        return parents

    def getChildren(self):
        children = {}
        for i in self.adjacent.keys():
            if self.adjacent[i] > 0:
                children[i] = self.adjacent[i]
        return children

    def getEdge(self, other):
        return self.adjacent[other]


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, id):
        if id not in self.nodes.keys():
            self.nodes[id] = Node(id)

    def getNode(self, id):
        return self.nodes[id] if id in self.nodes.keys() else None

    def addEdge(self, parent, child, weight):
        weight = abs(weight)
        if parent not in self.nodes.keys():
            self.addNode(parent)
        if child not in self.nodes.keys():
            self.addNode(child)

        self.nodes[parent].addAdjacent(child, weight)
        self.nodes[child].addAdjacent(parent, 0 - weight)


def readRules(inpath="input.txt"):
    rules = Graph()
    with open(inpath, "r") as infile:
        for line in infile.read().splitlines():
            key, contents = line.split("bags contain ")
            rules.addNode(key.strip())
            if("no other" in line):
                continue
            contentlist = contents.split(", ")
            for item in contentlist:
                itemTokens = item.split()
                rules.addEdge(key.strip(), " ".join(
                    itemTokens[1:-1]).strip(), int(itemTokens[0]))

    return rules


def part1(rules):
    valid = set()
    start = rules.getNode("shiny gold")
    toProcess = set(start.getParents().keys())
    while len(toProcess) != 0:
        curr = toProcess.pop()
        toProcess.update(rules.getNode(curr).getParents().keys())
        valid.add(curr)
    return len(valid)


def getNumBags(rules, id):
    node = rules.getNode(id)
    children = node.getChildren()
    if len(children) == 0:
        return 1
    else:
        return 1 + sum([children[i] * getNumBags(rules, i) for i in children])


def part2(rules):
    return getNumBags(rules, "shiny gold") - 1


def main():
    rules = readRules()
    print(f"Part 1: {part1(rules)}\nPart 2: {part2(rules)}")


main()
