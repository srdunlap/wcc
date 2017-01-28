# def multiply(a, b):
#     result = a * b
#     return result
#
# print(multiply(4,5)) # 20
# print(multiply(9,11)) # 99
# print(multiply(0,10)) # 0
# print(multiply(.5,9)) # 4.5
# print(multiply(-1, -55)) # 55
# print(multiply(3, 'Hello')) # 'HelloHelloHello'
#
# def isPositive(a):
#     if a > 0:
#         return True
#     else:
#         return False
#
# print(isPositive(-4)) # Expected: False
# print(isPositive(4)) # Expected: True
# print(isPositive(-9.9)) # Expected: False
# print(isPositive(9.9)) # Expected: True
#
# import random
#
# def draw_random_card():
#     cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
#     random.shuffle(cards)
#     return cards.pop()
#
# # Test the function
# print(draw_random_card()) # Expected: Random number b/n 1 & 11
# print(draw_random_card()) # Expected: Random number b/n 1 & 11
# print(draw_random_card()) # Expected: Random number b/n 1 & 11

# def display_winner(winner, msg):
#     if winner == 'Player':
#         outcome = 'You win! '
#     else:
#         outcome = 'Computer wins! '
#
#     print(outcome + '(' + msg + ')')
#
# # Test the function
# display_winner('Player', 'You were closest to 21') # Expected: You win! (You were closest to 21)
# display_winner('Computer', 'It was closest to 21') # Expected: Computer wins! (It was closest to 21)
# display_winner('Computer', 'You busted')  # Expected: Computer wins! (You busted)



# display_winner('Player', 'You were closest to 21') # Expected: You win! (You were closest to 21)
# display_winner('Computer', 'It was closest to 21') # Expected: Computer wins! (It was closest to 21)
# display_winner('Computer', 'You busted')  # Expected: Computer wins! (You busted)



# def calculate_lucky_number(birth_month, birth_day):
#
#     lucky_number = birth_month;
#
#     if birth_month in [2, 4, 6]:
#         lucky_number = birth_month + birth_day
#         return lucky_number
#     elif birth_month in [8, 10, 12]:
#         lucky_number = (birth_month * 10) - birth_day
#         return lucky_number
#
#     return lucky_number * 2



#
# def mystery(x, y, z):
#
#     return x + (y * z)
#
# # Test this function:
# print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
# print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'
#


#
# def goose(a,b,c):
#
#     return a + (b * c)
#
#
# print goose('Oh you ', 3, '!')
# print goose('You are such a goose ', '!!!', 3 )
#
#
# def bingo (d,y,m):
#
#     return d * 2 + y * 3 + m * 3
#
# print bingo ('cat' , 'dog', 'bird')
#
#
# def cat(a,b,c):
#     return a + (b * c)
#
# print cat('I have a cat' , 3, '!')
#
#
# def sarah(a,b,c):
#     return a + b + (c *3)
#
# print sarah('Hi my name' , 'is Sarah' , '!', )


def calc_tip(meal_price, rating)

if rating=='A':
    percent=.2;

elif rating =='B':
    percent=.18

else
    percent=.15

tip_amount: meal_price * rating;

return tip_amount
