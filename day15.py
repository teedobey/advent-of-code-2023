import fileinput
import parse


def main():
    total = 0
    lines = iter(fileinput.input())
    for line in lines:
        for seg in line[:-1].split(","):
            total += hash(seg, 0)
    print(F"OK {total}")

def hash(s, current):
    for ch in s:
        current += ord(ch)
        current *= 17
        current %= 256
    return current


if __name__ == '__main__':
    main()