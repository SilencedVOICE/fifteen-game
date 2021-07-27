from pygame.locals import *
import pygame
import time
import random


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
		pygame.draw.rect(screen, (241, 90, 36), (coordinates[serial - 1][0] + 1, coordinates[serial - 1][1] + 1, 98, 98), 0, 20)
		if serial < 10:
			serial_text = block_font.render(f"{serial}", True, (0, 0, 0))
			screen.blit(serial_text, (coordinates[serial - 1][0] + 38, coordinates[serial - 1][1] + 28))
		else:
			serial_text = block_font.render(f"{serial}", True, (0, 0, 0))
			screen.blit(serial_text, (coordinates[serial - 1][0] + 26, coordinates[serial - 1][1] + 28))
		status[serial - 1] = True
	else:
		pygame.draw.rect(screen, (0, 98, 255), (coordinates[serial - 1][0] + 1, coordinates[serial - 1][1] + 1, 98, 98), 0, 20)
		if serial < 10:
			serial_text = block_font.render(f"{serial}", True, (0, 0, 0))
			screen.blit(serial_text, (coordinates[serial - 1][0] + 38, coordinates[serial - 1][1] + 28))
		else:
			serial_text = block_font.render(f"{serial}", True, (0, 0, 0))
			screen.blit(serial_text, (coordinates[serial - 1][0] + 26, coordinates[serial - 1][1] + 28))
		status[serial - 1] = False


def UP():
	global coordinates
	blankY = coordinates[15][1]
	number = coordinates.index([coordinates[15][0], blankY + 100])
	coordinates = swap(coordinates, 15, number)


def LEFT():
	global coordinates
	blankX = coordinates[15][0]
	number = coordinates.index([blankX + 100, coordinates[15][1]])
	coordinates = swap(coordinates, 15, number)


def RIGHT():
	global coordinates
	blankX = coordinates[15][0]
	number = coordinates.index([blankX - 100, coordinates[15][1]])
	coordinates = swap(coordinates, 15, number)


def DOWN():
	global coordinates
	blankY = coordinates[15][1]
	number = coordinates.index([coordinates[15][0], blankY - 100])
	coordinates = swap(coordinates, 15, number)


pygame.init()
screen = pygame.display.set_mode((500, 600))
font = pygame.font.SysFont("Cooper Black", 40)
block_font = pygame.font.SysFont("Courier New", 40, bold=True)
compliment_font = pygame.font.SysFont("Cooper Black", 20)

end_rectangle = pygame.Surface((500, 600))
end_rectangle.set_alpha(224)
end_rectangle.fill((0, 0, 0))

solved = (
	[50, 50],
	[150, 50],
	[250, 50],
	[350, 50],
	[50, 150],
	[150, 150],
	[250, 150],
	[350, 150],
	[50, 250],
	[150, 250],
	[250, 250],
	[350, 250],
	[50, 350],
	[150, 350],
	[250, 350],
	[350, 350]
)
coordinates = list(solved)

functions = ["UP()", "LEFT()", "RIGHT()", "DOWN()", "UP()", "LEFT()", "RIGHT()", "DOWN()"]
random_pattern(200)
pattern = tuple(coordinates)

start_time = time.time()

number_of_moves = 0

status = []
for i in range(16):
	status.append(solved[i] == coordinates[i])

running = True
while running:
	screen.fill(0)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			if event.key == pygame.K_r:
				coordinates = list(pattern)
				number_of_moves = 0
				start_time = time.time()
			if event.key == pygame.K_n:
				random_pattern(200)
				pattern = tuple(coordinates)
				start_time = time.time()
			if (event.key == pygame.K_UP or event.key == pygame.K_w) and (coordinates[15][1] < 350) and not all(status):
				UP()
				number_of_moves += 1
			if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and (coordinates[15][0] < 350) and not all(status):
				LEFT()
				number_of_moves += 1
			if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and (coordinates[15][0] > 50) and not all(status):
				RIGHT()
				number_of_moves += 1
			if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and (coordinates[15][1] > 50) and not all(status):
				DOWN()
				number_of_moves += 1
		if event.type == pygame.MOUSEBUTTONDOWN:
			pass

	#qmark = font.render("?", True, (192, 192, 192))
	#screen.blit(qmark, (475, 0))

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
	time_text = font.render(f"{minutes}:{seconds}", True, (192, 192, 192))
	screen.blit(time_text, (317, 500))

	# number of moves
	moves_text = font.render(f"Moves: {number_of_moves}", True, (192, 192, 192))
	screen.blit(moves_text, (63, 500))

	if all(status):
		screen.blit(end_rectangle, (0, 0))

		gameover_text = font.render("Game Over", True, (255, 255, 255))
		screen.blit(gameover_text, (138, 50))

		congrats_text = compliment_font.render(f"Congratulations!", True, (255, 255, 255))
		screen.blit(congrats_text, (165, 150))

		compliment_text = compliment_font.render(f"You have successfully completed the game in", True, (255, 255, 255))
		screen.blit(compliment_text, (19, 180))

		elapsed_time_text = font.render(f"{minutes}:{seconds}", True, (255, 255, 255))
		screen.blit(elapsed_time_text, (196, 220))

		minutes_text = font.render(f"minutes", True, (255, 255, 255))
		screen.blit(minutes_text, (167, 270))

		number_of_moves_text = font.render(f"{number_of_moves}", True, (255, 255, 255))
		if number_of_moves < 10:
			screen.blit(number_of_moves_text, (238, 360))
		elif number_of_moves < 100:
			screen.blit(number_of_moves_text, (227, 360))
		elif number_of_moves < 1000:
			screen.blit(number_of_moves_text, (216, 360))
		else:
			screen.blit(number_of_moves_text, (205, 360))

		move_text = font.render("moves", True, (255, 255, 255))
		screen.blit(move_text, (185, 410))

		new_game_text = compliment_font.render("Press 'n' for new game", True, (255, 255, 255))
		screen. blit(new_game_text, (20, 560))

		reset_text = compliment_font.render("Press 'r' to reset", True, (255, 255, 255))
		screen.blit(reset_text, (315, 560))

	pygame.display.update()
