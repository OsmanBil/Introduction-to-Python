# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8  # 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6 # 5e6 is equal to 5 * 10 ** 6 which is equal to 5000000.0


# Use the multiplication assignment operator to decrease 
# the rainfall variable by 10% to account for runoff

rainfall *= 0.9

###########################

# Use the addition assigment operator to add 
# the rainfall variable to the reservoir_volume variable

reservoir_volume += rainfall

###########################

# Use the multiplication assignment operator to increase 
# reservoir_volume by 5% to account for stormwater that 
# flows into the reservoir in the days following the storm

reservoir_volume *= 1.05

###########################

# Use the multiplication assignment operator to decrease 
# reservoir_volume by 5% to account for evaporation

reservoir_volume *= 0.95

###########################

# Use the subtraction assignment operator to subtract 
# 2.5e5 cubic metres from reservoir_volume to account 
# for water that's piped to arid regions.

reservoir_volume -= 2.5e5 