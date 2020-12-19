def parseRules(rawRules):
    rules = {}
    for line in rawRules.split('\n'):
        k, rule = line.split(': ')
        if rule[0] == '"':
            rule = rule[1:-1]
        else:
            rule = [seq.split(' ') if ' ' in seq else [seq]
                    for seq in (rule.split(' | ') if ' | ' in rule else [rule])]
        rules[k] = rule
    return rules


def readData(inpath="input.txt"):
    with open(inpath, 'r') as infile:
        rawRules, rawStrings = infile.read().split("\n\n")
        return parseRules(rawRules), rawStrings.split("\n")


def checkSequence(grammar, seq, string):
    if not seq:
        yield string
    else:
        index, *seq = seq
        for string in run(grammar, index, string):
            yield from checkSequence(grammar, seq, string)


def runExpand(grammar, alt, string):
    for seq in alt:
        yield from checkSequence(grammar, seq, string)


def run(grammar, index, string):
    if isinstance(grammar[index], list):
        yield from runExpand(grammar, grammar[index], string)
    else:
        if string and string[0] == grammar[index]:
            yield string[1:]


def match(grammar, string):
    return any(m == '' for m in run(grammar, '0', string))


def part1(rules, strings):
    return sum(match(rules, s) for s in strings)


def part2(rules, strings):
    rules = {**rules, '8': [['42'], ['42', '8']],
             '11': [['42', '31'], ['42', '11', '31']]}
    return sum(match(rules, s) for s in strings)


def main():
    rules, strings = readData()
    print(f"Part 1: {part1(rules, strings)}\nPart 2: {part2(rules, strings)}")


main()
