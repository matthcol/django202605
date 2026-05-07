FROM python:3.13-slim

WORKDIR /app

# wheel = app + toutes les dépendances principales
# gunicorn est un extra [deploy], installé séparément
COPY dist/*.whl ./
RUN pip install --no-cache-dir *.whl gunicorn

# manage.py nécessaire pour l'entrypoint (migrate)
COPY manage.py entrypoint.sh ./

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["gunicorn", "netpy.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
