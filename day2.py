import fileinput
import parse

def main():
    ok = 0
    game = 0
    for line in fileinput.input():
        game += 1
        maxblue = max(r[0] for r in parse.findall("{:d} blue", line))
        maxred = max(r[0] for r in parse.findall("{:d} red", line))
        maxgreen = max(r[0] for r in parse.findall("{:d} green", line))
        if maxblue <= 14 and maxgreen <= 13 and maxred <= 12:
            ok += game
    print(ok)
    
if __name__ == '__main__':
    main()