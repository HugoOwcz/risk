
import pyxel
from Jeu import *


class Affichage(Jeu):

    def __init__(self):
        Jeu.__init__(self)
        pyxel.init(175, 100, fps=10)
        pyxel.load('new.pyxres')
        pyxel.mouse(True)
        self._parametrage = True
        self._selection1 = False
        self._nom_joueur1 = ''
        self._selection2 = False
        self._nom_joueur2 = ''
        self._choix_mode = 'auto'
        pyxel.run(self.update, self.draw)

    def update(self):
        if self._parametrage:
            self.update_parametrage()

    def update_parametrage(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.mouse_y < 40:
                self.modification_selection()
            elif 40 < pyxel.mouse_y < 70:
                self.modification_mode()
            elif 69 < pyxel.mouse_x < 102 and 79 < pyxel.mouse_y < 91:
                self.valider()
        if pyxel.btn(pyxel.KEY_A):
            self.ajout_caractere('a')
        elif pyxel.btn(pyxel.KEY_B):
            self.ajout_caractere('b')
        elif pyxel.btn(pyxel.KEY_C):
            self.ajout_caractere('c')
        elif pyxel.btn(pyxel.KEY_D):
            self.ajout_caractere('d')
        elif pyxel.btn(pyxel.KEY_E):
            self.ajout_caractere('e')
        elif pyxel.btn(pyxel.KEY_F):
            self.ajout_caractere('f')
        elif pyxel.btn(pyxel.KEY_G):
            self.ajout_caractere('g')
        elif pyxel.btn(pyxel.KEY_H):
            self.ajout_caractere('h')
        elif pyxel.btn(pyxel.KEY_I):
            self.ajout_caractere('i')
        elif pyxel.btn(pyxel.KEY_J):
            self.ajout_caractere('j')
        elif pyxel.btn(pyxel.KEY_K):
            self.ajout_caractere('k')
        elif pyxel.btn(pyxel.KEY_L):
            self.ajout_caractere('l')
        elif pyxel.btn(pyxel.KEY_M):
            self.ajout_caractere('m')
        elif pyxel.btn(pyxel.KEY_N):
            self.ajout_caractere('n')
        elif pyxel.btn(pyxel.KEY_O):
            self.ajout_caractere('o')
        elif pyxel.btn(pyxel.KEY_P):
            self.ajout_caractere('p')
        elif pyxel.btn(pyxel.KEY_Q):
            self.ajout_caractere('q')
        elif pyxel.btn(pyxel.KEY_R):
            self.ajout_caractere('r')
        elif pyxel.btn(pyxel.KEY_S):
            self.ajout_caractere('s')
        elif pyxel.btn(pyxel.KEY_T):
            self.ajout_caractere('t')
        elif pyxel.btn(pyxel.KEY_U):
            self.ajout_caractere('u')
        elif pyxel.btn(pyxel.KEY_V):
            self.ajout_caractere('v')
        elif pyxel.btn(pyxel.KEY_W):
            self.ajout_caractere('w')
        elif pyxel.btn(pyxel.KEY_X):
            self.ajout_caractere('x')
        elif pyxel.btn(pyxel.KEY_Y):
            self.ajout_caractere('y')
        elif pyxel.btn(pyxel.KEY_Z):
            self.ajout_caractere('z')
        elif pyxel.btn(pyxel.KEY_SPACE):
            self.ajout_caractere(' ')
        elif pyxel.btn(pyxel.KEY_BACKSPACE):
            if self._selection1:
                self._nom_joueur1 = self._nom_joueur1[:-1]
            elif self._selection2:
                self._nom_joueur2 = self._nom_joueur2[:-1]

    def draw(self):
        if self._parametrage:
            self.draw_parametrage()
        else:
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
                            elif isinstance(plateau[x-1][y], Chemin) and (plateau[x-1][y].get_direction() == 'horizontal' or (plateau[x-1][y].get_direction() == 'croisement' and 'S' in plateau[x-1][y].get_complement())):
                                voisin['N'] = 'C'
                        if x < self._plateau.get_taille()['x']-1:
                            if isinstance(plateau[x+1][y], Region):
                                voisin['S'] = 'R'
                            elif isinstance(plateau[x+1][y], Chemin) and (plateau[x+1][y].get_direction() == 'horizontal' or (plateau[x+1][y].get_direction() == 'croisement' and 'N' in plateau[x+1][y].get_complement())):
                                voisin['S'] = 'C'
                        if y > 0:
                            if isinstance(plateau[x][y-1], Region):
                                voisin['O'] = 'R'
                            elif isinstance(plateau[x][y-1], Chemin) and (plateau[x][y-1].get_direction() == 'horizontal' or (plateau[x][y-1].get_direction() == 'croisement' and 'E' in plateau[x][y-1].get_complement())):
                                voisin['O'] = 'C'
                        if y < self._plateau.get_taille()['y']-1:
                            if isinstance(plateau[x][y+1], Region):
                                voisin['E'] = 'R'
                            elif isinstance(plateau[x][y+1], Chemin) and (plateau[x][y+1].get_direction() == 'horizontal' or (plateau[x][y+1].get_direction() == 'croisement' and 'O' in plateau[x][y+1].get_complement())):
                                voisin['E'] = 'C'
                        if element.get_proprietaire() == self._joueur1.get_nom():
                            self.draw_region(x, y, voisin, 8)
                        elif element.get_proprietaire() == self._joueur2.get_nom():
                            self.draw_region(x, y, voisin, 16)
                        else:
                            self.draw_region(x, y, voisin)

    def draw_parametrage(self):
        pyxel.cls(0)
        pyxel.text(10, 1, 'Les noms des 2 joueurs doivent etre !=.', 5)
        pyxel.text(10, 10, 'Nom du premier joueur : ', 5)
        pyxel.rectb(110, 7, 51, 10, 7)
        if self._selection1:
            pyxel.rect(111, 8, 49, 8, 13)
        pyxel.text(112, 9, self._nom_joueur1.upper(), 5)
        pyxel.text(10, 22, 'Nom du deuxième joueur : ', 5)
        pyxel.rectb(110, 19, 51, 10, 7)
        if self._selection2:
            pyxel.rect(111, 20, 49, 8, 13)
        pyxel.text(112, 21, self._nom_joueur2.upper(), 5)
        pyxel.text(10, 40, 'Choix des regions :', 5)
        pyxel.text(50, 50, ' - Automatique ', 5)
        if self._choix_mode == 'auto':
            pyxel.blt(115, 49, 0, 0, 248, 8, 8, 0)
        else:
            pyxel.rect(115, 49, 8, 8, 7)
        pyxel.text(50, 60, ' - Manuel ', 5)
        if self._choix_mode == 'manuel':
            pyxel.blt(115, 59, 0, 0, 248, 8, 8, 0)
        else:
            pyxel.rect(115, 59, 8, 8, 7)
        pyxel.rect(70, 80, 31, 10, 7)
        pyxel.text(72, 82, 'Valider', 5)

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

    def modification_selection(self):
        if 110 < pyxel.mouse_x < 161 and 7 < pyxel.mouse_y < 17:
            self._selection1 = True
            self._selection2 = False
        elif 110 < pyxel.mouse_x < 161 and 19 < pyxel.mouse_y < 29:
            self._selection1 = False
            self._selection2 = True
        else:
            self._selection1 = False
            self._selection2 = False

    def modification_mode(self):
        if 115 < pyxel.mouse_x < 123 and 49 < pyxel.mouse_y < 57:
            self._choix_mode = 'auto'
        elif 115 < pyxel.mouse_x < 123 and 59 < pyxel.mouse_y < 67:
            self._choix_mode = 'manuel'

    def ajout_caractere(self, c):
        if self._selection1 and len(self._nom_joueur1) < 12:
            self._nom_joueur1 += c
        elif self._selection2 and len(self._nom_joueur1) < 12:
            self._nom_joueur2 += c

    def valider(self):
        if self._nom_joueur1 != self._nom_joueur2:
            self._parametrage = False
            pyxel.width = 96
            pyxel.height = 56
            self.parametrage(self._nom_joueur1, self._nom_joueur2, self._choix_mode)


a = Affichage()
