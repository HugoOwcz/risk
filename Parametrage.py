
import pyxel


class Parametrage:

    def __init__(self):
        pyxel.init(175, 100, fps=15)
        pyxel.load('new.pyxres')
        pyxel.mouse(True)
        self._selection1 = False
        self._nom_joueur1 = ''
        self._selection2 = False
        self._nom_joueur2 = ''
        self._mode = 'auto'
        self._info_finale = {}
        pyxel.run(self.update, self.draw)

    def update(self):
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
        pyxel.cls(0)
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
        if self._mode == 'auto':
            pyxel.blt(115, 49, 0, 0, 248, 8, 8, 0)
        else:
            pyxel.rect(115, 49, 8, 8, 7)
        pyxel.text(50, 60, ' - Manuel ', 5)
        if self._mode == 'manuel':
            pyxel.blt(115, 59, 0, 0, 248, 8, 8, 0)
        else:
            pyxel.rect(115, 59, 8, 8, 7)
        pyxel.rect(70, 80, 31, 10, 7)
        pyxel.text(72, 82, 'Valider', 5)

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
            self._mode = 'auto'
        elif 115 < pyxel.mouse_x < 123 and 59 < pyxel.mouse_y < 67:
            self._mode = 'manuel'

    def ajout_caractere(self, c):
        if self._selection1 and len(self._nom_joueur1) < 12:
            self._nom_joueur1 += c
        elif self._selection2 and len(self._nom_joueur1) < 12:
            self._nom_joueur2 += c

    def valider(self):
        self._info_finale = {'joueur1': self._nom_joueur1, 'joueur2': self._nom_joueur2, 'mode': self._mode}
        pyxel.quit()

    def get_info_finale(self):
        return self._info_finale
