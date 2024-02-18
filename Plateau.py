

class Plateau:
    def __init__(self):
        self._taille = {'x': 7, 'y': 12}
        self._liste_zones = [Zone(1, 3), Zone(2, 10), Zone(3, 3), Zone(4, 5), Zone(5, 3), Zone(6, 2)]
        self._plateau = []
        self.creation_plateau()

    def get_taille(self):
        return self._taille

    def get_plateau(self):
        return self._plateau

    def get_liste_zones(self):
        return self._liste_zones

    def creation_plateau(self):
        self._plateau = []
        plateau_lettre = [['R', 'R', 'C', 'C', 'C', 'C', 'C', 'R', 'R', 'C', 'V', 'V'],
                          ['R', 'R', 'C', 'V', 'V', 'V', 'V', 'R', 'R', 'C', 'V', 'V'],
                          ['C', 'V', 'C', 'C', 'R', 'R', 'V', 'R', 'R', 'C', 'V', 'V'],
                          ['C', 'R', 'R', 'C', 'R', 'R', 'V', 'R', 'R', 'C', 'V', 'V'],
                          ['C', 'R', 'R', 'V', 'V', 'V', 'V', 'R', 'R', 'R', 'V', 'V'],
                          ['V', 'R', 'R', 'C', 'R', 'R', 'C', 'C', 'V', 'C', 'R', 'C'],
                          ['V', 'V', 'V', 'V', 'R', 'R', 'V', 'V', 'V', 'V', 'R', 'R']]
        liste_region = [Region(1), Region(1), Region(2), Region(2),
                        Region(1), Region(1), Region(2), Region(2),
                        Region(3), Region(3), Region(2), Region(2),
                        Region(4), Region(4), Region(3), Region(3), Region(2), Region(2),
                        Region(4), Region(4), Region(2), Region(2), Region(2),
                        Region(4), Region(4), Region(5), Region(5), Region(6),
                        Region(5), Region(5), Region(6), Region(6)]
        pos_liste_region = 0
        liste_chemin = [Chemin('horizontal'), Chemin('horizontal'), Chemin('horizontal'), Chemin('horizontal'), Chemin('horizontal'), Chemin('croisement', 'SO'),
                        Chemin('croisement', 'SO'), Chemin('croisement', 'NSO'),
                        Chemin('vertical'), Chemin('croisement', 'NE'), Chemin('horizontal'), Chemin('croisement', 'NSO'),
                        Chemin('vertical'), Chemin('horizontal'), Chemin('croisement', 'NSO'),
                        Chemin('croisement', 'NE'),
                        Chemin('horizontal'), Chemin('horizontal'), Chemin('croisement', 'NO'), Chemin('croisement', 'NE'), Chemin('croisement', 'SO'),]
        pos_liste_chemin = 0
        for x in range(self._taille['x']):
            self._plateau.append([])
            for y in range(self._taille['y']):
                match plateau_lettre[x][y]:
                    case 'R':
                        self._plateau[x].append(liste_region[pos_liste_region])
                        pos_liste_region += 1
                        self._plateau[x][y].pos = (x, y)
                    case 'C':
                        self._plateau[x].append(liste_chemin[pos_liste_chemin])
                        pos_liste_chemin += 1
                        self._plateau[x][y].pos = (x, y)
                    case 'V':
                        self._plateau[x].append(None)


class Zone:

    def __init__(self, numero, bonus, nom=None):
        self._nom = nom
        self._numero = numero
        self._regions_dans_zone = []
        self._proprietaire = None
        self._bonus = bonus


class Region:

    def __init__(self, zone, nom=None):
        self._nom = nom
        self._pos = None
        self._proprietaire = None
        self._nb_arme = None
        self._zone = zone

    def get_proprietaire(self):
        return self._proprietaire


class Chemin:
    def __init__(self, direction, complement=None):
        self._pos = None
        self._direction = direction
        self._complement = complement

    def get_direction(self):
        return self._direction

    def get_complement(self):
        return self._complement

    def chercher_si_voisin(self, pos_x, pos_y, arrive_x, arrive_y):
        pass
