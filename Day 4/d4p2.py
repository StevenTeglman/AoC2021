file = open('Day 4\input4.txt', 'r')
lines = file.readlines()

call_numbers = lines[0].split(",")
call_numbers = [int(z) for z in call_numbers]
lb = lines[1]
lines = lines[1:]
cards = []

i = 0
while i < len(lines):
    if lines[i] == lb:
        i += 1
        cardlines = lines[i:i+5]
        card =[]
        for l in cardlines:
            line = []
            for j in range(0, len(l), 3):
                n = [int(l[j:j+2]), False]
                line.append(n)
            card.append(line)
        cards.append(card)
        i += 5


i=0
last_bingo = False
winning_card = []
last_num = 0
p_cards = cards.copy()
while i < len(call_numbers) and not last_bingo:
    j = i + 1
    called_nums = call_numbers[:j]
    n_cards = []
    # Update Bingo Cards
    for c in p_cards:
        n_card = []
        for l in c:
            n_line = []
            for b in l:
                if b[0] in called_nums:
                    n_b = [b[0], True]
                else:
                    n_b = b
                n_line.append(n_b)
            n_card.append(n_line)
        n_cards.append(n_card)
    
    for nc in n_cards[:]:
        bingo = False
        # Horizontal Bingo Check
        for nh in nc:
            if all(numh[1] == True for numh in nh):
                winning_card = nc
                last_num = called_nums[-1:]
                bingo = True
                if len(n_cards) == 1:
                    winning_card = n_cards[0]
                    last_num = called_nums[-1:]
                    last_bingo = True
                    print("Last BINGO!!")
                    for line in winning_card:
                        print(line)
                    print("Numbers called: {}".format(called_nums))
                    print("Last number called: {}".format(called_nums[-1:]))
                    break
                n_cards.remove(nc)
                break
        
        # Vertical Bingo Check
        x = 0
        while x < 5 and not bingo:
            if all(numh[x][1] == True for numh in nc):
                winning_card = nc
                last_num = called_nums[-1:]
                bingo = True
                if len(n_cards) == 1:
                    winning_card = n_cards[0]
                    last_num = called_nums[-1:]
                    last_bingo = True
                    print("Last BINGO!!")
                    for line in winning_card:
                        print(line)
                    print("Numbers called: {}".format(called_nums))
                    print("Last number called: {}".format(called_nums[-1:]))
                    break
                
                n_cards.remove(nc)
                break
            x += 1

    p_cards = n_cards

    i += 1

win_sum = 0
for l in winning_card:
    for n in l:
        if not n[1]:
            win_sum += int(n[0])

result = win_sum * int(last_num[0])
print("last_num is: {}".format(last_num))
print("win_sum is: {}".format(win_sum))
print("Result is: {}".format(result))
            

    








    
    







