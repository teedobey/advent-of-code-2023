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

    cur = [k for k in mapping.keys() if k[2] == "A"]
    cycles = [count_cycles(c, command, mapping) for c in cur]
    product = 1
    for c in cycles:
        gcd = count_gcd(product, c)
        product *= c
        product = int(product / gcd)
        print(product)
        print(gcd)        
    print(cycles)
    print(product)


def count_cycles(cur, command, mapping):
    index_cmd = 0
    res = 0
    while not cur[2] == "Z":
        choice = 0 if command[index_cmd] == "L" else 1
        cur = mapping[cur][choice]
        index_cmd += 1
        index_cmd %= len(command)
        res += 1
    return res


def count_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    main()