# Posts,comments with Django Rest & Ajax

# Backend
1) django & djangorestframework
Install required packages from requirement.txt

django-admin startproject backend

python manage.py startapp posts

Migrate the models and sync the db
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

# API'S
1) posts/
2) comments/
3) ^post/like/(?P<pk>\d+)/$ [name='post_like']
4) ^post/dislike/(?P<pk>\d+)/$ [name='post_dislike']


# Front end(Single Page App)
frontend/index.html
-->Ajax calls for API's.
