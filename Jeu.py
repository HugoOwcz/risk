
import random
from Plateau import *
from Joueur import *


class Jeu:

    def __init__(self):
        self._plateau = Plateau()
        self._joueur1 = None
        self._joueur2 = None
        self._mode = None

    def parametrage(self, nom_joueur1, nom_joueur2, mode):
        self._joueur1 = Joueur(nom_joueur1, 24)
        self._joueur2 = Joueur(nom_joueur2, 24)
        self._mode = mode
        self.choix_regions()

    def choix_regions(self):
        if self._mode == 'manuel':
            pass
        elif self._mode == 'auto':
            nombre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
            nombre_joueur1 = []
            nombre_joueur2 = []
            for i in range(len(nombre)):
                tmp = random.randint(0, len(nombre)-1)
                if i % 2 == 0:
                    nombre_joueur1.append(nombre.pop(tmp))
                else:
                    nombre_joueur2.append(nombre.pop(tmp))
            nb_armee = True
            for i in nombre_joueur1:
                cpt = 0
                for x in range(self._plateau.get_taille()['x']):
                    for y in range(self._plateau.get_taille()['y']):
                        if isinstance(self._plateau.get_plateau()[x][y], Region):
                            cpt += 1
                        if cpt == i:
                            self._plateau.get_plateau()[x][y].set_proprietaire(self._joueur1.get_nom())
                            if nb_armee:
                                self._plateau.get_plateau()[x][y].set_nb_armee(2)
                            else:
                                self._plateau.get_plateau()[x][y].set_nb_armee(1)
                            nb_armee = not nb_armee
                            cpt += 100
            for i in nombre_joueur2:
                cpt = 0
                for x in range(self._plateau.get_taille()['x']):
                    for y in range(self._plateau.get_taille()['y']):
                        if isinstance(self._plateau.get_plateau()[x][y], Region):
                            cpt += 1
                        if cpt == i:
                            self._plateau.get_plateau()[x][y].set_proprietaire(self._joueur2.get_nom())
                            if nb_armee:
                                self._plateau.get_plateau()[x][y].set_nb_armee(2)
                            else:
                                self._plateau.get_plateau()[x][y].set_nb_armee(1)
                            nb_armee = not nb_armee
                            cpt += 100

    def gagne(self):
        if self._joueur1.get_nb_regions() == self._plateau.get_nb_regions():
            return True, self._joueur1.get_nom()
        elif self._joueur2.get_nb_regions() == self._plateau.get_nb_regions():
            return True, self._joueur2.get_nom()
        return False, None
