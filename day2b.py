import fileinput
import parse

def main():
    res = 0
    for line in fileinput.input():
        maxblue = max(r[0] for r in parse.findall("{:d} blue", line))
        maxred = max(r[0] for r in parse.findall("{:d} red", line))
        maxgreen = max(r[0] for r in parse.findall("{:d} green", line))        
        res += maxblue * maxred * maxgreen
    print(res)
    
if __name__ == '__main__':
    main()