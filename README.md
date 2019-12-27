Flask App Template
===================
This is meant to be a quickstart to a flask app with a relational database social login managed by firebase

#Setting up the Environment
$pyenv virtualenv <name>
$pyenv activate <name>
$pip install -r requirements.txt

touch .env
# Setting up the Database

$ psql
# create database database-name;
CREATE DATABASE
# \q

<Add the database uri to your .env file>

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

*note* in the future when you change models in the database you need to run

python manage.py db migrate
python manage.py db upgrade
