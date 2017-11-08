### Tutorial and explanation at
http://techarena51.com/index.php/buidling-a-database-driven-restful-json-api-in-python-3-with-flask-flask-restful-and-sqlalchemy/

### Steps to Install

     pip install -r requirements.txt
     python run.py
     
### Resource URL’s

- GET   http://localhost:8000/v1/users.json Returns a list of all users

- POST  http://localhost:8000/v1/users.json Creates a user and returns with user id

- GET   http://localhost:8000/v1/users/\<user_id\>.json Returns user details for the given user id if the it exists
