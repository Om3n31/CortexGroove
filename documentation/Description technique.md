# Description technique

## Structure

Il y a 3 dossiers à la racine de se projet :
 - /documentation
 - /frontend
 - /backend

### Backend

Vous trouverez dans le dossier backend un projet Django.
Il possède une base de donnée postgre qui contiendra tous les configurations de l'utilisateur.
Est prévu aussi d'avoir une seconde base contenant sous forme de blob les réseaux bruts (contenant les valeurs des poids et biais des neurones).
Chaque base de données possède un container docker, en plus du container pour le run de Django.

Enfin, le dossier src/main_lib contient la librairie principale, avec dans le fichier src/main_test.py un exemple d'utilisation de la librairie.

### Frontend

Le dossier frontend est basé sur nuxt (framework qui fonctionne avec Vue). Ce côté du projet suit une architecture à basse de composants. 
L'interface est actuellement directement lancée via npm pour développer plus facilement, mais nous avons également mis en place de la conteneurisation.
L'architecture des dossiers est la suivante : 
- assets : css et images png / svg
- components : composants graphiquess réutilisables
- layouts : arrangement graphique général des pages (ici ons e contentera d'en utiliser un seul, avec le bandeau en haut)
- pages : pour les pages
- public : icône
- server : à terme pourra servir a créer des sous dossiers contenant des middlewares par exemple, ou bien des pré traitements de données récupérées du back
