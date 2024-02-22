# Application de Résultats de Matchs de Football

Cette application web affiche les résultats des matchs de football ainsi que les classements des ligues. Les données sont récupérées à partir de l'API de [API Football](https://apiv3.apifootball.com/documentation/).

## Fonctionnalités

- Affichage des résultats des matchs de football pour différentes ligues.
- Affichage des classements des ligues.
- Affichage des détails d'un match spécifique.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Lancez l'application en exécutant `python app.py`.

## Utilisation

- Accédez à l'application via votre navigateur Web à l'adresse [http://localhost:5000]
- Sélectionnez une date et une ligue dans le formulaire et cliquez sur le bouton "Rechercher" pour afficher les résultats des matchs et les classements correspondants.
- Cliquez sur un match pour afficher ses détails.

## Structure du Projet

- `app.py`: Fichier principal de l'application Flask.
- `templates/`: Répertoire contenant les modèles HTML et css.
- `index.html`: Fchier html permettant d'afficher les résultats du jour choisi et le classement de la ligue.
- `match_details.html`: Fichier contenant les détails du match sur lequel on clique.
- `styles.css`: Feuille de style CSS pour personnaliser l'apparence de l'application.

## Auteur

Ce projet a été développé par Aguilar Flavien, Bichon-Nougaillac Benjamin, Fernandez Julian

github : https://github.com/Miiruki/football-analysis