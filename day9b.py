import fileinput
import parse

def main():
    sum_elem = []
    sum = 0
    lines = iter(fileinput.input())
    for line in lines:
        sum_elem = []
        nums = [int(x) for x in line[:-1].split(" ")]
        sum_elem.append(nums[0])
        while not all([x == 0 for x in nums]):
            new_nums = []
            for i in range(1, len(nums)):
                new_nums.append(nums[i] - nums[i-1])
            sum_elem.append(new_nums[0])
            nums = new_nums
        for i, x in enumerate(sum_elem):
            if i % 2 == 0:
                sum += x
            else:
                sum -= x
    print(sum)

if __name__ == "__main__":
    main()

# d-c+b-a 