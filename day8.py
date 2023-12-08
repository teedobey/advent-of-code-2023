import fileinput
import parse

def main():
    res = 0
    lines = iter(fileinput.input())
    command = next(lines)[:-1]
    unused = next(lines)
    mapping = {}
    for line in lines:
        left = line[7:10]
        right = line[12:15]
        fr = line[0:3]
        print (left + " " + right + " " + fr)
        mapping[fr] = (left, right)

    cur = "AAA"
    index_cmd = 0
    while cur != "ZZZ":
        choice = 0 if command[index_cmd] == "L" else 1
        cur = mapping[cur][choice]
        index_cmd += 1
        index_cmd %= len(command)
        res += 1
    print(res)

if __name__ == "__main__":
    main()