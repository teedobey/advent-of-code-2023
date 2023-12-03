import fileinput

def main():
    sum = 0
    chars = []
    for line in fileinput.input():
        chars.append(line[:-1])  # assumes all lines end with \n
    curfigure = 0
    connected = False
    for y, line in enumerate(chars):
        for x, ch in enumerate(line):
            if x == 0:
                if connected:
                    sum += curfigure  
                curfigure = 0
                connected = False
            if ch.isdigit():
                curfigure = curfigure * 10 + int(ch)
                if isconnected(x, y, chars):
                    connected = True
            else:
                if connected:
                    sum += curfigure
                curfigure = 0
                connected = False
    if curfigure != 0:
        if connected:
            sum += curfigure
    print(sum)                

def isconnected(x, y, chars):
    if y > 0:
        if isconnected_row(x, y-1, chars):
            return True
    if isconnected_row(x, y, chars):
        return True
    if y < len(chars) - 1:
        if isconnected_row(x, y+1, chars):
            return True
    return False
    
def isconnected_row(x, y, chars):
    if x > 0:
        if issymbol(chars[y][x-1]):
            return True
    if issymbol(chars[y][x]):
        return True
    if x < len(chars[y]) - 1:
        if issymbol(chars[y][x+1]):
            return True
    return False

def issymbol(ch):
    return not ch.isdigit() and ch != '.'

if __name__ == '__main__':
    main()