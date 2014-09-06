from drawer import Drawer
from PIL import ImageDraw

class Solver():

	color = (255, 0, 0)

	def __init__(self, h, mx, my):
		self.h = h
		self.mx = mx
		self.my = my
		self.imgx = self.mx * self.h
		self.imgy = self.my * self.h

	def sign(self, a):
		return 1 if a else -1

	def draw(self, maze, solution):

		drawer = Drawer(self.h, self.mx, self.my)
		image = drawer.prepare(maze)
		pixels = image.load()
		draw = ImageDraw.Draw(image) 

		prev = None

		for step in [(0,-1)] + solution + [(self.mx - 1, self.my)]:
			if prev:
				kx1 = prev[0] * self.h + self.h / 2
				ky1 = prev[1] * self.h + self.h / 2
				kx2 = step[0] * self.h + self.h / 2
				ky2 = step[1] * self.h + self.h / 2				
				draw.line((kx1, ky1, kx2, ky2), fill="red")				
			prev = step
		image.save("SolvedMaze_" + str(self.mx) + "x" + str(self.my) + ".png", "PNG")
			