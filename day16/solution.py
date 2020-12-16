def readRule(ruleStr):
    tokens = ruleStr.split(": ")
    ranges = list(map(lambda x: x.split("-"),
                      tokens[1].split(" or ")))
    parts = list(map(lambda x: list(map(int, x)), ranges))
    valid = set(range(parts[0][0], parts[0][1] + 1))
    valid.update(range(parts[1][0], parts[1][1] + 1))
    return (tokens[0], valid)


def readTickets(inpath="input.txt"):
    with open(inpath, "r") as infile:
        parts = list(map(lambda x: x.split("\n"), infile.read().split("\n\n")))
        return {readRule(ruleStr)[0]: readRule(ruleStr)[1] for ruleStr in parts[0]}, list(map(int, parts[1][1].split(","))), list(map(lambda x: list(map(int, x.split(","))), parts[2][1:]))


def validForAny(rules):
    valid = set()
    for rule in rules:
        valid.update(rule)
    return valid


def part1(rules, nearby):
    valid = validForAny(rules.values())

    invalidFound = []
    for ticket in nearby:
        for i in ticket:
            if i not in valid:
                invalidFound.append(i)
    return sum(invalidFound)


def isValid(overall, ticket):
    for i in ticket:
        if i not in overall:
            return False
    return True


def part2(rules, ours, nearby):
    overall = validForAny(rules.values())
    colToRule = {i: set(rules.keys()) for i in range(len(ours))}
    for ticket in nearby:
        if isValid(overall, ticket):
            for i, val in enumerate(ticket):
                for k, valid in rules.items():
                    if val not in valid:
                        colToRule[i].remove(k)

    indToRule = [None for _ in colToRule]

    for j in sorted(colToRule, key=colToRule.get):
        rule = list(colToRule[j] - set(indToRule))[0]
        indToRule[j] = rule

    ans = 1
    for i, val in enumerate(ours):
        if indToRule[i].startswith("departure"):
            ans *= val
    return ans


def main():
    rules, ours, nearby = readTickets()
    print(
        f"Part 1: {part1(rules, nearby)}\nPart 2: {part2(rules, ours, nearby)}")


main()
