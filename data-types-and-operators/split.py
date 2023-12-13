# 1. A basic split method:

new_str = "The cow jumped over the moon."
new_str.split()

# print(new_str.split())	

#['The', 'cow', 'jumped', 'over', 'the', 'moon.']




# 2. Here  the separator is space, and the maxsplit argument is set to 3.
new_str.split(' ', 3)
#print(new_str.split(' ', 3))

#['The', 'cow', 'jumped', 'over the moon.']



# 3. Using '.' or period as a separator.
new_str.split('.')
# print(new_str.split('.'))
['The cow jumped over the moon', '']


# 4. Using no separators but having a maxsplit argument of 3.
new_str.split(None, 3)

#print(new_str.split(None, 3))
['The', 'cow', 'jumped', 'over the moon.']



verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"

#print(len(verse))

#index = verse.find('and')
#print(index)

#last_index = verse.rfind('you')
#print(last_index)

count = verse.count('you')
print(count)