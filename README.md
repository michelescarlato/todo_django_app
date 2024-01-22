# Todo application on Django

Create a virtual environment before installing the dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies with:

```bash
pip install -r requirements.txt
```

Run the server with:

```bash
python3 manage.py runserver
```

## Create a new user
Use the Register function.
When creating a new user, remember to use at least an alphanumeric password with a special character(e.g. Supercali654!).
Currently, the App doesn't handle error messages related to weak password usage, and the user will not be created.

## Login with an existing user
You can use `antonio` with password `Supercali654!`.

## Test the app

With the authenticated user will be possible to create new tasks, setting a title and a description (optional).
Clicking on the created task, it can be `marked` as completed.
Clicking on the `X` close to the task name it can be `deleted`.
The `search bar` will help you to look for a specific task.

On the top right you find the `logout` button.
