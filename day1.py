import fileinput

def main():
  sum = 0
  for line in fileinput.input():
    first_digit = [x for x in line if x.isdigit()][0]
    last_digit = [x for x in line if x.isdigit()][-1]
    sum += int(first_digit)*10 + int(last_digit)
  print(sum)

if __name__ == '__main__':
    main()