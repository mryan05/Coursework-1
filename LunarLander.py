#mryan05 Max Ryan

import math

#Prints the values of altitude, velocity and fuel
def print_values(altitude, velocity, fuel):
	print('Altitude is at ' + str(altitude))
	print('Velocity is at ' + str(velocity))
	print('Fuel is at ' + str(fuel))
	

#Main logic of the game
def game():
	altitude = 1000.0
	velocity = 0.0
	fuel = 1000.0
	CONSTANT = 0.15
	turn = 1
	while altitude >= 0:
		if turn == 1:
			burn = 0
			print_values(altitude, velocity, fuel)
			print("")
		else:
			print_values(altitude, velocity, fuel)
			print('How much fuel will you use?: ')
			burn = int(input()) 
		if burn > fuel:
			burn = fuel
			fuel = 0
		elif burn < 0:
			burn = 0
		else:
			fuel -= burn
		velocity += 1.6
		velocity -= CONSTANT * burn
		altitude -= velocity
		turn += 1
	if velocity <= 10:
		altitude = 0
		print_values(altitude, velocity, fuel)
		print('You have landed succesfully!')
		play_again()
	else:
		print('You have crashed, you have created a crater ' + (str(math.fabs(altitude)) + ' metres deep in the lunar surface.'))
		play_again()

# Options for when game has ended
def play_again(): 	
	play = True
	while play:
		print('Would you like to play again?: ')
		s = input()
		if s[0] == 'y' or s[0] == 'Y':
			game()
		elif s[0] == 'n' or s[0] == 'N':
			play = False
		else:
			play = True
						
game()

