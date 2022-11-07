# Assignment Submission by Hardeep Kumar to Assist 2 Path Tech

## Info

There are two folders, 'apt_back' for Backend and 'apt_front' for Frontend.
Backend is written using Django and requires postgresql to work.
Frontend is written using Vue 3.

## Setup

## Backend

- cd to apt_back
- create a virtual environment if needed. If using poetry then it will handle itself.
- Install dependencies using either poetry or pip

  ```sh
  poetry install
  # or
  pip install -r requirements.txt
  ```

- create a new file named `.env` using `demo.env` as reference and add url to postgres server
  ```env
  DATABASE_URL=<postgresql_uri_string>
  # example
  DATABASE_URL=postgresql://localhost@localhost/apt
  ```
- apply migrations using `python manage.py migrate`
- start dev server `python manage.py runserver`

> # Note: the server must run on port 8000 or else frontend won't work

### Frontend

- cd to apt_front
- use either yarn or npm to install dependencies

  ```sh
  yarn install
  # or
  npm install
  ```

- To start the serve use `yarn dev` or `npm run dev`
- Open the url in browser
