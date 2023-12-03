import fileinput

def main():
    sum = 0
    chars = []
    for line in fileinput.input():
        chars.append(line[:-1])  # assumes all lines end with \n
    curfigure = 0
    numbers = []
    for y, line in enumerate(chars):
        for x, ch in enumerate(line):
            if ch == "*":
                numbers += getadjacent(x, y, -1, chars)
                numbers += getadjacent(x, y, 0, chars)
                numbers += getadjacent(x, y, 1, chars)
                if len(numbers) == 2:
                    sum += numbers[0] * numbers[1]
                numbers = []
    print(sum)                

def getadjacent(target_x, y, y_delta, chars):
    res = []
    if y + y_delta < 0 or y+ y_delta >= len(chars):
        return []
    target_row = y + y_delta
    curfigure = 0
    start_x = 0
    for x, ch in enumerate(chars[target_row]):
        if ch.isdigit():
            if curfigure == 0:
                start_x = x
            curfigure = curfigure * 10 + int(ch)
        else:
            if curfigure != 0:            
                if (target_x >= x-2 and target_x <= x) or (start_x >= target_x-1 and start_x <= target_x+1):
                    res.append(curfigure)
                curfigure = 0
    if curfigure != 0:
        if (start_x >= target_x-1 and start_x <= target_x+1):
            res.append(curfigure)
    return res

def issymbol(ch):
    return not ch.isdigit() and ch != '.'

if __name__ == '__main__':
    main()