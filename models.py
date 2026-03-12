import random

class Creature:
    """Classe mère gérant la structure de base de toute entité au combat."""
    def __init__(self, nom, pv, ca, type_degat):
        self.nom = nom
        self.pv = pv
        self.max_pv = pv
        self.ca = ca  # Classe d'Armure (Défense)
        self.type_degat = type_degat
        self.initiative = 0

    def est_vivante(self):
        """Vérifie si la créature a encore des points de vie."""
        return self.pv > 0

    def lancer_initiative(self):
        """Génère un score d'initiative (1d20)."""
        self.initiative = random.randint(1, 20)
        return self.initiative

    def recevoir_degats(self, montant, type_attaque=None):
        self.pv = max(0, self.pv - montant)
        return montant

    def attaquer(self, cible, moteur_calcul):
        return moteur_calcul.calculer_attaque(self, cible)

class Hero(Creature):
    """Classe représentant les figures historiques (Joueurs)."""
    def __init__(self, nom, pv, ca, type_degat, arme, histoire, special=None):
        super().__init__(nom, pv, ca, type_degat)
        self.arme = arme
        self.histoire = histoire
        self.type_special = special # 'invocation', 'contextuel', 'eveil'
        self.special_disponible = True

class Monstre(Creature):
    """Classe représentant les adversaires (PNJ)."""
    def __init__(self, nom, pv, ca, type_degat, resistance, environnement_natal):
        super().__init__(nom, pv, ca, type_degat)
        self.resistance = resistance
        # Chaque monstre possède maintenant son propre objet Environnement
        self.environnement_natal = environnement_natal 

    def recevoir_degats(self, montant, type_attaque=None):
        if type_attaque == self.resistance:
            montant //= 2
        return super().recevoir_degats(montant)

class Environnement:
    """Classe gérant les lieux de combat liés aux monstres."""
    def __init__(self, nom, type_terrain):
        self.nom = nom
        self.type_terrain = type_terrain # "Savane", "Aquatique", etc.

    def __str__(self):
        return self.nom