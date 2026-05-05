# Django

## Dependances
```
django
django-extensions
djangorestframework
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
python .\manage.py shell_plus --lab
```