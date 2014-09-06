from PIL import Image

class Drawer():

    def __init__(self, h, mx, my):
        self.h = h
        self.mx = mx
        self.my = my
        self.imgx = self.mx * self.h
        self.imgy = self.my * self.h
        self.perx = self.imgx / self.mx
        self.pery = self.imgy / self.my

    def is_enter(self, kx, ky):
        return ky == 0 and kx < self.h

    def is_exit(self, kx, ky):
        return ky == self.imgy-1 and kx > (self.mx - 1) * self.h

    def prepare(self, maze):
        image = Image.new("RGB", (self.imgx, self.imgy))
        pixels = image.load()
        color = [(0, 0, 0), (255, 255, 255)]  # RGB colors of the maze

        for ky in range(self.imgy):
            for kx in range(self.imgx):
                pixels[kx, ky] = color[1]

                if not self.is_enter(kx,ky) and not self.is_exit(kx,ky) and (kx == 0 or kx == self.imgx - 1 or ky == 0 or ky == self.imgy - 1):
                    pixels[kx, ky] = color[0]
                else:
                    if kx % self.perx == 0:
                        index = (kx / self.perx) + (ky / self.pery) * self.mx
                        if index >= 1 and index - 1 < self.mx * self.my and maze[index][index - 1] == 0:
                            pixels[kx, ky] = color[0]
                    if ky % self.pery == 0:
                        index = (kx / self.perx) + (ky / self.pery) * self.mx
                        if index >= self.mx and maze[index][index - self.mx] == 0:
                            pixels[kx, ky] = color[0]
        return image

    def draw(self, maze):
        image = self.prepare(maze)
        image.save("Maze_" + str(self.mx) + "x" + str(self.my) + ".png", "PNG")
