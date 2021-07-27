# IMPORTING REQUIRED MODULES
from pygame.draw import rect
from pygame.mouse import get_pos
import pygame
import time
import random


# DEFINING FUNCTIONS
def swap(array, first, second):
	x = array[first]
	array[first] = array[second]
	array[second] = x
	return array


def random_pattern(k):
	for n in range(k):
		try:
			exec(random.choice(functions))
		except ValueError:
			continue


def block(serial):
	global coordinates
	if coordinates[serial - 1] == solved[serial - 1]:
		rect(screen, (241, 90, 36), (coordinates[serial - 1][0] + 3, coordinates[serial - 1][1] + 3, 294, 294), 0, 60)
		if serial < 10:
			serial_text = block_font.render(f"{serial}", True, (0, 0, 0))
			screen.blit(serial_text, (coordinates[serial - 1][0] + 114, coordinates[serial - 1][1] + 84))
		else:
			serial_text = block_font.render(f"{serial}", True, (0, 0, 0))
			screen.blit(serial_text, (coordinates[serial - 1][0] + 78, coordinates[serial - 1][1] + 84))
		status[serial - 1] = True
	else:
		rect(screen, (0, 98, 255), (coordinates[serial - 1][0] + 3, coordinates[serial - 1][1] + 3, 294, 294), 0, 60)
		if serial < 10:
			serial_text = block_font.render(f"{serial}", True, (0, 0, 0))
			screen.blit(serial_text, (coordinates[serial - 1][0] + 114, coordinates[serial - 1][1] + 84))
		else:
			serial_text = block_font.render(f"{serial}", True, (0, 0, 0))
			screen.blit(serial_text, (coordinates[serial - 1][0] + 78, coordinates[serial - 1][1] + 84))
		status[serial - 1] = False


def UP():
	global coordinates
	blankY = coordinates[15][1]
	number = coordinates.index([coordinates[15][0], blankY + 300])
	coordinates = swap(coordinates, 15, number)


def LEFT():
	global coordinates
	blankX = coordinates[15][0]
	number = coordinates.index([blankX + 300, coordinates[15][1]])
	coordinates = swap(coordinates, 15, number)


def RIGHT():
	global coordinates
	blankX = coordinates[15][0]
	number = coordinates.index([blankX - 300, coordinates[15][1]])
	coordinates = swap(coordinates, 15, number)


def DOWN():
	global coordinates
	blankY = coordinates[15][1]
	number = coordinates.index([coordinates[15][0], blankY - 300])
	coordinates = swap(coordinates, 15, number)


