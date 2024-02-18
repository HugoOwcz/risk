
from Plateau import *
from Joueur import *
from Parametrage import *


class Jeu(Parametrage):

    def __init__(self):
        Parametrage.__init__(self)
        self._info = self.get_info_finale()
        print(self._info, self.get_info_finale())
        self._plateau = Plateau()
        self._joueur1 = None
        self._joueur2 = None

    def initialisation(self):
        pass


j = Jeu()
