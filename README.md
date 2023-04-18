1. Create virtualenv
   ```console
   python -m venv env#name of the virtualenv
   env\Scripts\activate
   ```

1. Create the project
   `mlapps` is the name of the project

   ```console
   $ django-admin startproject mlapps .
   ```

1. Run the server

   ```console
   $ python3 manage.py runserver
   $ python manage.py makemigrations #Make changes to your models and run migrate
   $ python3 manage.py migrate
   ```

   - View it at `http://localhost:8000/` or `http://127.0.0.1:8000/`

1. Adding the apps to the src dir called `authenticate`

   ```console
   $ python3 manage.py startapp authenticate
   ```

1. Adding superuser(admin)

   ```console
   $ python manage.py createsuperuser
   ```
