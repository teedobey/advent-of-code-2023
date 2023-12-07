import fileinput
import parse

def main():
    res = 0
    lines = iter(fileinput.input())
    hands = []
    bids = []
    hand_bids = []
    for line in lines:
        items = line[:-1].split(" ")
        hands.append(items[0])
        bids.append(int(items[1]))
        hand_bids.append((items[0], int(items[1])))
    for i, hand in enumerate(hands):
        print("Hand: " + hand + " key: " + str(key(hand)))
    hand_bids.sort(key=lambda x: key(x[0]))
    for i, hand_bid in enumerate(hand_bids):
        print("Hand: " + hand_bid[0] + " Bid:" + str(hand_bid[1]))
        res += (i + 1) * hand_bid[1]
    print(res)


# [type, order]
def key(hand):
  combo_hand = 0
  for i in hand:
      combo_hand *= 13
      combo_hand += cardkey(i)
  print(combo_hand)
  combo_type = 0
  possible_non_joker_hands = gen_hands(hand)
  if any(is_five_of_kind(h) for h in possible_non_joker_hands):
      combo_type = 6
  elif any(is_four_of_kind(h) for h in possible_non_joker_hands):
      combo_type = 5
  elif any(is_full_house(h) for h in possible_non_joker_hands):
      combo_type = 4
  elif any(is_three_of_kind(h) for h in possible_non_joker_hands):
      combo_type = 3
  elif any(is_two_pair(h) for h in possible_non_joker_hands):
      combo_type = 2
  elif any(is_one_pair(h) for h in possible_non_joker_hands):
       combo_type = 1
  print(combo_type)
  return [combo_type, combo_hand]

def gen_hands(hand):
    hands = [""]
    for card in hand:
        if card != 'J':
            for j, unused in enumerate(hands):
                hands[j] += card
        else:
            new_hands = []
            for j, ex_hand in enumerate(hands):
                for k in ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
                    new_hands.append(ex_hand + k)
            hands = new_hands
    return hands

def is_five_of_kind(hand):
    return len(set(x for x in hand)) == 1

def is_four_of_kind(hand):
    freq = { x: hand.count(x) for x in hand }
    return 4 in freq.values()

def is_full_house(hand):
    freq = { x: hand.count(x) for x in hand }
    return 3 in freq.values() and 2 in freq.values()

def is_three_of_kind(hand):
    freq = { x: hand.count(x) for x in hand }
    return 3 in freq.values() and 2 not in freq.values()

def is_two_pair(hand):
    freq = { x: hand.count(x) for x in hand }
    return list(freq.values()).count(2) == 2

def is_one_pair(hand):
    freq = { x: hand.count(x) for x in hand }
    return list(freq.values()).count(2) == 1 and list(freq.values()).count(1) == 3

def cardkey(singlecard):
    return {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}[singlecard[0]]


if __name__ == "__main__":
    main()
