# Django Todo

A minimal to-do list app built with Django: add, edit, and delete items against
a SQLite-backed `Item` model, server-rendered with a single template.

## Stack

- Django 5.1
- SQLite (default Django backend)
- Server-rendered templates (no frontend framework)

## Local setup

```bash
python -m venv venv
source venv/bin/activate   # venv\Scripts\activate on Windows
pip install -r requirements.txt

export DJANGO_SECRET_KEY="replace-with-a-real-secret"   # optional for local dev
python manage.py migrate
python manage.py runserver
```

## Routes

| Path | View | Purpose |
|---|---|---|
| `/` | `TodoAppView` | List all items |
| `/todo/` | `AddTodo` | Add an item |
| `/todo/delete/<id>/` | `DeleteTodo` | Delete an item |
| `/todo/edit/<id>/` | `EditTodo` | Edit an item |
| `/todo/update/<id>/` | `UpdateTodoItem` | Save an edit |
