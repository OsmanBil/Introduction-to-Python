points = 174  # use this input to make your submission

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"
#print(result)
###########################################################################    


# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.

answer = 25 #provide answer
guess = 50 #provide guess

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
else:
    result = "Nice!  Your guess matched the answer!"

#print(result)
###########################################################################

state = "CA" #Either "CA", "MN", or "NY"
purchase_amount = 109 #amount of purchase

if state == "CA": #provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN": #provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY": #provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

#print(result)

###########################################################################

points = 174
prize = None

if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"


if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)