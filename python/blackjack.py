import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#print(cards)

random.shuffle(cards)

print(cards)

player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))
print(cards)

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')
if decision == 'h':
    player_card2 = cards.pop()
    print('Player card: ' + str(player_card2))
if decision == 's':
    player_card2=0


computer_card2 = cards.pop()
print('Computer card: ' + str(computer_card2))

print('Player cards: ' + str([player_card1 , player_card2]))
print('Computer cards: ' + str([computer_card1, computer_card2]))


decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')
if decision == 'h':
    player_card3 = cards.pop()
    print('Player card: ' + str(player_card3))
if decision == 's':
    player_card3=0

if computer_card1 + computer_card2 <= 16:
    computer_card3 = cards.pop()
if computer_card1 + computer_card2 > 16:
    computer_card3 = 0
    print('Computer cards: ' + str(computer_card3))


print('Player cards: ' + str([player_card1 , player_card2, player_card3]))
print('Computer cards: ' + str([computer_card1, computer_card2, computer_card3 ]))

print('Game Over')
print('Player score: ' + str(player_card1 + player_card2 + player_card3))
print('Computer score: ' + str(computer_card1 + computer_card2 + computer_card3))


player_total = player_card1 + player_card2 + player_card3
computer_total = computer_card1 + computer_card2 + computer_card3

if player_total > 21 and computer_total > 21:
    print('Tie! You both busted!')
elif player_total == computer_total and player_total <=21 and computer_total<=21:
    print ('Tie!!')
elif player_total <=21 and computer_total >21:
    print ('You Won!')
elif player_total > 21 and computer_total <= 21:
    print('You failed! Computer beat you because you busted!')

elif computer_total <= 21 and player_total <= 21 and player_total > computer_total:
    print('You Won!')
elif computer_total <= 21 and player_total <= 21 and computer_total > player_total:
    print('Computer Won! Your total was lower!')
