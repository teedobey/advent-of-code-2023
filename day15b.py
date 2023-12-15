import fileinput
import parse


def main():
    total = 0
    lines = iter(fileinput.input())
    for line in lines:
        cmds = line[:-1].split(",")
        mp, pow = process(cmds)
        print(pow)
        for boxi, p in enumerate(pow):
            for i, pw in enumerate(p):
                total += (boxi + 1) * (i+1) * pw
    print(F"OK {total}")

def process(cmds):
    mp = [[] for x in range(0, 256)]
    pow = [[] for x in range(0,256)]
    for cmd in cmds:
        label = cmd.split("=")[0].split("-")[0]
        if "=" in cmd:
            power = int(cmd.split("=")[1])
            box = hash(label)
            if label in mp[box]:
                idx = mp[box].index(label)
                pow[box][idx] = power
            else:
                mp[box].append(label)
                pow[box].append(power)
        elif "-" in cmd:
            box = hash(label)
            if label in mp[box]:
                idx = mp[box].index(label)
                mp[box].remove(label)
                del pow[box][idx]
    return (mp, pow)


def hash(s):
    current = 0
    for ch in s:
        current += ord(ch)
        current *= 17
        current %= 256
    return current


if __name__ == '__main__':
    main()