# Blog Application (Django + Postgres)

This is a **simple Blog platform** with Categories, Comments, User authentication, rich-text blogs, pagination, and SEO-friendly slugs.  
The project uses **Django**, **Postgres**, **pytest**, **coverage**, and **mypy-django plugin** for static typings.

---

### 🟣 MyPy-Django Typing

To enable typings for your ORM and `User`:

The project uses the `mypy-django plugin` configured in `mypy.ini` to assist with Django-specific typing. 
For example, the 'user' property is not defined on a request by default, but inserted via Auth middleware, 
so the plugin allows that association to be made for developer and IDE convenience.

```ini
[mypy]
plugins = mypy_django_plugin.main
ignore_missing_imports = true
```

### 🟣 Makefile Commands

The following Makefile commands are available to streamline your workflow:

 - Run Tests (with pytest): `make test`
 - Calculate Coverage: `make coverage`
 - Calculate Coverage and generate HTML report: `make coverage-html`
 - Format the src code with Ruff: `make format`
 - Run the app in development mode: `make run`
