# Description technique

## Structure

Il y a 3 dossiers à la racine de se projet :
 - /documentation
 - /frontend
 - /backend

### Backend

Vous trouverez dans le dossier backend un projet Django.
Il possède une base de donnée postgre qui contiendra tous les configurations de l'utilisateur.
Est prévu aussi d'avoir une seconde base contenant sous forme de blob les réseaux brutes (contenant les valeurs des poids et biais des neurones).
Chaque base de données possède un container docker, en plus du container pour le run de Django.

Enfin, le dossier src/main_lib contient la librairie principale, avec dans le fichier src/main_test.py un exemple d'utilisation de la librairie.

### Frontend

TODO
