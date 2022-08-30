# Django-To-Do-list-with-user-authentication

Installation

- First clone the project.

```sh
git clone https://github.com/burno-lima/Django-To-Do-list-with-user-authentication.git
```

- Create venv and activate.

```sh
python -m venv .venv
```
```sh
.venv/Scripts/activate
```
- Install dependency for project.

```sh
pip install -r requirements.txt
```

- Perform pending migration.

```sh
python manage.py migrate
```

- Create superuser.

```sh
python manage.py createsuperuser --username="admin" --email="admin@email.com"
```

- Start server.

```sh
python manage.py runserver
```
- Access

<code><a href="http://127.0.0.1:8000">127.0.0.1:8000</a></code>

