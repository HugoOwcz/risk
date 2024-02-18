
class Joueur:

    def __init__(self, nom, nb_armee):
        self._nom = nom
        self._nb_armee = nb_armee
        self._nb_regions = 0
        self._liste_regions = []
        self._liste_zone_controle = []

    def get_nom(self):
        return self._nom

    def get_nb_armee(self):
        return self._nb_armee

    def modification_armee(self, nb):
        self._nb_armee += nb

    def get_nb_regions(self):
        return self._nb_regions

    def modification_nb_regions(self, nb):
        self._nb_regions += nb

    def get_liste_regions(self):
        return self._liste_regions

    def ajout_regions(self, region):
        self._liste_regions.append(region)

    def suppression_regions(self, numero):
        self._liste_regions.pop(numero)

    def get_liste_zones(self):
        return self._liste_zone_controle

    def ajout_zones(self, region):
        self._liste_zone_controle.append(region)

    def suppression_zones(self, numero):
        self._liste_zone_controle.pop(numero)
