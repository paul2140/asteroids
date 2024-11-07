# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	dt = 0
	asteroidfield = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for obj in updatable:
			obj.update(dt)
		for obj in asteroids:
			if obj.collided(player):
				sys.exit("Game over!")
			for item in shots:
				if obj.collided(item):
					item.kill()
					obj.split()

		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
		main()
