# Backend

## Setup

- Create a virtual environment
- Install required packages with either pip or poetry
- Create an empty postgresql database
- check `demo.env` and a new `.env` file with same values but add your postgresql database connection string.
- apply migrations using `python manage.py migrate`

## Run backend

```
python manage.py runserver
```
