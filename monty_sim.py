
from random import randint 

def monty_hall():
	count_win = 0 
	trials = 1000000
	for x in range(trials):
		doors = [0, 0, 0]
		# win is the winning door 
		win = randint(0, 2)
		doors[win] = 1 
		chosen = randint(0, 2)
		# print l

		rev = reveal_door(doors, win, chosen)
		final = switch(chosen, rev) 

		if final == win:
			count_win += 1
	print count_win / float(trials)


def reveal_door(doors, win, chosen):
	door_reveal = -1 
	if doors[chosen] == 1:
		indices = [0, 1, 2]
		indices.remove(chosen)
		reveal = indices[randint(0,1)]
		door_reveal = reveal 
	else:
		indices = [0, 1, 2]
		indices.remove(chosen)
		indices.remove(win)
		reveal = indices[0]
		door_reveal = reveal 
	return door_reveal

def switch(chosen, door_reveal):
    new_indices = [0, 1, 2]
    new_indices.remove(chosen)
    new_indices.remove(door_reveal)
    return new_indices[0]

monty_hall()















