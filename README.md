# Django-To-Do-list-with-user-authentication

![ToDoTask](https://user-images.githubusercontent.com/80166382/187453793-fe3f1c2b-e2eb-4654-807d-d1b4c753694c.png)

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
.venv\Scripts\activate
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

Reference: _https://www.youtube.com/watch?v=llbtoQTt4qw&t=1s_
