

todo rest API with django. for ACM ascendo @2021<br>
<a href="https://notes-workshop.stackblitz.io/">Final product</a>
## Basics

* An API is an application programming interface. It is a set of rules that allow programs to talk to each other. The developer creates the API on the server and allows the client to talk to it.
* REST determines how the API looks like. It stands for “Representational State Transfer”. It is a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called a resource) when you link to a specific URL.
* Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern.
* Django REST framework is a powerful and flexible toolkit for building Web APIs. ... The Web browsable API is a huge usability win for your developers. Authentication policies including packages for OAuth1a and OAuth2. Serialization that supports both ORM and non-ORM data sources.
## Getting Started





### Documentations

* <a href="https://docs.djangoproject.com/en/3.2/"> Django </a>
* <a href="https://www.django-rest-framework.org/"> DRF </a>
* <a href="https://www.postgresql.org/docs/">Postgres</a>
* <a href="https://djoser.readthedocs.io/en/latest/authentication_backends.html"> DJOSER </a>

### Starting

* clone the repo
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
# A simple rest api with DRF

## step1 : installation

* <a href="https://docs.djangoproject.com/en/1.8/howto/windows/#:~:text=Django%20can%20be%20installed%20easily,version%20in%20the%20command%20prompt.">Django Installation</a>
* <a href="https://www.django-rest-framework.org/#installation">DRF installation and setting up </a>
* <a href="https://djangocentral.com/visual-studio-code-setup-for-django-developers/">Configuring vs code</a>
* <a href="https://www.postman.com/downloads/"> Postman </a>
* <a href="https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04"> Postgres </a>
* <a href="https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html"> Heroku </a>

#### <a href="https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html">cookie cutter django</a>
### <a href="https://www.geeksforgeeks.org/how-to-enable-cors-headers-in-your-django-project/">Enabling cross origin sharing</a>
### Configuring project for deploying in heroku

- create a free heroku account,<a href="https://devcenter.heroku.com/articles/heroku-cli#download-and-install"> download and install heroku cli</a>
```bash
sudo snap install --classic heroku
```
- install wsgi server, whitenoise for static file managing. psycopg2 for postgres

```
pip install django gunicorn whitenoise dj-database-url psycopg2
```
<br>


<i>requirements.txt</i>
```
Django==3.2.3
djangorestframework==3.12.4
psycopg2==2.8.6
pytz==2021.1
dj-database-url==0.5.0
gunicorn==20.1.0
```

- Add Procfile 

```
web: gunicorn <nameOfProject>.wsgi --log-file -
```
- add .gitignore

```
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
venv/
```

- initialize git

- login to heroku
```
heroku login
```
- change settings.py

```
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1',            'nameofapp.herokuapp.com']

DEBUG = False # use heroku logs for getting logs


```
- set secret key as env variable

```
SECRET_KEY = os.environ.get('SECRET_KEY')
heroku config:set SECRET_KEY=secretkey
```
- statics
```
whitenoise.runserver_nostatic #apps
whitenoise #requirements.txt
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
'whitenoise.middleware.WhiteNoiseMiddleware',  #middleware
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR,'project_name/static')
]
```

- configure database
```
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
```
- media
```
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
```
- git commit

- add postgres addon
```
heroku addons:create heroku-postgresql:hobby-dev
heroku config -s | grep DATABASE_URL
```

- disable collect static
```
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku master
```
- run bash
```
heroku open
heroku run bash
```
## For queries

contact

1. Ajith P M
2. Niranjan B



## License

This project is licensed under the GNU License - see the LICENSE.md file for details


As a part of ACM ascendo 2021
