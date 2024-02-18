
import pyxel
from Plateau import *


class Affichage:

    def __init__(self):
        self._plateau = Plateau()
        pyxel.init(12*8, 7*8)
        pyxel.load('new.pyxres')
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            print('x : ', pyxel.mouse_x, 'y :', pyxel.mouse_y)

    def draw(self):
        pyxel.cls(1)
        plateau = self._plateau.get_plateau()
        for x in range(self._plateau.get_taille()['x']):
            for y in range(self._plateau.get_taille()['y']):
                element = plateau[x][y]
                if isinstance(element, Chemin):
                    self.draw_chemin(element, x, y)
                if isinstance(element, Region):
                    voisin = {'N': None, 'S': None, 'E': None, 'O': None}
                    if x > 0:
                        if isinstance(plateau[x-1][y], Region):
                            voisin['N'] = 'R'
                        elif isinstance(plateau[x-1][y], Chemin):
                            voisin['N'] = 'C'
                    if x < self._plateau.get_taille()['x']-1:
                        if isinstance(plateau[x+1][y], Region):
                            voisin['S'] = 'R'
                        elif isinstance(plateau[x+1][y], Chemin):
                            voisin['S'] = 'C'
                    if y > 0:
                        if isinstance(plateau[x][y-1], Region):
                            voisin['O'] = 'R'
                        elif isinstance(plateau[x][y-1], Chemin):
                            voisin['O'] = 'C'
                    if y < self._plateau.get_taille()['y']-1:
                        if isinstance(plateau[x][y+1], Region):
                            voisin['E'] = 'R'
                        elif isinstance(plateau[x][y+1], Chemin):
                            voisin['E'] = 'C'
                    if element.get_proprietaire() == 1:
                        self.draw_region(x, y, voisin, 8)
                    elif element.get_proprietaire() == 2:
                        self.draw_region(x, y, voisin, 16)
                    else:
                        self.draw_region(x, y, voisin)

    def draw_chemin(self, element, x, y):
        match element.get_direction():
            case 'vertical':
                pyxel.blt(y * 8, x * 8, 0, 0, 0, 8, 8, 0)
            case 'horizontal':
                pyxel.blt(y * 8, x * 8, 0, 0, 8, 8, 8, 0)
            case 'croisement':
                match element.get_complement():
                    case 'SO':
                        pyxel.blt(y * 8, x * 8, 0, 0, 16, 8, 8, 0)
                    case 'NE':
                        pyxel.blt(y * 8, x * 8, 0, 0, 24, 8, 8, 0)
                    case 'SE':
                        pyxel.blt(y * 8, x * 8, 0, 0, 32, 8, 8, 0)
                    case 'NO':
                        pyxel.blt(y * 8, x * 8, 0, 0, 40, 8, 8, 0)
                    case 'NOE':
                        pyxel.blt(y * 8, x * 8, 0, 0, 48, 8, 8, 0)
                    case 'SOE':
                        pyxel.blt(y * 8, x * 8, 0, 0, 56, 8, 8, 0)
                    case 'NSE':
                        pyxel.blt(y * 8, x * 8, 0, 0, 64, 8, 8, 0)
                    case 'NSO':
                        pyxel.blt(y * 8, x * 8, 0, 0, 72, 8, 8, 0)
                    case 'NSOE':
                        pyxel.blt(y * 8, x * 8, 0, 0, 80, 8, 8, 0)

    def draw_region(self, x, y, voisin, joueur=0):
        n, s, e, o = voisin.values()
        match n:
            case None:
                match s:
                    case None:
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 0, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 136, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 24, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 88, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 80, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 112, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 32, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 224, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 48, 8, 8, 0)
                    case 'R':
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 0, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 200, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 16, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 168, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 16, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 184, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 24, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 216, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 232, 8, 8, 0)
                    case 'C':
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 8, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 144, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 72, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 96, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 96, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 128, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 80, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 168, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 232, 8, 8, 0)
            case 'R':
                match s:
                    case None:
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 176, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 136, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 192, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 112, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 48, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 128, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 200, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 152, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 240, 8, 8, 0)
                    case 'R':
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 48, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 32, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 56, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 0, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 64, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 8, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 64, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 40, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 72, 8, 8, 0)
                    case 'C':
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 164, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 144, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 248, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 120, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 56, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 240, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 208, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 160, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 248, 8, 8, 0)
            case 'C':
                match s:
                    case None:
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 16, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 152, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 56, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 104, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 88, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 120, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 64, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 160, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 72, 8, 8, 0)
                    case 'R':
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 8, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 208, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 40, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 176, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 24, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 192, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 40, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 224, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 80, 8, 8, 0)
                    case 'C':
                        match e:
                            case None:
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 8+joueur, 40, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 88, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 96, 8, 8, 0)
                            case 'R':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 104, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 32+joueur, 104, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 112, 8, 8, 0)
                            case 'C':
                                match o:
                                    case None:
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 120, 8, 8, 0)
                                    case 'R':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 136, 8, 8, 0)
                                    case 'C':
                                        pyxel.blt(y * 8, x * 8, 0, 56+joueur, 128, 8, 8, 0)


a = Affichage()
