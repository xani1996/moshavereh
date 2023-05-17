#!bin/sh

echo "----- Collect static files ------ "
python manage.py collectstatic

echo "-----------Apply migration--------- "
python manage.py migrate

echo "-----------Run gunicorn--------- "
gunicorn -b :5000 test_blog.wsgi:application