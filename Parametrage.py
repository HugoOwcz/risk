
import pyxel


class Parametrage:

    def __init__(self):
        pyxel.init(100, 100)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, 'TMP', 5)


p = Parametrage()
