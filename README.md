# Setting up the local machine

1. Install the latest version of **Python** and **Git**.
2. In a command line, check if `pip` was installed.
   ```bash
   $ pip --version
   ```
   Note: For Windows users, you may need to add `pip` into your PATH from the environmental variables.
3. Install the virtualenvwrapper using `pip`. This would allow us to create a virtual environment for our project.<br>
   _For Windows_:
   ```bash
   $ pip install virtualenvwrapper-win
   ```
   _For Linux/UNIX_:
   ```bash
   $ pip install virtualenvwrapper
   ```
   <br>

# Setting up the environment and Django

1. Create a virtual environment to be used for the project. This will make an isolated **Python** environment free of other libraries and packages. You may name it as you desire.
   ```bash
   $ mkvirtualenv <name-of-your-environment>
   ```
2. You should notice that the your terminal now has a modified prompt which looks like the following:
   ```bash
   (<name-of-your-environment>)$
   ```
   Note: After exiting your terminal, the virtual environment would naturally be deactivated upon your next launch or another spawn of terminal. You do not need to recreate the virtual environment every project. To use the created virtual environment again, you may use the following command:\_
   ```bash
   $ workon <name-of-your-environment>
   ```
3. Install **Django** using `pip`.
   ```bash
   (<name-of-your-environment>)$ pip install django
   ```
4. Once installed you issue the `django-admin` command to check. You should see a list of commands that can be issued.
   ````
   (<name-of-your-environment>)$ django-admin
   ```bash
   ````
5. Create your project using the following command.
   ```bash
   (<name-of-your-environment>)$ django-admin startproject twitterclone
   ```
   _Note: In this case, the name of the project was **twitterclone**. General rule for naming convention is to ensure that the name has no spaces nor non-alphanumeric characters._
   
   The path of your project should look similar to one below:
   ```
   twitter-clone/
   |__ twitter-clone/
   |     |__ __pycache__/
   |     |__ __init__.py
   |     |__ asgi.py
   |     |__ settings.py
   |     |__ urls.py
   |     |__ wsgi.py
   |__ db.sqlite3
   |__ manage.py
   ```
6. Run the server using the following command:

   ```bash
   (<name-of-your-environment>)$ python manage.py runserver
   ```

   You should be able to access the page on your web browser at http://127.0.0.1:8000. You may stop serving it using `Ctrl + C`.

# Setup .env file for environmental variables
1. To properly integrate environmental variables in a **Django** project, additional dependency must be installed. Using `pip`, install `python-decouple`.
   ```bash
   (<name-of-your-environment>)$ pip install python-decouple
   ```
2. Inside your project directory, enter the subdirectory and create a .env file. For now, add the following lines.
   ```
   SECRET_KEY=
   ```
3. Open `settings.py` from inside the project subdirectory.
4. Just below the `from from pathlib import Path` line, import `config` from the `decouple` library.
   ```python
   ...
   from pathlib import Path
   from decouple import config
   ...
   ```
5. Copy the value of the variable `SECRET_KEY`.
   ```python
   SECRET_KEY = 'django-insecure-i&n$0x7e_(4jeo&!tbfq%*yk(t-486lt^nnrzqay9+2odd(y#p'
   ```
6. Paste the value to the `SECRET_KEY` variable in the `.env` file.
   ```
   SECRET_KEY=django-insecure-i&n$0x7e_(4jeo&!tbfq%*yk(t-486lt^nnrzqay9+2odd(y#p
   ```
   *Note: Make sure that there are no spaces in between the variable name, equal sign, and the value itself.*
7. Go back to the `settings.py` file and replace the value of `SECRET_KEY` by referencing the environmental variable assigned to it using the `config` function from the `decouple` library.
   ```python
   SECRET_KEY = config('SECRET_KEY')
   ```
8. Go ahead as well on modifying the `DEBUG` variable.<br>
   *settings.py*
   ```python
   DEBUG = config('DEBUG', default=True, cast=bool)
   ```
   *.env*
   ```
   DEBUG=True
   ```
   *Note: During development, always set `DEBUG` to `True` to see debug messages. Set it only to false when testing or deploying for production.*
8. Try to run the server again. You should not experience any problem.

   ```bash
   (<name-of-your-environment>)$ python manage.py runserver
   ```

   The updated path of your project should look similar to one below:
   ```
   twitter-clone/
   |__ twitter-clone/
   |     |__ __pycache__/
   |     |__ __init__.py
   |     |__ .env
   |     |__ asgi.py
   |     |__ settings.py
   |     |__ urls.py
   |     |__ wsgi.py
   |__ db.sqlite3
   |__ manage.py
   ```
   <br>

# Setting up the repository

1. Create a new repository from your **Github** account.<br>
   *Note: Make sure to intialize an empty repository.*
2. Go inside the directory of your **Django** project.
   ```bash
   $ cd /path/to/cloned/repository/
   ```
3. Initalize the repository from your local machine.
   ```bash
   $ git init
   $ git branch -M main
   $ git remote add origin https://github.com/<your-github-user>/<your-repository>.git
   ```
4. Track the files and do an an intial commit.
   ```bash
   $ git add .
   $ git commit -m "Intialized repository with Django project."
   ```
5. Create a new branch named `development` and checkout to it. This will be your dedicated branch during active development. You may add, commit, and push to this branch during the course of development.
   ```bash
   $ git branch development
   $ git checkout development
   ```
6. Before proceeding with the development, setup a `.gitignore` file on the root directory of the project (same directory as the `manage.py` file) with the following lines inside:
   ```
   .env
   *.log
   *.pot
   *.pyc
   __pycache__/
   local_settings.py
   db.sqlite3
   db.sqlite3-journal
   media
   ```

   The updated path of your project should look similar to one below:
   ```
   twitter-clone/
   |__ twitter-clone/
   |     |__ __pycache__/
   |     |__ __init__.py
   |     |__ .env
   |     |__ asgi.py
   |     |__ settings.py
   |     |__ urls.py
   |     |__ wsgi.py
   |__ .gitignore
   |__ db.sqlite3
   |__ manage.py
   ```
   <br>