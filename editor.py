import pygame as pg


class Window:
	WIDTH = 800
	HEIGHT = 600
	SIZE = (WIDTH, HEIGHT)
	
	def __init__(self) -> None:

		# initialize pygame
		pg.init()

		self.window = pg.display.set_mode(self.SIZE)
		self.window.fill((64, 64, 64))
	
	def loop(self) -> None:
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					exit()
			pg.display.update()


if __name__ == "__main__":
	window = Window()
	window.loop()
