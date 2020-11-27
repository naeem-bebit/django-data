1. Create the project,
   `mlapps` is the name of the project

   ```console
   $ django-admin startproject mlapps .
   ```

1. Run the server

   ```console
   $ python3 manage.py runserver
   $ python3 manage.py migrate
   ```

   - View it at `http://localhost:8000/` or `http://127.0.0.1:8000/`

1. Adding the apps to the src dir called `authenticate`

   ```console
   $ python3 manage.py startapp authenticate
   ```
