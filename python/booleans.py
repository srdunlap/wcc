# # # # # # # # # # #print(1 != 5) # Expected output: True
# # # # # # # # # # #print(1 == 2) # Expected output: False
# # # # # # # # # #
# # # # # # # # # # #print(1 > 2) # Expected output: False
# # # # # # # # # #
# # # # # # # # # # #print(2 > 1) # Expected output: True
# # # # # # # # # #
# # # # # # # # # # #print(1 >= 1) # Expected output: True
# # # # # # # # # #
# # # # # # # # # # print(2 == 2) # Expected output: True
# # # # # # # # # #
# # # # # # # # # # print(2 != 2) # Expected output: False
# # # # # # # # #
# # # # # # # # # age = 30
# # # # # # # # #
# # # # # # # # # print(age > 10) # Expected outcome: True
# # # # # # # # #
# # # # # # # # # print(10 < age) # Expected outcome: True
# # # # # # # # #
# # # # # # # # # print(age > 10 + 20) # Expected outcome: False
# # # # # # # # #
# # # # # # # # # print(age + 20 > 10) # Expected outcome: True
# # # # # # # # print('a' > 'z') # Expected outcome: False
# # # # # # # #
# # # # # # # # print('z' > 'a') # Expected outcome: True
# # # # # # # #
# # # # # # # # print('apples' > 'oranges') # Expected outcome: False
# # # # # # # #
# # # # # # # # print('oranges' > 'apples') # Expected outcome: True
# # # # # # # #
# # # # # # # # print('cat' > 'car') # Expected outcome: True
# # # # # # # #
# # # # # # # # print('car' > 'cat') # Expected outcome: False
# # # # # # # #
# # # # # # # print 'a' > 2 # Outcome: True
# # # # # # answer = int(raw_input('What is 1 + 1? '))
# # # # # # print(answer == 2)
# # # # # age = 1
# # # # # print(age > 12 and age < 19) # Expected outcome: False
# # # # #
# # # # # age = 14
# # # # # print(age > 12 and age < 19) # Expected outcome: True
# # # # #
# # # # # age = 19
# # # # # print(age > 12 and age < 19) # Expected outcome: False
# # # # #
# # # # # age = 18
# # # # # print(age > 12 and age < 19 and age != 5) # Expected outcome: True
# # # # #
# # # # # age = 5
# # # # # print(age > 12 and age < 19 and age != 5) # Expected outcome: False
# # # # #
# # # # # age = -1
# # # # # print(age > 12 and age < 19) # Expected outcome: False
# # # # #
# # # # # age = 10
# # # # # print(age > 25 and age < 15) # Expected outcome: False
# # # # # # Could the above expression ever be True? No
# # # # gesture = 'rock'
# # # # print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome:True
# # # #
# # # # gesture = 'pape'
# # # # print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: false (typo)
# # # gesture = 'rock'
# # # print(gesture == 'rock' and gesture == 'paper' or gesture == 'scissors')
# #
# #
# # age = int(raw_input('How old are you?'))
# # print(age > 4 and age < 11)
#
# age = int(raw_input('How old are you?'))
# print(11 > age > 4)

# age = int(raw_input('How old are you?'))
# print(age > 5 and age <10)


# age = int(raw_input('How old are you?'))
# print(5 < age < 10)



age = int(raw_input('How old are you?'))
print( 5 < age < 10)
#print(6 <= age <= 9)
