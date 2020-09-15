# CRUD App with Django / Python

### To run the app:
```
python3 manage.py runserver
```

### Database
* SQLite DB
* Upon making changes in 'models.py', be sure to run 
```
python3 manage.py makemigrations requests
```
* Verify migration worked by running:
```
python3 manage.py sqlmigrate polls 0001
```
* Now migrate the model tables into the database:
```
python3 manage.py migrate
```