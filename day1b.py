import fileinput

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
to_digit = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0,
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

def main():
  sum = 0
  for line in fileinput.input():
    first_digits = [(to_digit[x], line.find(x)) for x in digits if x in line]
    last_digits = [(to_digit[x], line.rfind(x)) for x in digits if x in line]
    first_digit = min(first_digits, key=lambda x: x[1])[0]
    last_digit = max(last_digits, key=lambda x: x[1])[0]
    sum += int(first_digit)*10 + int(last_digit)
  print(sum)
  
if __name__ == '__main__':
    main()