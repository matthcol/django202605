# Django

## Dependances
```
django
django-extensions
djangorestframework
django-debug-toolbar
drf-spectacular         # Swagger API
jupyterlab
```

## Create project
```
django-admin startproject netpy 
cd netpy
django-admin startapp app_people
django-admin startapp app_movie

python manage.py makemigrations app_people
python manage.py migrate
python manage.py migrate app_people

python manage.py makemigrations app_movie
python manage.py showmigrations app_movie
python manage.py sqlmigrate app_movie 0001_initial
python manage.py sqlmigrate app_movie 0001
python manage.py migrate app_movie

```

Rollback Migration (non appliquée) : supprimer fichier migration

Rollback Migration(s) déjà appliquée(s): numéro migration ou zero
```
python manage.py showmigrations app_movie
python manage.py migrate app_movie zero
# delete migration file
```

## ORM + Notebook
Apres avoir ajouté django-extensions en dépendance et en django_extensions comme app.
```
python .\manage.py shell
python manage.py shell_plus  
python .\manage.py shell_plus --lab           # dans le navigateur
```

Pour lancer le notebook dans VSCode:
```
DJANGO_SETTINGS_MODULE=netpy.settings
```

## Documentation Queries et fonctions
- https://docs.djangoproject.com/en/6.0/ref/models/querysets
- https://docs.djangoproject.com/en/6.0/ref/models/database-functions

## Feed Database
Bash ou cmd:
```
python manage.py shell_plus < feed.py
```

Powershell
```
Get-Content feed.py | python manage.py shell_plus
```

## Docker

### Dépendances

Les dépendances sont déclarées dans `pyproject.toml` avec deux groupes optionnels :
- `[dev]` : debug-toolbar, jupyterlab, ipython
- `[deploy]` : gunicorn

### Développement

Démarrer les deux bases PostgreSQL (app + tests) :
```
docker compose -f docker-compose.dev.yml up -d
```

Charger les variables d'environnement depuis `.env.dev` puis lancer Django :
```
# Bash/cmd
python manage.py runserver

# PowerShell (définir les variables manuellement ou via un outil dotenv)
$env:DB_HOST="localhost"; python manage.py runserver
```

Lancer les tests unitaires sur la base dédiée (sans persistence) :
```
python manage.py test --settings=netpy.settings_test
```

### Déploiement

Copier le fichier exemple et renseigner les valeurs :
```
cp .env.deploy.example .env.deploy
```

Builder le wheel (génère `dist/netpy-*.whl`) :
```
pip install build
python -m build --wheel
```

Builder l'image et démarrer les conteneurs (app + PostgreSQL) :
```
docker compose --env-file .env.deploy up -d --build
```

L'entrypoint applique automatiquement les migrations au démarrage du conteneur app.

Pour arrêter :
```
docker compose --env-file .env.deploy down
```