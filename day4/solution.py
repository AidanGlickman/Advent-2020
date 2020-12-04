def readPass(inpath="input.txt"):
    with open(inpath, "r") as infile:
        passports = infile.read().split('\n\n')
        return passports


def part1(passports):
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    count = 0
    for passport in passports:
        keys = set(map(lambda x: x.split(':')[0], passport.split()))
        if keys.issuperset(required):
            count += 1
    return count


def keyFilter(passports):
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid = []
    for passport in passports:
        passDict = {pair.split(':')[0]: pair.split(':')[1]
                    for pair in passport.split()}
        if set(passDict.keys()).issuperset(required):
            valid.append(passDict)
    return valid


def altPart1(passports):
    valid = keyFilter(passports)
    return len(valid)


def part2(passports):
    count = 0
    for passDict in keyFilter(passports):
        print(passDict)
        try:
            if (1920 <= int(passDict['byr']) <= 2002):
                print('BYR')
                if (2010 <= int(passDict['iyr']) <= 2020):
                    print('IYR')
                    if (2020 <= int(passDict['eyr']) <= 2030):
                        print('EYR')
                        if ((passDict['hgt'][-2:] == 'cm' and (150 <= int(passDict['hgt'][:-2]) <= 193))
                                or (passDict['hgt'][-2:] == 'in' and (59 <= int(passDict['hgt'][:-2]) <= 76))):
                            print('HGT')
                            if passDict['hcl'][0] == '#' and hex(int(passDict['hcl'][1:], 16))[2:] == passDict['hcl'][1:]:
                                print('HCL')
                                if passDict['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                                    print('ECL')
                                    if (len(passDict['pid']) == 9 and passDict['pid'].isnumeric()):
                                        print('PID')
                                        count += 1
        except:
            continue

    return count


def main():
    passports = readPass(inpath="input.txt")
    print(f"Part 1: {altPart1(passports)}\n Part 2: {part2(passports)}")


main()