# main
pygame.init()
screen = pygame.display.set_mode((1500, 2100), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption("Fifteen")

# declaring fonts
font = pygame.font.SysFont("Cooper Black", 120)
block_font = pygame.font.SysFont("Courier New", 120, bold=True)
button_font = pygame.font.SysFont("Cooper Black", 90)
compliment_font = pygame.font.SysFont("Cooper Black", 60)
#cross_font = pygame.font.SysFont("Kalpurush", 90)

# transparent end screen
end_rectangle = pygame.Surface((1500, 1800))
end_rectangle.set_alpha(224)
end_rectangle.fill((0, 0, 0))

# info square
info_square = pygame.Surface((125, 125))
info_square.set_alpha(255)
info_square.fill((128, 16, 16))

# new game button
new_game_rectangle = pygame.Surface((700, 200))
new_game_rectangle.set_alpha(255)
new_game_rectangle.fill((16, 128, 48))

# reset button
reset_rectangle = pygame.Surface((700, 200))
reset_rectangle.set_alpha(255)
reset_rectangle.fill((16, 64, 128))

# declaring pattern related variables
solved = (
	[150, 150],
	[450, 150],
	[750, 150],
	[1050, 150],
	[150, 450],
	[450, 450],
	[750, 450],
	[1050, 450],
	[150, 750],
	[450, 750],
	[750, 750],
	[1050, 750],
	[150, 1050],
	[450, 1050],
	[750, 1050],
	[1050, 1050]
)
coordinates = list(solved)

# function list
functions = ["UP()", "LEFT()", "RIGHT()", "DOWN()"]

# rendering random pattern
random_pattern(200)
pattern = tuple(coordinates)

# declaring start time
start_time = time.time()

# declaring number of moves
number_of_moves = 0

status = []
for i in range(16):
	status.append(solved[i] == coordinates[i])

start_mouse_pos = 0
end_mouse_pos = 0

# game loop
running = True
while running:

	# background color
	screen.fill(0)

	# reading events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			if event.key == pygame.K_AC_BACK:
				running = False
			if event.key == pygame.K_r:
				coordinates = list(pattern)
				number_of_moves = 0
				start_time = time.time()
			if event.key == pygame.K_n:
				random_pattern(200)
				number_of_moves = 0
				pattern = tuple(coordinates)
				start_time = time.time()
		if event.type == pygame.MOUSEBUTTONDOWN:
			#start_mouse_pos = pygame.mouse.get_pos()
			if not all(status):
				if (coordinates[15][0] < get_pos()[0] < coordinates[15][0] + 300) and (coordinates[15][1] + 300 < get_pos()[1] < coordinates[15][1] + 600) and (coordinates[15][1] < 1050):
					UP()
					number_of_moves += 1
				if (coordinates[15][0] + 300 < get_pos()[0] < coordinates[15][0] + 600) and (coordinates[15][1] < get_pos()[1] < coordinates[15][1] + 300) and (coordinates[15][0] < 1050):
					LEFT()
					number_of_moves += 1
				if (coordinates[15][0] - 300 < pygame.mouse.get_pos()[0] < coordinates[15][0]) and (coordinates[15][1] < pygame.mouse.get_pos()[1] < coordinates[15][1] + 300) and (coordinates[15][0] > 150):
					RIGHT()
					number_of_moves += 1
				if (coordinates[15][0] < pygame.mouse.get_pos()[0] < coordinates[15][0] + 300) and (coordinates[15][1] - 300 < pygame.mouse.get_pos()[1] < coordinates[15][1]) and (coordinates[15][1] > 150):
					DOWN()
					number_of_moves += 1
			if (25 < pygame.mouse.get_pos()[0] < 725) and (1850 < pygame.mouse.get_pos()[1] < 2050):
				new_game_rectangle.fill((0, 224, 64))
			if (775 < pygame.mouse.get_pos()[0] < 1475) and (1850 < pygame.mouse.get_pos()[1] < 2050):
				reset_rectangle.fill((0, 80, 224))
			#if (1375 < pygame.mouse.get_pos()[0] < 1500) and (0 < pygame.mouse.get_pos()[1] < 125):
			#	info_square.fill((224, 16, 16))
		if event.type == pygame.MOUSEBUTTONUP:
			#end_mouse_pos = pygame.mouse.get_pos()
			new_game_rectangle.fill((16, 128, 48))
			reset_rectangle.fill((16, 64, 128))
			#info_square.fill((128, 16, 16))
			if (25 < pygame.mouse.get_pos()[0] < 725) and (1850 < pygame.mouse.get_pos()[1] < 2050):
				random_pattern(200)
				number_of_moves = 0
				pattern = tuple(coordinates)
				start_time = time.time()
			if (775 < pygame.mouse.get_pos()[0] < 1475) and (1850 < pygame.mouse.get_pos()[1] < 2050):
				coordinates = list(pattern)
				number_of_moves = 0
				start_time = time.time()
			#if (1375 < pygame.mouse.get_pos()[0] < 1500) and (0 < pygame.mouse.get_pos()[1] < 125):
			#	pass

			#if (abs(start_mouse_pos[0] - end_mouse_pos[0]) > 300) and (150 < start_mouse_pos[0] and start_mouse_pos[1] and end_mouse_pos[0] and end_mouse_pos[1] < 1350):
			#	if abs(start_mouse_pos[0] - end_mouse_pos[0]) > abs(start_mouse_pos[1] - end_mouse_pos[1]):
			#		if start_mouse_pos[0] - end_mouse_pos[0] > 0:
			#			LEFT()
			#		if (coordinates[15][0] > 150):
			#			RIGHT()
			#	if abs(start_mouse_pos[0] - end_mouse_pos[0]) < abs(start_mouse_pos[1] - end_mouse_pos[1]):
			#		if start_mouse_pos[1] - end_mouse_pos[1] > 0:
			#			DOWN()
			#		else:
			#			UP()

	#screen.blit(info_square, (1375, 0))
	#qMark = button_font.render("?", True, (255, 255, 255))
	#crossMark = cross_font.render("x", True, (255, 255, 255))
	#screen.blit(crossMark, (1416, 9))

	# BLOCK 1
	block(1)

	# BLOCK 2
	block(2)

	# BLOCK 3
	block(3)

	# BLOCK 4
	block(4)

	# BLOCK 5
	block(5)

	# BLOCK 6
	block(6)

	# BLOCK 7
	block(7)

	# BLOCK 8
	block(8)

	# BLOCK 9
	block(9)

	# BLOCK 10
	block(10)

	# BLOCK 11
	block(11)

	# BLOCK 12
	block(12)

	# BLOCK 13
	block(13)

	# BLOCK 14
	block(14)

	# BLOCK 15
	block(15)

	# BLANK BLOCK
	if coordinates[15] == solved[15]:
		status[15] = True
	else:
		status[15] = False

	# elapsed time
	if not all(status):
		present_time = time.time()
	else:
		present_time = present_time

	seconds = int((present_time - start_time) % 60)
	minutes = int((present_time - start_time) // 60)

	# for correct time rendering
	if len(f"{seconds}") != 2 and len(f"{minutes}") != 2:
		minutes = f"0{minutes}"
		seconds = f"0{seconds}"
	elif len(f"{seconds}") != 2 and len(f"{minutes}") == 2:
		minutes = f"{minutes}"
		seconds = f"0{seconds}"
	elif len(f"{seconds}") == 2 and len(f"{minutes}") != 2:
		minutes = f"0{minutes}"
		seconds = f"{seconds}"
	else:
		minutes = f"{minutes}"
		seconds = f"{seconds}"

	# time
	time_text = font.render(f"{minutes}:{seconds}", True, (192, 192, 192))
	screen.blit(time_text, (951, 1500))

	# number of moves
	moves_text = font.render(f"Moves: {number_of_moves}", True, (192, 192, 192))
	screen.blit(moves_text, (189, 1500))

	# new game button
	screen.blit(new_game_rectangle, (25, 1850))
	new_game_block_text = button_font.render("New Game", True, (255, 255, 255))
	screen.blit(new_game_block_text, (130, 1900))

	# reset button
	screen.blit(reset_rectangle, (775, 1850))
	reset_block_text = button_font.render("Reset", True, (255, 255, 255))
	screen.blit(reset_block_text, (1000, 1900))

	# end loop
	if all(status):
		screen.blit(end_rectangle, (0, 0))

		gameover_text = font.render("Game Over", True, (255, 255, 255))
		screen.blit(gameover_text, (414, 150))

		congrats_text = compliment_font.render(f"Congratulations!", True, (255, 255, 255))
		screen.blit(congrats_text, (495, 450))

		compliment_text = compliment_font.render(f"You have successfully completed the game in", True, (255, 255, 255))
		screen.blit(compliment_text, (57, 540))

		elapsed_time_text = font.render(f"{minutes}:{seconds}", True, (255, 255, 255))
		screen.blit(elapsed_time_text, (588, 660))

		minutes_text = font.render(f"minutes", True, (255, 255, 255))
		screen.blit(minutes_text, (501, 810))

		number_of_moves_text = font.render(f"{number_of_moves}", True, (255, 255, 255))
		if number_of_moves < 10:
			screen.blit(number_of_moves_text, (714, 1080))
		elif number_of_moves < 100:
			screen.blit(number_of_moves_text, (681, 1080))
		elif number_of_moves < 1000:
			screen.blit(number_of_moves_text, (648, 1080))
		else:
			screen.blit(number_of_moves_text, (615, 1080))

		move_text = font.render("moves", True, (255, 255, 255))
		screen.blit(move_text, (555, 1230))

	# updating display in every iterations
	pygame.display.update()
