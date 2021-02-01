# Django Boilerplate


Django-boilerplate is a custom boilerplate for multi tenancy applications within the same database.

### Steps

  1. Enable virtualenv
  2. Install requirements.txt
  3. Run boilerplate_configurator.py
  4. Give the name of the project (Make sure there is no existing project of that name)
  5. Setup database
  6. Makemigrations, migrate and runserver
  - Check for items in other files as well like Dockerfile, gunicorn.conf

### Code

```sh
$ source venv/bin/activate
$ python3 boilerplate_configurator.py
$ <project_name>
```
### TODO
 - Try using Custom User model with fixtures for admin user like AUTH USER MODEL, get_user_model()
 - Check for any missing data or improper imports
