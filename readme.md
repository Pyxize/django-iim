## Django IIM App

## Make migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
## Load fixtures
```bash
python manage.py loaddata person.json
python manage.py loaddata category.json
python manage.py loaddata article.json
```
## Display local app
```bash
python3 manage.py runserver
```

## Architecture

* Notre projet est constitué d'un dossier `App` qui va permettre l'initialisation des projets,
paramétré le projet django et gérer les urls (routes) des différents projets


* Chaque dossier à la racine correspond à un projet (cv, showcase,..) avec leurs `migrations, template, view,..
`
  

* Un dossier `static` pour le `css, javascript et images`


* A la racine un fichier `manage.py` générer par django pour faire des commandes (voir les commandes en haut de la doc)


* Le fichier `requirements.txt` pour les différents package, le `gitignore `et le fichier de documentation