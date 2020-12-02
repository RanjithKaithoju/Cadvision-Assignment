# Cadvision-Task

#Backend
1) django & djangorestframework
Install required packages from requirement.txt

django-admin startproject backend

python manage.py startapp posts

Migrate the models and sync the db
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

API'S
posts/
comments/
^post/like/(?P<pk>\d+)/$ [name='post_like']
^post/dislike/(?P<pk>\d+)/$ [name='post_dislike']


#Front end(Single Page App)
frontend/index.html
-->Ajax calls for API's.