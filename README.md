# App de scoring de crédit

L'objectif de cette appli est de présenter un exemple de modèle de scoring de
crédit exposé via FastAPI.

L'app contient un endpoint avec une étape de validation des données via 
*Pydantic* et fait appel à une librairie de preprocessing qui pourrait être 
utilisé pour d'autres modèles. Un fichier de test est présent au sein de cette 
librairie.

La requête retourne alors une probabilité de défaut de paiement ainsi qu'une 
note (A, B ou C).


## Docker

Clonez le repository et téléchargez Docker, puis placez vous à la racine
et lancez les commandes suivantes afin de builder l'image et démarrer le 
container.

```shell
docker build -t scoring_image .
docker run -d --name scoring_fastapi -p 80:80 scoring_image
```


## Accès à la doc de l'API

Consultez la documentation de l'API via l'URL : http://localhost/docs

Cliquez sur le endpoint *scoring*, puis sur *Try it out* et saisissez un ID de 
client ainsi que les données entrantes du modèle (montant emprunté, revenu, ...).

Enfin, cliquez sur *execute* afin de lancer la requête.



## Note explicative

Le code de l'app FastAPI est situé dans app/main.py.

A l'intérieur de ce fichier, l'objet ScoringInput définit le format des données
entrantes et contient deux validators (pour vérifier que le montant à emprunter
est compris entre 0 et 10000€ par exemple).

La fonction get_score récupère les données, applique les fonctions de 
preprocessing, calcule la proba de défaut de paiement et la note et renvoie la 
réponse.

La librairie de preprocessing est contenue dans le dossier preprocessing, 
contenant les fonctions dans core.py et les tests unitaires dans le dossier 
tests.
