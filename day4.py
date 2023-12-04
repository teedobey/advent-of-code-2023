import fileinput
import parse

def main():
    sum = 0
    for line in fileinput.input():
        sections = line.split("|")
        winning = [int(r[0]) for r in parse.findall("{:d} ", sections[0])]
        mine = [int(r[0]) for r in parse.findall("{:d}", sections[1])]
        count_won = len(set(winning) & set(mine))
        if count_won > 0:
            sum += (1 << (count_won - 1))
    print(sum)

if __name__ == '__main__':
    main()