# Recipes API

## Technology stack:
- Python 3.8.5
- Aiohttp 3.7.4
- PostgreSQL 5.2

## Сommands to start the service:
- python -m venv
- .\recipes-project\Scripts\activate
- pip install -r requirements.txt
- python app.py

## Database:
- Create Database 'recipes'
- Run all SQL queries from the [file "queries"](https://github.com/uzhegovaelena/recipes-project/blob/master/files/queries.sql) (creating the necessary tables and filling with test data).


![Link](https://github.com/uzhegovaelena/recipes-project/blob/master/files/Database%20schema.drawio.png)

## Enviroment variables: 
```
PORT=8080

# variables for DB connection:
DB_DATABASE=recipes
DB_USER=replace_me
DB_PASSWORD=replace_me
DB_HOST=localhost
DB_PORT=5432
```

## Endpoints

### Users

#### Create a new user

```
curl --request POST \
  --url http://localhost:8080/users \
  --header 'Content-Type: application/json' \
  --data '{
  "username": "test",
  "email": "test@gmail.com",
  "password": "test"
}'
```

#### Get user info by username

```
curl --request GET \
  --url http://localhost:8080/users/[username] \
  --header 'apikey: ***'
```

#### Authentication

```
curl --request GET \
  --url http://localhost:8080/users/auth \
  --header 'Content-Type: application/json' \
  --data '{
  "email": "test@gmail.com",
	"password": "test"
}'
```

#### Get top 10 users by numbers of recipes

```
curl --request GET \
  --url http://localhost:8080/users/top \
  --header 'apikey: ***'
```

### Recipes

#### Create a new recipe

```
curl --request POST \
  --url http://localhost:8080/recipes \
  --header 'Content-Type: application/json' \
  --header 'apikey: ***' \
  --data '{
  "title": "milk",
  "description": "description"
}'
```

#### Get list of recipes

```
curl --request GET \
  --url 'http://localhost:8080/recipes?limit=30&offset=0' \
  --header 'apikey: ***'
```

#### Get a recipe

```
curl --request GET \
  --url http://localhost:8080/recipes/28 \
  --header 'apikey: ***'
```

