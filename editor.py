import pygame

class Window:
	def __init__(self) -> None:
		pygame.init()

		# redefintions
		self.DISPLAY = pygame.display
		self.SURFACE = pygame.surface.Surface
		self.CLOCK = pygame.time.Clock()
		self.FONT = pygame.font
		self.FREETYPE = pygame.freetype

		self.DISPLAY.set_caption("test")

		self.FPS = 60

		self.WIDTH = 800
		self.HEIGHT = 600
		self.SIZE = (self.WIDTH, self.HEIGHT)

		self.PADDING = 10
		self.PADDING2 = self.PADDING * 2

		self.main_window = self.DISPLAY.set_mode(self.SIZE, pygame.RESIZABLE)
		
		self.index_window_size = ((self.WIDTH + self.PADDING2) // 6, self.HEIGHT - self.PADDING2)
		self.index_window_position = (self.PADDING, self.PADDING)
		self.index_window = self.SURFACE((self.index_window_size))

		self.index_fontsize = 16
		self.indexes = [[i * 16, self.FREETYPE.SysFont("sans", self.index_fontsize)] for i in range(self.index_window_size[1] // self.index_fontsize)]

		print(len(self.indexes))

	def draw(self) -> None:
		self.main_window.fill( (  0,   0,   0))	# (  0,   0,   0) BLACK
		self.index_window.fill((255,   0,   0))	# (255,   0,   0) RED
		
		self.rendered_indexes = [(i[1].render("%.6X" % i[0]), (0, i[0] * 20)) for i in self.indexes]
		
		self.index_window.blits(blit_sequence=self.rendered_indexes, doreturn=1)
		
		self.main_window.blit(self.index_window, self.index_window_position)

	def resize(self, size) -> None:
		self.main_window = DISPLAY.set_mode(size, pygame.RESIZABLE)

	def quit(self) -> None:
		pygame.quit()
		self.run = False

	def loop(self) -> None:
		self.run = True
		while self.run:
			self.CLOCK.tick(self.FPS)

			self.draw()
			self.DISPLAY.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:

					# quit on ESC
					if event.key == pygame.K_ESCAPE:
						self.quit()

				if event.type == pygame.VIDEORESIZE:
					self.resize((event.w, event.h))

				# quit on termination
				if event.type == pygame.QUIT:
					self.quit()

def main() -> None:
	window = Window()
	window.loop()

if __name__ == "__main__":
	main()
