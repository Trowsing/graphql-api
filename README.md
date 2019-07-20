# GraphQL Django API
This is a representation of the basic GraphQL structure to create an API integrated with Django.

#### Running locally:
After cloning the repository:
```console
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
You can also load the fixture to populate your database
```
$ python manage.py loaddata data.json
```
#### Testing the API:
- Go to: _127.0.0.1:8000/api_ or _localhost:8000/api_
- Create your own query or paste the contents of `graphql-queries.txt`
- Have fun!


