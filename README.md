# projet_poo_dnd
Dépôt GitHub de notre projet 


# 🐉 Projet POO - Système de combat RPG

Bienvenue dans le dépôt du **Groupe 2** pour le projet de programmation orientée objet. Ce projet utilise les concepts de classes, d'héritage et de polymorphisme pour simuler un système de combat type DnD.

## 🏗️ Architecture du Projet (Rôle 1)

L'architecture est découpée en 5 fichiers pour faciliter la collaboration via Git et éviter les conflits :

* **`models.py`** : Contient les classes `Creature`, `Heros`, `Monstre` et `Action`. **C'est le cœur logique, aucun `print()` ne doit y être ajouté.**
* 
**`engine.py`** : (Rôle 2) Gérera les lancers de dés (1d20, 3d6) et les calculs de réussite critique.


* **`data.py`** : (Rôle 3) Contiendra les instances de nos héros (ex: Soundiata Keïta) et de nos adversaires (ex: Mobutu).
* 
**`terminal_ui.py`** : (Rôle 4) Gérera l'affichage des menus et les entrées utilisateur (`input`).


* 
**`main.py`** : (Rôle 5) La boucle principale (REPL) qui orchestre le combat.



---

## 🛠️ Guide d'utilisation des Modèles

Pour mes collaborateurs, voici comment utiliser les classes que j'ai mises en place :

### 1. Créer une nouvelle Créature

Pour ajouter un personnage ou un monstre dans `data.py`, utilisez les constructeurs suivants :

* 
**Héros** : `Heros(nom, description, pv, defense, type_degats, arme)`.


* 
**Monstre** : `Monstre(nom, description, pv, defense, type_degats, resistances)`.



### 2. Gestion des Dégâts

Toute créature possède une méthode `.recevoir_degats(montant)`. Elle déduit les points de vie tout en s'assurant qu'ils ne tombent pas en dessous de 0.

### 3. Fonctionnalités Spéciales (Personnalisation)

J'ai préparé le terrain pour nos fonctionnalités uniques :

* **Mode Éveil** : Les monstres comme Mobutu possèdent un attribut `est_en_eveil`. Le Maître des Calculs devra l'activer si les PV sont bas pour booster les dégâts.


* **Invocations** : Les héros peuvent utiliser la méthode `.invoquer()` pour appeler des alliés (comme le Lion du Mali pour Soundiata).

---

## 🚀 Instructions pour l'équipe

1. **Récupération** : Faites un `git pull` avant de commencer à travailler.
2. **Commits** : Faites des commits clairs (ex: `feat: ajout des lancers de dés dans engine.py`).
3. 
**Rôles** : Respectez bien la séparation des fichiers pour ne pas casser la boucle principale.



