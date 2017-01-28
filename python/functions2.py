# def mystery(x, y, z):
#
#     return x + (y * z)# ??? Your code here
#
# # Test this function:
# print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
# print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'

def calculate_tip(price, rating):

    if rating == 'A':
        tip = .20;

    elif rating == 'B':
        tip = .18

    else:
        tip= .15

    return price * tip

print(calculate_tip(30.50, 'C'))
print(calculate_tip(15, 'B'))
print(calculate_tip(20, 'A'))
