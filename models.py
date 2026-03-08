class Creature:
    def __init__(self, nom, description, pv, defense, type_degats):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.pv_max = pv # Utile pour ne pas soigner au-delà du max
        self.defense = defense # La Classe d'Armure (CA) 
        self.type_degats = type_degats
        self.etats = [] # Pour gérer "paralysé", "empoisonné", etc. 

    def recevoir_degats(self, montant):
        """Réduit les PV et s'assure qu'ils ne tombent pas sous 0."""
        self.pv -= montant
        if self.pv < 0:
            self.pv = 0



class Heros(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, arme):
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme
        self.compagnon = None # Pour stocker le "Lion du Mali" par exemple

    def invoquer(self, nom_entite):
        """Prépare l'arrivée d'un allié sur le terrain."""
        self.compagnon = nom_entite
    def __init__(self, nom, description, pv, defense, type_degats, arme):
        # super() appelle le constructeur de Creature pour remplir le nom, pv, etc.
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme
        self.inventaire = []

class Monstre(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, resistances):
        super().__init__(nom, description, pv, defense, type_degats)
        self.resistances = resistances
        self.est_en_eveil = False # Passe à True si les PV sont bas

    def verifier_seuil_eveil(self):
        """Vérifie si le monstre doit passer en mode Éveil (ex: < 30% PV)."""
        if self.pv <= (self.pv_max * 0.3):
            self.est_en_eveil = True


class Action:
    def __init__(self, nom, lanceur, cible=None):
        self.nom = nom
        self.lanceur = lanceur # Qui fait l'action
        self.cible = cible     # Sur qui (peut être vide pour une invocation)                    