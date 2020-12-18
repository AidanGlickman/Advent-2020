import re


def readExps(inpath="input.txt"):
    with open(inpath, "r") as infile:
        return infile.read().splitlines()


class Num1(int):
    def __add__(self, b):
        return Num1(self.real + b.real)

    def __sub__(self, b):
        return Num1(self.real * b.real)


def part1(exps):
    replaced = [exp.replace('*', '-') for exp in exps]
    return sum([eval(
        re.sub(r"(\d+)", r"Num1(\1)", repEx)) for repEx in replaced])


class Num2(int):
    def __add__(self, b):
        return Num2(self.real * b.real)

    def __mul__(self, b):
        return Num2(self.real + b.real)


def part2(exps):
    replaced = [exp.replace('*', '-').replace('+', '*').replace('-', '+')
                for exp in exps]
    return sum([eval(re.sub(r"(\d+)", r"Num2(\1)", repEx)) for repEx in replaced])


def main():
    exps = readExps()
    print(f"Part 1: {part1(exps)}\nPart 2: {part2(exps)}")


main()
