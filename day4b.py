import fileinput
import parse

def main():
    sum = 0
    card_counts = []
    win_counts = []
    points_per_win = []
    tot_cards = 0
    for line in fileinput.input():
        card_counts.append(1)  # original card
        sections = line.split("|")
        winning = [int(r[0]) for r in parse.findall("{:d} ", sections[0])]
        mine = [int(r[0]) for r in parse.findall("{:d}", sections[1])]
        count_won = len(set(winning) & set(mine))
        win_counts.append(count_won)
        if count_won > 0:
            points_per_win.append(1 << (count_won - 1))
        else:
            points_per_win.append(0)

    for i, cnt in enumerate(card_counts):
        for j in range(win_counts[i]):
            card_counts[i+j+1] += card_counts[i]
        #print(str(i+1) + ": num cards " + str(card_counts[i]) + ", points per win " + str(points_per_win[i]))
        sum += card_counts[i] * points_per_win[i]
        tot_cards += card_counts[i]
    #print(sum)
    print(tot_cards)


if __name__ == '__main__':
    main()