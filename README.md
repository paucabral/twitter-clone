# Twitter<b>Clone</b>

### **Author**: Pau Cabral<br>

<br>

This is TwitterCLONE, a simple Twitter clone made using Django framework in Python.

This tutorial tackles the development of a Django web application up to its deployment to Heroku.

<br>

# Setting up the local machine

1. Install the latest version of **Python** and **Git**.
2. In a command line, check if `pip` was installed.
   ```bash
   $ pip --version
   ```
   _Note: For Windows users, you may need to add `pip` into your PATH from the environmental variables._
3. Install the `virtualenvwrapper` using `pip`. This would allow us to create a virtual environment for our project.<br>
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
   $ mkvirtualenv twtclone
   ```
   *Note: In this case, the name of the environment was set to *twtclone\*.
2. You should notice that the your terminal now has a modified prompt which looks like the following:
   ```bash
   (twtclone)$
   ```
   _Note: After exiting your terminal, the virtual environment would naturally be deactivated upon your next launch or another spawn of terminal. You do not need to recreate the virtual environment every project. To use the created virtual environment again, you may use the following command:_
   ```bash
   $ workon twtclone
   ```
3. Install **Django** using `pip`.
   ```bash
   (twtclone)$ pip install django
   ```
4. Once installed you issue the `django-admin` command to check. You should see a list of commands that can be issued.
   ```bash
   (twtclone)$ django-admin
   ```
5. Create your project using the following command.

   ```bash
   (twtclone)$ django-admin startproject twitterclone
   ```

   _Note: In this case, the name of the project was **twitterclone**. General rule for naming convention is to ensure that the name has no spaces nor non-alphanumeric characters._

   The path of your project should look similar to one below:

   ```
   twitter-clone/
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ db.sqlite3
   |__ manage.py
   ```

6. Run the server using the following command:

   ```bash
   (twtclone)$ python manage.py runserver
   ```

   You should be able to access the page on your web browser at http://127.0.0.1:8000. You may stop serving it using `Ctrl + C`.

   <br>

# Setup .env file for environmental variables

1. To properly integrate environmental variables in a **Django** project, additional dependency must be installed. Using `pip`, install `python-decouple`.
   ```bash
   (twtclone)$ pip install python-decouple
   ```
2. Inside your project directory, enter the subdirectory and create a .env file. For now, add the following lines.
   ```
   SECRET_KEY=
   ```
3. Open `settings.py` from inside the project subdirectory.
4. Just below the `from from pathlib import Path` line, import `config` from the `decouple` library.
   ```python
   from pathlib import Path
   from decouple import config # Insert the code here.
   ```
5. Copy the value of the variable `SECRET_KEY`.
   ```python
   SECRET_KEY = 'django-insecure-i&n$0x7e_(4jeo&!tbfq%*yk(t-486lt^nnrzqay9+2odd(y#p'
   ```
6. Paste the value to the `SECRET_KEY` variable in the `.env` file.
   ```
   SECRET_KEY=django-insecure-i&n$0x7e_(4jeo&!tbfq%*yk(t-486lt^nnrzqay9+2odd(y#p
   ```
   _Note: Make sure that there are no spaces in between the variable name, equal sign, and the value itself._
7. Go back to the `settings.py` file and replace the value of `SECRET_KEY` by referencing the environmental variable assigned to it using the `config` function from the `decouple` library.
   ```python
   SECRET_KEY = config('SECRET_KEY')
   ```
8. Go ahead as well on modifying the `DEBUG` variable.<br>
   _settings.py_
   ```python
   DEBUG = config('DEBUG', default=True, cast=bool)
   ```
   _.env_
   ```
   DEBUG=True
   ```
   _Note: During development, always set `DEBUG` to `True` to see debug messages. Set it only to `False` when testing or deploying for production._
9. Try to run the server again. You should not experience any problem.

   ```bash
   (twtclone)$ python manage.py runserver
   ```

   The updated path of your project should look similar to one below:

   ```
   twitter-clone/
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ .env
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ db.sqlite3
   |__ manage.py
   ```

   <br>

# Setting up the repository

1. Create a new repository from your **Github** account.<br>
   _Note: Make sure to intialize an empty repository._
2. Go inside the directory of your **Django** project.
   ```bash
   $ cd /path/to/cloned/repository/
   ```
3. Initalize the repository from your local machine.
   ```bash
   $ git init
   ```
4. Before proceeding with the development, setup a `.gitignore` file on the root directory of the project (same directory as the `manage.py` file) with the following lines inside:

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

   The updated path of your project locally should look similar to one below:

   ```
   twitter-clone/
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ .env
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ .gitignore
   |__ db.sqlite3
   |__ manage.py
   ```

5. Track the files and do an an intial commit.
   ```bash
   $ git add .
   $ git commit -m "Intialized repository with Django project."
   ```
6. Configure remote origin as the **Github** repository your created.
   ```bash
   $ git branch -M main
   $ git remote add origin https://github.com/<your-github-user>/<your-repository>.git
   ```
7. Push the project the `main` branch for now. You should see the files in your `master` branch except those declared inside `.gitignore`.
   ```bash
   $ git push -u origin main
   ```
   However, since some files are included in `.gitignore`, the updated path your remote project repository should look similar to one below instead:
   ```
   twitter-clone/
   |__ twitter-clone/
   |   |__ __init__.py
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ .gitignore
   |__ manage.py
   ```
8. Create a new branch named `development` and checkout to it. This will be your dedicated branch during active development. You may add, commit, and push to this branch during the course of the development.
   ```bash
   $ git branch development
   $ git checkout development
   ```
   <br>

# Creating Apps

In **Django**, _apps_ can be used to manage multiple pages with specific features. In this project, we will be adding the _apps_: _accounts_ and _tweets_.

1. In the root project directory, create the _accounts_ app using the following command:
   ```bash
   (twtclone)$ python manage.py startapp accounts
   ```
2. Open the `settings.py` and add `accounts` on the list of `INSTALLED_APPS`.

   ```python
   # Application definition

   INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'accounts',
   ]
   ```

3. You may proceed as well on creating the _tweets_ app with the following command:
   ```bash
   (twtclone)$ python manage.py startapp tweets
   ```
4. Likewise, add `tweets` as well on the list of `INSTALLED_APPS` inside `settings.py`.
   ```python
   INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'accounts',
      'tweets',
   ]
   ```
5. Your local directory structure should now look similar to the one below:

   ```
   twitter-clone/
   |__ accounts/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ views.py
   |__ tweets/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ views.py
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ .env
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ .gitignore
   |__ db.sqlite3
   |__ manage.py
   ```

   <br>

# Creating a super user account and exploring the Admin Panel

Django lets us create a super user account which has direct access to the built-in Admin Panel. It can be used to check and modify the entries in a database, as well as other features such modifying accounts.

1. To start, we need to do an initial migration. Inside the root project directory, run the following command:
   ```bash
   (twtclone)$ python manage.py migrate
   ```
2. After the built-in Django models are migrated, you may now proceed on creating a supersuser using the command below. Simply follow each prompt and provide the necessary information.

   ```bash
   (twtclone)$ python manage.py createsuperuser
   ```

3. Run your project and you may now explore the admin panel at http://127.0.0.1:8000/admin using the account you just created.
   ```bash
   (twtclone)$ python manage.py runserver
   ```
   <br>

# Creating preliminary views and associating each app with specific URL patterns

URL patterns set the paths to which each _app_ or specific functionality can be accessed as a webpage.

1. Open your base `urls.py` (in directory as `twitterclone/twitterclone`).
2. Open the _accounts_ subdirectory (twitterclone/accounts/) and create a file named `urls.py`.<br>
   Your local directory structure should now look similar to the one below:

   ```
   twitter-clone/
   |__ accounts/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ tweets/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ views.py
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ .env
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ .gitignore
   |__ db.sqlite3
   |__ manage.py
   ```

3. Open the `views.py` inside the _accounts_ subdirectory and set the prelimnary _views_. The _views_ are basically the dedicated either classes or functions which serve as the backend of a functionalities found in a specific _Django_ webpage. In this case, we will be using class based views. For now, follow the code below. There are some commented explanations on the added lines as well.

   ```python
   from django.shortcuts import render
   from django.views import View # import the class View from Django library
   from django.http import HttpResponse # import the HttpResponse from Django library

   # Create your views here.

   class Login(View): # Created a Login ckass inherting the View class from the Django library
      def get(self, request, *args, **kwargs): # The get function is the dedicated backend for handling GET requests on a URL. GET requests are made when data is meant to be gathered and displayed in a webpage.
         return HttpResponse('login') # render the text: login upon get request.

      def post(self, request, *args, **kwargs): # The post function on the other hand handles the POST requests on a URL. POST requests are made when data is meant to sent or submitted to backend for processing or storing.
         pass # we will leave this empty for now
   ```

4. Open your previously created `urls.py` file and follow the code below. There are commented explanations below as well.

   ```python
   from django.urls import path # import path to set URL paths
   from . import views # import all the views inside the views.py for the accounts app

   urlpatterns = [
      path('', views.Login.as_view(), name='login'), # the path '/' or the root path was used as the path to locate the Login page.
   ]
   ```

5. The URL however, is still not accessible since it still not connected from the main `urls.py` in the base application. Update the `urlpatterns` in the base `urls.py` (`twitterclone/twitterclone/settings.py`) and add `'/'` as the dedicated path for _accounts_ app since we want the pages contained here (i.e. the landing/login page) to be accessed from the root URL. You may follow the code below and check the commented explanations for the added lines.

   ```python
   from django.contrib import admin
   from django.urls import path, include # import the necessary code to include urlpatterns from other apps.

   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('accounts.urls')), # append the url patterns from accounts app to the base path. This way, all URL patterns can be accessible starting from the base url.
   ]
   ```

6. Now, the `'/'` directory can be viewed after running the project again. You should now see a new content when visiting http://127.0.0.1:8000/.
   ```bash
   (twtclone)$ python manage.py runserver
   ```
7. Proceed on doing the same steps for the _tweets_ app. This time however, the tweet app views and all its URL is meant to be accessible in `/tweets` directory. For now create a view dedicated to view all tweets with a class named `AllTweets`. Proceed on creating a `urls.py` for it as well.<br>

   _twitterclone/tweets/views.py_.

   ```python
   from django.shortcuts import render
   from django.views import View
   from django.http import HttpResponse

   # Create your views here.


   class AllTweets(View):
      def get(self, request, *args, **kwargs):
         return HttpResponse('This is page dedicated to view all tweets.')

      def post(self, request, *args, **kwargs):
         pass
   ```

   _twitterclone/tweets/urls.py_.

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
      path('all-tweets', views.AllTweets.as_view(), name='all-tweets'),
   ]
   ```

   _twitterclone/twitterclone/urls.py_.

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('accounts.urls')),
      path('tweets/', include('tweets.urls')),
   ]
   ```

   In this case, the dedicated URL path for all the URLs in the _tweets_ app was set to `'tweets/'` and the corresponding `AllTweets` view can be found on the URL `'tweets/all-tweets'`. You may run the project again and visit the newly created webpage at http://127.0.0.1/tweets/all-tweets/.

   ```bash
   (twtclone)$ python manage.py runserver
   ```

   Your updated local directory structure should look similar to this.

   ```
   twitter-clone/
   |__ accounts/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ tweets/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ .env
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ .gitignore
   |__ db.sqlite3
   |__ manage.py
   ```

   <br>

# Creating models

_Models_ are basically the representation of databases in Django. Models can be used to create a table and add, delete, or modify entries of a database. In this example, we will be creating a model for the profile information of users.

1. Inside the _accounts_ app directory (`twitterclone/accounts`), open the file `models.py`.
2. Simply add the following lines of code after the `# Create your models here.` comment. This will create a new table dedicated for the Profile of the users.

   ```python
   class Profile(models.Model):
     first_name = models.CharField(max_length=200, null=True)
     last_name = models.CharField(max_length=200, null=True)
     username = models.CharField(max_length=200, null=True)
     email = models.CharField(max_length=200, null=True)
     date_created = models.DateTimeField(auto_now_add=True, null=True)

     def __str__(self):
       return self.username
   ```

3. To fully create the model, it needs to be migrated to the database. Run the command below to make the migration.
   ```bash
   (twtclone)$ python manage.py makemigrations
   ```
4. Afterwards, run the migrate command again to fully construct the changes to the database.

   ```bash
   (twtclone)$ python manage.py migrate
   ```

5. To manage the newly created table from the Admin Panel, open the `admin.py` file of the _accounts_ app and add the following lines of code after the comment `#Register your models here`:

   ```python
   from .models import * # imports all models in accounts app

   admin.site.register(Profile)
   ```

6. You may now check that a new table was added by visiting the Admin Panel at http://127.0.0.1:8000/admin.

   ```bash
   (twtclone)$ python manage.py runserver
   ```

   <br>

# Templates, inheritance, and static files

Templates are basically the frontend component of a basic **Django** project. It is where the corresponding HTML files are placed and referenced by the views.

1. Create a templates directory inside an _app_ subdirectory. In this case, a new directory `templates` is created inside the _accounts_ app (`twitterclone/accounts`).
2. Inside the `templates` directory, create another directory with the same name as the corresponding _app_. In this case, create an `accounts` directory inside the newly created `templates` directory.

   Your updated local directory structure should look similar to this.

   ```
   twitter-clone/
   |__ accounts/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ accounts/
   |       |__ templates/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ tweets/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ .env
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ .gitignore
   |__ db.sqlite3
   |__ manage.py
   ```

3. One great feature of **Django** is the ability to set a base template which can be inherited by other HTML files. This way, particular HTML code can be reused (i.e. for headers, navbar, footers, etc.). For now, we will create a `base.html` as template for all the HTML files in our _accounts_ app. Create a `base.html` file inside the `twitterclone/accounts/templates/accounts` directory. We may import within it an external CSS library as well like bootstrap. In the mean time, add the following contents inside:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <meta http-equiv="X-UA-Compatible" content="IE=edge" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <title>{% block title %}{% endblock %}</title>
       <link
         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
         rel="stylesheet"
         integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
         crossorigin="anonymous"
       />
     </head>
     <body>
       <div class="container">{% block content %} {% endblock %}</div>
     </body>
   </html>
   ```

4. Along with the external CSS refrences, we can also setup our local CSS on a dedicated stylesheet/s and serving them as static files. In the root project directory (`twitterclone/`) create `static` directory and place another set of directories for `css`, `img`, and `js`. This is where we will serve our CSS, static images, and separate Javascript files.

   Your updated local directory structure should look similar to this.

   ```
   twitter-clone/
   |__ accounts/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ accounts/
   |       |__ templates/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ static/
   |   |__ css/
   |   |__ img/
   |   |__ js/
   |__ tweets/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ .env
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ .gitignore
   |__ db.sqlite3
   |__ manage.py
   ```

5. For now add `index.css` file inside the `css` directory and add the following contents below. This will be our dedicated stylesheet for the project.

   ```css
   body {
     background-color: rgb(223, 243, 243);
   }

   .brand {
     font-weight: 1000;
   }
   ```

   Your updated local directory structure should look similar to this.

   ```
   twitter-clone/
   |__ accounts/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ accounts/
   |       |__ templates/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ static/
   |   |__ css/
   |       |__ index.css
   |   |__ img/
   |   |__ js/
   |__ tweets/
   |   |__ __pycache__/
   |   |__ migrations/
   |   |__ __init__.py
   |   |__ admin.py
   |   |__ apps.py
   |   |__ models.py
   |   |__ tests.py
   |   |__ urls.py
   |   |__ views.py
   |__ twitter-clone/
   |   |__ __pycache__/
   |   |__ __init__.py
   |   |__ .env
   |   |__ asgi.py
   |   |__ settings.py
   |   |__ urls.py
   |   |__ wsgi.py
   |__ .gitignore
   |__ db.sqlite3
   |__ manage.py
   ```

6. To be able to serve static files however, there are lines of code to be added to `settings.py`. Import the `os` module and add the following lines of code to define the location of CSS files.<br>

   _twitterclone/twitterclone/settings.py_

   ```python
   import os # put at the top just above "from pathlib import Path"

   ...

   STATIC_DIR = os.path.join(BASE_DIR, "static")

   STATIC_URL = '/static/' # This variable already exists, just add the remaining lines of code.
   STATIC_ROOT = 'staticfiles'

   STATICFILES_DIRS = [
      STATIC_DIR,
   ]
   ```

7. Open the base `urls.py` as well and add the necessary import to serve static files. Your updated `urls.py` and add the following line.

   _twitterclone/twitterclone/urls.py_

   ```python
   from django.conf.urls.static import static
   ```

8. Import the `index.css` file in the `base.html` file by adding the `{% load static %}` invocation and referencing it with the `<link>` tag. You may follow the updated `base.html` code below:
   ```html
   {% load static %}
   <!-- Initiate loading of static files -->
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <meta http-equiv="X-UA-Compatible" content="IE=edge" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <title>{% block title %}{% endblock %}</title>
       <link
         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
         rel="stylesheet"
         integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
         crossorigin="anonymous"
       />
       <link
         rel="stylesheet"
         type="text/css"
         href="{% static 'css/index.css' %}"
       />
       <!-- Import the created CSS file -->
     </head>
     <body>
       <div class="container">{% block content %} {% endblock %}</div>
     </body>
   </html>
   ```
9. This time, let's create a dedicated HTML file which we will bind for the _Login_ view. We will be extending the contents of `base.html` to this file so that the we do not have to rewrite the code we have written inside the `base.html`. Create `login.html` inside the accounts template directory (`twitterclone/accounts/templates/accounts/`).<br>

   _twitterclone/accounts/templates/accounts/login.html_

   ```html
   {% extends 'accounts/base.html' %} {% load static %} {% block title %}
   Twitter Clone | Login {% endblock %} {% block content %}
   <div>
     <h1 class="brand">Twitter Clone</h1>
     <h1>Login</h1>
   </div>
   {% endblock %}
   ```

   _Note: The document title is placed in between the block title blocks and the content which was initialized at the `<body>` tag is placed in between the block content blocks._

10. We will now connect this HTML file to the _Login_ view inside the `views.py` of our _accounts_ app. Modify the `get` function and return a render instead. You may simply follow the code below.

    ```python
    from django.shortcuts import render
    from django.views import View
    from django.http import HttpResponse

    # Create your views here.


    class Login(View):
       def get(self, request, *args, **kwargs):
          return render(request, template_name='accounts/login.html', context={}) # This is the updated line.

       def post(self, request, *args, **kwargs):
          pass
    ```

11. Try running the project again and visit the _Login_ page at http://127.0.0.1:8000/. We will update this page and other views for the _accounts_ app towards the latter part of the project.

    ```bash
    (twtclone)$ python manage.py runserver
    ```

    <br>

# Displaying "tweets" in the _tweets_ app

<!-- This app is dedicated for viewing and posting tweets. Throughout this section, we will be creating a basic Create, Read, Update, and Delete (CRUD) functionality, and discuss the creation of _forms_. -->

This app is dedicated for viewing and posting tweets. For now, we will be adding the functionality to dynamically view the latest "tweets" based on the entry from the database.

1. Start by creating a templates directory and adding a `base.html` file with the following content below. We will be placing a basic navbar in the base template as well. Placing the navbar on the base template will allow it to appear on the rest of _tweets_ app templates as long as the _extends_ block is indicated. Update the contents of `index.css` as well to correspond with the changes.<br>

   _twitterclone/tweets/templates/tweets/base.html_

   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <meta http-equiv="X-UA-Compatible" content="IE=edge" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />

       <title>{% block title %}{% endblock %}</title>

       <link
         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
         rel="stylesheet"
         integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
         crossorigin="anonymous"
       />
       <link
         rel="stylesheet"
         href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
       />
       <link
         rel="stylesheet"
         type="text/css"
         href="{% static 'css/index.css' %}"
       />
     </head>

     <body>
       <header class="navigationHeader sticky-top">
         <nav
           class="navbar navbar-expand-lg navbar-dark bg-primary container-fluid"
         >
           <div class="container">
             <a class="navbar-brand navBrand" href="#"
               >Twitter<span class="brand">CLONE</span></a
             >
             <button
               class="navbar-toggler"
               type="button"
               data-toggle="collapse"
               data-target="#navbarTogglerDemo02"
               aria-controls="navbarTogglerDemo02"
               aria-expanded="false"
               aria-label="Toggle navigation"
             >
               <span class="navbar-toggler-icon"></span>
             </button>

             <div
               class="collapse navbar-collapse align-items-center"
               id="navbarTogglerDemo02"
             >
               <ul class="nav navbar-nav ms-auto align-items-center">
                 <li class="nav-item">
                   <a class="nav-link menuItem" href="#">
                     <i class="fa fa-home fa-3" aria-hidden="true"></i> Home
                   </a>
                 </li>
                 <li class="nav-item">
                   <a class="nav-link menuItem" href="#">
                     <i class="fa fa-newspaper-o fa-3" aria-hidden="true"></i>
                     Timeline
                   </a>
                 </li>
                 <li class="nav-item">
                   <a class="nav-link menuItem" href="#">
                     <i class="fa fa-user fa-3" aria-hidden="true"></i>
                     Profile
                   </a>
                 </li>
                 <li class="nav-item">
                   <a class="nav-link menuItem" href="#">
                     <i class="fa fa-sign-out fa-3" aria-hidden="true"></i>
                     Logout
                   </a>
                 </li>
               </ul>
             </div>
           </div>
         </nav>
       </header>

       <div class="container">{% block content %} {% endblock %}</div>
     </body>

     <script
       src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
       integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
       crossorigin="anonymous"
     ></script>
     <script
       src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
       integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
       crossorigin="anonymous"
     ></script>
     <script
       src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
       integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
       crossorigin="anonymous"
     ></script>
   </html>
   ```

   _twitterclone/static/css/index.css_

   ```css
   body {
     background-color: rgb(223, 243, 243);
   }

   .brand {
     font-weight: 1000;
   }

   .navigationHeader {
     font-weight: 500;
   }

   .navBrand {
     font-size: 1.5rem;
   }

   .menuItem {
     font-size: 1rem;
     color: rgb(198, 223, 226) !important;
   }

   .menuItem:hover {
     color: white !important;
   }
   ```

2. Create another HTML named `all-tweets.html`. Add the following content below for now. This will be binded to the _AllTweets_ view.<br>

   _twitterclone/tweets/templates/tweets/all-tweets.html_

   ```html
   {% extends 'tweets/base.html' %} {% load static %} {% block title %} Twitter
   Clone | Tweets {% endblock %} {% block content %}
   <style>
     .tweetBtn {
       font-size: 80%;
       border-radius: 5rem;
       letter-spacing: 0.1rem;
       font-weight: bold;
       padding: 0.5rem;
       padding-left: 2rem;
       padding-right: 2rem;
       transition: all 0.2s;
       background-color: #2f98d4;
       color: white;
     }

     .tweetBtn:hover {
       background-color: #2473a0;
     }

     .iconBtn {
       color: rgb(81, 91, 102);
       font-size: large;
       font-weight: 1000;
     }

     .iconBtn:hover {
       color: #2f98d4;
     }
   </style>
   <div class="container allTweets">
     <div>
       <div class="card shadow mb-5 rounded border-0">
         <div class="card-header">
           <!-- Name Header -->
           <h2 class="card-title">Good day John Doe, post a tweet!</h2>
           <!-- End Name Header -->
         </div>
         <div class="card-body">
           <form>
             <div class="form-group">
               <!-- Tweet -->
               <textarea
                 required
                 name="tweet"
                 class="form-control"
                 id="createTweet"
                 rows="3"
               >
               </textarea>
               <!-- End Tweet -->
             </div>
             <br />
             <div class="pull-right">
               <button type="submit" class="btn text-white tweetBtn">
                 Tweet
               </button>
             </div>
           </form>
         </div>
       </div>
     </div>
     <br />
     <div>
       <h1>Checkout the latest Tweets!</h1>
       <div class="container">
         <!-- Cards -->
         <div class="card shadow mb-5 rounded border-0">
           <div
             class="card-header text-white border-0"
             style="background-color: #2f98d4;"
           >
             <div class="row row-cols-auto">
               <div class="col my-auto">
                 <img
                   class="tweet-profile-img my-auto"
                   alt="john-doe"
                   src="https://icon-library.com/images/generic-user-icon/generic-user-icon-19.jpg"
                 />
               </div>
               <div class="col my-auto">
                 <!-- Name -->
                 <h4 class="my-auto">John Doe</h4>
                 <!-- End Name -->
                 <!-- Username -->
                 <span>@johnDoe</span>
                 <!-- End Username -->
               </div>
             </div>
           </div>
           <div class="card-body">
             <p class="card-text text-wrap">
               <!-- Date Created -->
               <span class="text-muted timestamp">
                 Posted at 2017-09-01 18:39:43
               </span>
               <!-- End Date Created -->
               <br />
               <!-- Message -->
               Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
               eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
               enim ad minim veniam, quis nostrud exercitation ullamco laboris
               nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
               reprehenderit in voluptate velit esse cillum dolore eu fugiat
               nulla pariatur. Excepteur sint occaecat cupidatat non proident,
               sunt in culpa qui officia deserunt mollit anim id est laborum.
               <!-- End Message -->
             </p>
             <br />
             <!-- User only -->
             <div class="pull-right row row-cols-auto">
               <div class="col">
                 <!-- Edit -->
                 <a href="#" style="background: none; border: none;">
                   <i
                     class="iconBtn fa fa-pencil-square-o fa-3"
                     aria-hidden="true"
                   ></i>
                 </a>
                 <!-- End Edit -->
               </div>
               <div class="col">
                 <!-- Delete -->
                 <form>
                   <button
                     type="submit"
                     style="background: none; border: none;"
                   >
                     <i
                       class="iconBtn fa fa-trash-o fa-3"
                       aria-hidden="true"
                     ></i>
                   </button>
                 </form>
                 <!-- End Delete -->
               </div>
             </div>
             <!-- End User only -->
           </div>
         </div>
         <!-- End Cards -->
       </div>
     </div>
   </div>
   {% endblock %}
   ```

   _twitterclone/static/css/index.css_

   ```css
   .allTweets {
     margin-top: 1rem;
     margin-bottom: 1rem;
   }

   .tweet-profile-img {
     width: 2.5rem;
     border-radius: 50%;
   }

   .card-body p {
     margin: 1rem;
   }

   textarea {
     height: 8rem;
     min-height: 8rem;
     max-height: 8rem;
     resize: none;
   }

   .timestamp {
     font-size: small;
   }
   ```

3. Bind the `all-tweets.html` template to the _AllTweets_ view by updating the `get` function. This will be a static page for now. Simply follow the code below:

   _twitterclone/tweets/views.py_

   ```python
   from django.shortcuts import render
   from django.views import View
   from django.http import HttpResponse

   # Create your views here.


   class AllTweets(View):
      def get(self, request, *args, **kwargs):
         return render(request, template_name='tweets/all-tweets.html', context={}) # This is the updated line.

      def post(self, request, *args, **kwargs):
         pass

   ```

4. To save the "tweets", a dedicated tweets table must be created in the database. This table needs a foreign key coming from the profile table to identify which profile created each tweet. Create the Tweet model by following the code below:<br>
   _twitterclone/tweets/models.py_

   ```python
   from django.db import models
   from accounts.models import Profile

   # Create your models here.

   class Tweet(models.Model):
     user = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
     msg = models.TextField()
     date_created = models.DateTimeField(auto_now_add=True, null=True)

     def __str__(self):
       return self.msg
   ```

5. To fully create the model, run the command below to make the migration.
   ```bash
   (twtclone)$ python manage.py makemigrations
   ```
6. Afterwards, run the migrate command again to fully construct the changes to the database.

   ```bash
   (twtclone)$ python manage.py migrate
   ```

7. Open the `admin.py` file of the _tweets_ app and add the following lines of code:

   ```python
   from .models import * # imports all models in tweets app

   admin.site.register(Tweet)
   ```

8. You may now check that a new table was added by visiting the Admin Panel at http://127.0.0.1:8000/admin.

   ```bash
   (twtclone)$ python manage.py runserver
   ```

9. Inside the admin panel, for now, add some entries on profiles and tweets. This will be our test entries for displaying database entries in our _AllTweets_ view.

10. Modify the `get` method for the _AllTweets_ view and add the following lines to issue a query on the database acquring all entries in the tweets table sorted by latest to oldest.

    ```python
    def get(self, request, *args, **kwargs):
      tweets = Tweet.objects.all().order_by('-date_created')
      return render(request, template_name='tweets/all-tweets.html', context={'tweets':tweets})
    ```

11. To make our template dynamic we will have to modify its content. This can be done using **Jinja** templates to render the output of our _Python_ code inside the HTML file. Using a for loop, all entries from the _tweets_ object will be displayed. You may update the contents of your `all-tweets.html` to the one below ().

    ```html
    {% extends 'tweets/base.html' %} {% load static %} {% block title %} Twitter
    Clone | Tweets {% endblock %} {% block content %}
    <style>
      .tweetBtn {
        font-size: 80%;
        border-radius: 5rem;
        letter-spacing: 0.1rem;
        font-weight: bold;
        padding: 0.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
        transition: all 0.2s;
        background-color: #2f98d4;
        color: white;
      }

      .tweetBtn:hover {
        background-color: #2473a0;
      }

      .iconBtn {
        color: rgb(81, 91, 102);
        font-size: large;
        font-weight: 1000;
      }

      .iconBtn:hover {
        color: #2f98d4;
      }
    </style>
    <div class="container allTweets">
      <div>
        <div class="card shadow mb-5 rounded border-0">
          <div class="card-header">
            <!-- Name Header -->
            <h2 class="card-title">Good day John Doe, post a tweet!</h2>
            <!-- End Name Header -->
          </div>
          <div class="card-body">
            <form>
              <div class="form-group">
                <!-- Tweet -->
                <textarea
                  required
                  name="tweet"
                  placeholder="What's on your mind?"
                  class="form-control"
                  id="createTweet"
                  rows="3"
                ></textarea>
                <!-- End Tweet -->
              </div>
              <br />
              <div class="pull-right">
                <button type="submit" class="btn text-white tweetBtn">
                  Tweet
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <br />
      <div>
        <h1>Checkout the latest Tweets!</h1>
        <div class="container">
          <!-- Cards -->
          {% for tweet in tweets %}
          <div class="card shadow mb-5 rounded border-0">
            <div
              class="card-header text-white border-0"
              style="background-color: #2f98d4;"
            >
              <div class="row row-cols-auto">
                <div class="col my-auto">
                  <img
                    class="tweet-profile-img my-auto"
                    alt="john-doe"
                    src="https://icon-library.com/images/generic-user-icon/generic-user-icon-19.jpg"
                  />
                </div>
                <div class="col my-auto">
                  <!-- Name -->
                  <h4 class="my-auto">
                    {{ tweet.user.first_name }} {{ tweet.user.last_name }}
                  </h4>
                  <!-- End Name -->
                  <!-- Username -->
                  <span>@{{ tweet.user.username }}</span>
                  <!-- End Username -->
                </div>
              </div>
            </div>
            <div class="card-body">
              <p class="card-text text-wrap">
                <!-- Date Created -->
                <span class="text-muted timestamp"
                  >{{ tweet.date_created }}</span
                >
                <!-- End Date Created -->
                <br />
                <!-- Message -->
                {{ tweet.msg }}
                <!-- End Message -->
              </p>
              <br />
              <!-- User only -->
              <div class="pull-right row row-cols-auto">
                <div class="col">
                  <!-- Edit -->
                  <a href="#" style="background: none; border: none;">
                    <i
                      class="iconBtn fa fa-pencil-square-o fa-3"
                      aria-hidden="true"
                    ></i>
                  </a>
                  <!-- End Edit -->
                </div>
                <div class="col">
                  <!-- Delete -->
                  <form>
                    <button
                      type="submit"
                      style="background: none; border: none;"
                    >
                      <i
                        class="iconBtn fa fa-trash-o fa-3"
                        aria-hidden="true"
                      ></i>
                    </button>
                  </form>
                  <!-- End Delete -->
                </div>
              </div>
              <!-- End User only -->
            </div>
          </div>
          {% endfor %}
          <!-- End Cards -->
        </div>
      </div>
    </div>
    {% endblock %}
    ```

12. You may view the updated page at http://127.0.0.1:8000/all-tweets. We will leave this for now as we will create the other functionalities to make the page fully useable.

    ```bash
    (twtclone)$ python manage.py runserver
    ```

    <br>

# Creating an account registration page

In **Django**, we have the option to manually handle theregistration of accounts in our database or integrate them via forms. In this section, we will be using the combination of both to register a user with an account in the built in **Django** user data base and integrate it with manual entries to a dedicated profile table.

1.  In the _accounts_ app, create a preliminary view for the registration page with a post and get method and bind it to a specific URL pattern. Add an HTML template as well. You may simply follow the code for each file below.<br>

    _twitterclone/accounts/views.py_

    ```python
    class Register(View):
      def get(self, request, *args, **kwargs):
        return render(request, template_name='accounts/register.html')

      def post(self, request, *args, **kwargs):
        pass
    ```

    _twitterclone/accounts/urls.py_

    ```python
    urlpatterns = [
     path('', views.Login.as_view(), name='login'),
     path('register/', views.Register.as_view(), name='register'),
    ]
    ```

    _twitterclone/accounts/templates/accounts/register.html_

    ```html
    {% extends 'accounts/base.html' %} {% load static %} {% block title %}
    Twitter Clone | Register {% endblock %} {% block content %}
    <div>
      <h1>Register</h1>
    </div>
    {% endblock %}
    ```

2.  Proceed on creating a `forms.py` inside the _accounts_ app directory (`twitterclone/accounts/`). This will create a form that we can use as inputs for our frontend. You may simply copy the code below.<br>

    ```python
     from django.forms import ModelForm
     from django.contrib.auth.forms import UserCreationForm
     from django.contrib.auth.models import User


     class CreateUserForm(UserCreationForm):
         class Meta:
             model = User
             fields = ['first_name', 'last_name', 'username',
                       'email', 'password1', 'password2']

         def __init__(self, *args, **kwargs):
             super(CreateUserForm, self).__init__(*args, **kwargs)
             self.fields['first_name'].widget.attrs.update(
                 {'class': 'form-control', 'placeholder': 'First Name'})
             self.fields['last_name'].widget.attrs.update(
                 {'class': 'form-control', 'placeholder': 'Last Name'})
             self.fields['username'].widget.attrs.update(
                 {'class': 'form-control', 'placeholder': 'Username'})
             self.fields['email'].widget.attrs.update(
                 {'class': 'form-control', 'placeholder': 'Email'})
             self.fields['password1'].widget.attrs.update(
                 {'class': 'form-control', 'placeholder': 'Password'})
             self.fields['password2'].widget.attrs.update(
                 {'class': 'form-control', 'placeholder': 'Confirm Password'})

    ```

    Your updated local directory structure should look similar to this.

    ```
    twitter-clone/
    |__ accounts/
    |   |__ __pycache__/
    |   |__ migrations/
    |   |__ accounts/
    |   |   |__ templates/
    |   |       |__ base.html
    |   |       |__ login.html
    |   |       |__ register.html
    |   |__ __init__.py
    |   |__ admin.py
    |   |__ apps.py
    |   |__ forms.py
    |   |__ models.py
    |   |__ tests.py
    |   |__ urls.py
    |   |__ views.py
    |__ static/
    |   |__ css/
    |   |   |__ index.css
    |   |__ img/
    |   |__ js/
    |__ tweets/
    |   |__ __pycache__/
    |   |__ migrations/
    |   |__ tweets/
    |   |   |__ templates/
    |   |       |__ all-tweets.html
    |   |       |__ base.html
    |   |__ __init__.py
    |   |__ admin.py
    |   |__ apps.py
    |   |__ models.py
    |   |__ tests.py
    |   |__ urls.py
    |   |__ views.py
    |__ twitter-clone/
    |   |__ __pycache__/
    |   |__ __init__.py
    |   |__ .env
    |   |__ asgi.py
    |   |__ settings.py
    |   |__ urls.py
    |   |__ wsgi.py
    |__ .gitignore
    |__ db.sqlite3
    |__ manage.py
    ```

3.  Update the _Profile_ model as well to create a one is to one connection with the profile and user. You may follow the updated code below: <br>

    _twitterclone/accounts/models.py_

    ```python
    from django.db import models
    from django.contrib.auth.models import User

    # Create your models here.


    class Profile(models.Model):
        user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
        first_name = models.CharField(max_length=200, null=True)
        last_name = models.CharField(max_length=200, null=True)
        username = models.CharField(max_length=200, null=True)
        email = models.CharField(max_length=200, null=True)
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
            return self.email

    ```

4.  Proceed on running the migrations to update the database information.

    ```bash
    (twtclone)$ python manage.py makemigrations
    (twtclone)$ python manage.py migrate
    ```

5.  Import `forms.py` inside `views.py` and update the get and post method of the _Register_ view to reference the created form. <br>

    ```python
    from django.shortcuts import render, redirect # Add redirect to the imports
    ...
    from .forms import CreateUserForm
    from .models import *
    from django.contrib import messages

    ...

    class Register(View):
       def get(self, request, *args, **kwargs):
          form = CreateUserForm()
          return render(request, template_name='accounts/register.html', context={'form': form})

       def post(self, request, *args, **kwargs):
          form = CreateUserForm(request.POST)

          if form.is_valid():
              user = form.save()
              first_name = form.cleaned_data['first_name']
              last_name = form.cleaned_data['last_name']
              username = form.cleaned_data['username']
              email = form.cleaned_data['email']

              profile = Profile(user=user, first_name=first_name,
                                last_name=last_name, email=email, username=username)
              profile.save()
              return redirect('/registration-success/') # Notice that this path, nor its template is still not created. This will be craeted later on.
          else:
              messages.error(request, 'There was an error.')
          return render(request, template_name='accounts/register.html', context={'form': form})
    ```

6.  This time as well, update the `register.html` file to integrate the form in the frontend. You may copy the updated content of the file below. Update the `index.css` file as well to fully incorporate the updated design.<br>

    _twitterclone/accounts/templates/register.html_

    ```html
    {% extends 'accounts/base.html' %} {% load static %} {% block title %}
    Twitter Clone | Register {% endblock %} {% block content %}
    <div>
      <div class="container">
        <div class="row">
          <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
            <div class="card card-signin my-5">
              <div class="card-body">
                <h3 class="text-center">Sign up an account</h3>
                <br />
                <!-- This form is assigned with a method of post request since it is meant to send a data/payload to the backend  -->
                <form class="form-signin" method="POST">
                  {% csrf_token %}
                  <!-- Declaring a CSRF Token is required for post requests in Django forms -->

                  <div class="form-label-group">
                    <div class="row">
                      <div class="col form-label-group">
                        {{ form.first_name }}
                        <label for="id_first_name">First Name</label>
                      </div>
                      <div class="col form-label-group">
                        {{ form.last_name }}
                        <label for="id_last_name">Last Name</label>
                      </div>
                    </div>

                    <div class="row">
                      <div class="form-label-group">
                        {{ form.email }}
                        <label for="id_email">Email</label>
                      </div>
                    </div>

                    <div class="row">
                      <div class="form-label-group">
                        {{ form.username }}
                        <label for="id_username">Username</label>
                      </div>
                    </div>

                    <div class="row">
                      <div class="form-label-group">
                        {{ form.password1 }}
                        <label for="id_password1">Password</label>
                      </div>
                    </div>

                    <div class="row">
                      <div class="form-label-group">
                        {{ form.password2 }}
                        <label for="id_password2">Confirm Password</label>
                      </div>
                    </div>

                    <script>
                      var password = document.getElementById("id_password1"),
                        confirm_password =
                          document.getElementById("id_password2");

                      function validatePassword() {
                        if (password.value != confirm_password.value) {
                          confirm_password.setCustomValidity(
                            "Passwords Don't Match"
                          );
                        } else {
                          confirm_password.setCustomValidity("");
                        }
                      }

                      password.onchange = validatePassword;
                      confirm_password.onkeyup = validatePassword;
                    </script>
                  </div>

                  <button
                    name="Create User"
                    class="btn text-uppercase"
                    type="submit"
                    style="width: 100%;"
                  >
                    Sign Up
                  </button>
                  <hr class="my-4" />
                  <p class="text-center">
                    Already have an account?
                    <a href="{% url 'login' %}" style="text-decoration: none;"
                      >Login</a
                    >
                  </p>
                  {% for message in messages %} {% if form.errors %} {% for
                  field in form %} {% for error in field.errors %}
                  <div class="alert alert-danger">
                    <strong>{{ error|escape }}</strong>
                  </div>
                  {% endfor %} {% endfor %} {% for error in
                  form.non_field_errors %}
                  <div class="alert alert-danger">
                    <strong>{{ error|escape }}</strong>
                  </div>
                  {% endfor %} {% endif %} {% endfor %}
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    {% endblock %}
    ```

    _twitterclone/static/css/index.css_

    ```css
    :root {
      --input-padding-x: 1.5rem;
      --input-padding-y: 0.75rem;
    }

    .card-signin {
      border: 0;
      border-radius: 0rem;
      box-shadow: 0 0.5rem 1rem 0 rgba(0, 0, 0, 0.1);
    }

    .card-signin .card-title {
      margin-bottom: 2rem;
      font-weight: 300;
      font-size: 1.5rem;
    }

    .card-signin .card-body {
      padding: 2rem;
    }

    .form-signin {
      width: 100%;
    }

    .form-signin .btn {
      font-size: 80%;
      border-radius: 5rem;
      letter-spacing: 0.1rem;
      font-weight: bold;
      padding: 1rem;
      transition: all 0.2s;
      background-color: #2f98d4;
      color: white;
    }

    .form-signin .btn:hover {
      background-color: #2473a0;
    }

    .form-label-group {
      position: relative;
      margin-bottom: 1rem;
    }

    .form-label-group input {
      height: auto;
      border-radius: 0.5rem;
    }

    .form-label-group > input,
    .form-label-group > label {
      padding: var(--input-padding-y) var(--input-padding-x);
    }

    .form-label-group > label {
      position: absolute;
      top: 0;
      left: 0;
      display: block;
      width: 100%;
      margin-bottom: 0;
      /* Override default `<label>` margin */
      line-height: 1.5;
      color: #495057;
      border: 1px solid transparent;
      border-radius: 0.25rem;
      transition: all 0.1s ease-in-out;
    }

    .form-label-group input::-webkit-input-placeholder {
      color: transparent;
    }

    .form-label-group input:-ms-input-placeholder {
      color: transparent;
    }

    .form-label-group input::-ms-input-placeholder {
      color: transparent;
    }

    .form-label-group input::-moz-placeholder {
      color: transparent;
    }

    .form-label-group input::placeholder {
      color: transparent;
    }

    .form-label-group input:not(:placeholder-shown) {
      padding-top: calc(
        var(--input-padding-y) + var(--input-padding-y) * (2 / 3)
      );
      padding-bottom: calc(var(--input-padding-y) / 3);
    }

    .form-label-group input:not(:placeholder-shown) ~ label {
      padding-top: calc(var(--input-padding-y) / 3);
      padding-bottom: calc(var(--input-padding-y) / 3);
      font-size: 12px;
      color: #777;
    }

    /* Fallback for Edge
                -------------------------------------------------- */

    @supports (-ms-ime-align: auto) {
      .form-label-group > label {
        display: none;
      }
      .form-label-group input::-ms-input-placeholder {
        color: #777;
      }
    }

    /* Fallback for IE
                -------------------------------------------------- */

    @media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
      .form-label-group > label {
        display: none;
      }
      .form-label-group input:-ms-input-placeholder {
        color: #777;
      }
    }
    ```

7.  This time, we will create a dedicated page for to confirm successful registration. Proceed on adding a view, URL path, and creating template for this page named `registration-success.html` by following the code below.<br>

    _twitterclone/accounts/views.py_

    ```python
    class RegistrationSuccess(View):
      def get(self, request, *args, **kwargs):
          return render(request, template_name='accounts/registration-success.html', context={})
    ```

    _twitterclone/accounts/urls.py_

    ```python
    urlpatterns = [
        path('', views.Login.as_view(), name='login'),
        path('register/', views.Register.as_view(), name='register'),
        path('registration-success/', views.RegistrationSuccess.as_view(), name='registration-success'),
    ]
    ```

    _twitterclone/accounts/templates/accounts/registration-success.html_

    ```html
    {% extends 'accounts/base.html' %} {% load static %} {% block title %}
    Twitter Clone | Registration Successful {% endblock %} {% block content %}
    <div>
      <div class="container">
        <div class="row">
          <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
            <div class="card card-signin my-5">
              <div class="card-body">
                <h3 class="text-center">Registration Successful!</h3>
                <br />

                <p class="text-center">
                  You have successfully registered an account. You may now
                  proceed on logging in.
                </p>

                <a
                  name="Create User"
                  class="btn text-uppercase text-white bg-info"
                  href="{% url 'login' %}"
                  style="width: 100%;"
                  ><b>LOGIN</b></a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    {% endblock %}
    ```

    ```
    twitter-clone/
    |__ accounts/
    |   |__ __pycache__/
    |   |__ migrations/
    |   |__ accounts/
    |   |   |__ templates/
    |   |       |__ base.html
    |   |       |__ login.html
    |   |       |__ register.html
    |   |       |__ registration-success.html
    |   |__ __init__.py
    |   |__ admin.py
    |   |__ apps.py
    |   |__ forms.py
    |   |__ models.py
    |   |__ tests.py
    |   |__ urls.py
    |   |__ views.py
    |__ static/
    |   |__ css/
    |       |__ index.css
    |   |__ img/
    |   |__ js/
    |__ tweets/
    |   |__ __pycache__/
    |   |__ migrations/
    |   |__ tweets/
    |   |   |__ templates/
    |   |       |__ all-tweets.html
    |   |       |__ base.html
    |   |__ __init__.py
    |   |__ admin.py
    |   |__ apps.py
    |   |__ models.py
    |   |__ tests.py
    |   |__ urls.py
    |   |__ views.py
    |__ twitter-clone/
    |   |__ __pycache__/
    |   |__ __init__.py
    |   |__ .env
    |   |__ asgi.py
    |   |__ settings.py
    |   |__ urls.py
    |   |__ wsgi.py
    |__ .gitignore
    |__ db.sqlite3
    |__ manage.py
    ```

8.  You may now check if the registration is working properly by monitoring the entries in the profile and users table from the Admin Panel.

    ```bash
    (twtclone)$ python manage.py runserver
    ```

    <br>

# Creating a functional login page with proper redirection and decorators.

Now that user registration has been created, it is time to discuss how these users will be able to access the pages of the application through login. In this section, we will implement the use of serializers as well to restrict access to certain pages inline with the the use of _Jinja_ templates to dynamically make changes to the page based on user authentication.

1. Proceed on modifying the post method of the _Login_ view from the _accounts_ app. Firstly, import the **Django** authentication library and import the built in `login` function. We will create the view in such a way that if the user that login is a superuser, he/she will be redirected to the page of the admin panel (`/admin`). Otherwise, regular users will be redirected to the all tweets page (`tweets/all-tweets`). You may follow the updated code below. <br>

   _twitterclone/accounts/views.py_

   ```python
   from django.contrib.auth import authenticate, login

   ...

   class Login(View):
      def get(self, request, *args, **kwargs):
          return render(request, template_name='accounts/login.html', context={})

      def post(self, request, *args, **kwargs):
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request, username=username, password=password)
          if user is not None:
              login(request, user)
              if user.is_superuser:
                  return redirect('/admin')
              else:
                  return redirect('/tweets/all-tweets')
          else:
              messages.info(request, 'Username or Password is incorrect.')
          return render(request, template_name='accounts/login.html', context={})
   ```

2. We will now proceed on binding functionalities set in this view to the login template. To do so, you may follow the updated code below. This login page shares the same _CSS_ code with the register page along with a couple of intext and inline styling. Hence all you need is to update the `login.html` file and the `base/html` file from the _accounts_ app templates .<br>

   _twitterclone/accounts/templates/accounts/login.html_

   ```html
   {% extends 'accounts/base.html' %} {% load static %} {% block title %}
   Twitter Clone | Login {% endblock %} {% block content %}
   <style>
     .nounderline {
       color: rgb(105, 199, 236);
       text-decoration: none;
     }

     .nounderline:hover {
       color: rgb(117, 235, 235);
       text-decoration: underline;
     }

     .signin {
       display: block;
     }

     @media (max-width: 480px) {
       .signin {
         margin: 0;
         display: flex;
         justify-content: center;
         width: 100%;
       }
     }
   </style>

   <div class="container-fluid mb-5">
     <div class="row p-3 mt-5 justify-content-md-center">
       <h2 class="text-white">
         Welcome to Twitter<span class="brand">CLONE</span>!
       </h2>
     </div>
     <div class="row container-fluid mb-0 justify-content-md-center">
       <div class="col col-lg-7 container-fluid">
         <div class="my-5 p-4">
           <p class="text-white">
             This is Twitter<span class="brand">CLONE</span>, a simple Twitter
             clone made using <i>Django</i> framework in <i>Python</i>.
           </p>
           <p class="text-white">
             This web application is part of a tutorial made by
             <a class="nounderline" href="http://paucabral.github.io"
               >Pau Cabral</a
             >
             on the development of a <i>Django</i> web application, to its
             deployment to <i>Heroku</i>.
           </p>
           <br />
           <br />
           <p class="text-white">
             You may visit this project's repository at
             <a
               style="font-weight: bold;"
               class="nounderline"
               href="https://github.com/paucabral/twitter-clone/"
               >Github</a
             >.
           </p>
         </div>
       </div>

       <div class="col container-fluid ms-auto signin">
         <div class="row justify-content-md-center">
           <div class="col my-auto">
             <div class="card card-signin">
               <div class="card-body">
                 <h3 class="text-center">Sign In</h3>
                 <br />
                 <form class="form-signin" method="POST">
                   {% csrf_token %}
                   <div class="form-label-group">
                     <input
                       type="text"
                       id="username"
                       class="form-control"
                       name="username"
                       placeholder="Username"
                       required
                       autofocus
                     />
                     <label for="username">Username</label>
                   </div>

                   <div class="form-label-group">
                     <input
                       type="password"
                       minlength="8"
                       id="password"
                       class="form-control"
                       name="password"
                       placeholder="Password"
                       required
                     />
                     <label for="password">Password</label>
                   </div>
                   <br />
                   <button
                     class="btn text-uppercase"
                     type="submit"
                     style="width: 100%;"
                   >
                     Sign in
                   </button>
                   <hr class="my-4" />

                   {% for message in messages %}
                   <div class="alert alert-danger">
                     <b class="text-center">{{ message }}</b>
                   </div>
                   {% endfor %}

                   <p class="text-center">
                     Don't have an account?
                     <a
                       href="{% url 'register' %}"
                       style="text-decoration: none;"
                       >Sign Up</a
                     >
                   </p>
                 </form>
               </div>
             </div>
           </div>
         </div>
       </div>
     </div>
   </div>
   {% endblock %}
   ```

   _twitterclone/accounts/templates/accounts/base.html_

   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <meta http-equiv="X-UA-Compatible" content="IE=edge" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <title>{% block title %}{% endblock %}</title>
       <link
         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
         rel="stylesheet"
         integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
         crossorigin="anonymous"
       />
       <link
         rel="stylesheet"
         type="text/css"
         href="{% static 'css/index.css' %}"
       />
       <style>
         .bg {
           background-image: linear-gradient(
               rgba(0, 0, 0, 0.5),
               rgba(0, 0, 0, 0.5)
             ),
             url("https://media.gettyimages.com/photos/blurred-crowd-of-unrecognizable-at-the-street-picture-id1179844008?b=1&k=6&m=1179844008&s=170667a&w=0&h=TgItFSgBEqiSJcjF34G_0ho8936PL_HR0pfC-CuI_jQ=");
           background-repeat: no-repeat;
           background-attachment: fixed;
           background-size: cover;
         }
       </style>
     </head>
     <body class="bg">
       <div class="container">{% block content %} {% endblock %}</div>
     </body>
   </html>
   ```

3. To fully enhance the user experience on the landing page after login (`/tweets/all-tweets`), edit the boilerplate code, `all-tweets.html` in the section that is meant to display name of the user (commented as `<!-- Name Header -->`). This will be done through _Django_'s built-in user identification with login authentication. To do so, simply follow the code below.<br>

   ```html
   ...

   <!-- Name Header -->
   <h2 class="card-title">
     Good day {% if user.profile.first_name|length > 0 %} {{
     user.profile.first_name }} {{ user.profile.last_name }}, {% else %} {{
     user.username }}, {% endif %}post a tweet!
   </h2>
   <!-- End Name Header -->

   ...
   ```

4. We can now proceed on creating a simple view for logging out users. This will be done by ending their session through _Django_'s built-in `logout` function from its _authentication_ library. Proceed on adding the view in the _accounts_ app, creating a corresponding URL path for it, and binding the dedicated logout button from the navigation bar, found in the `base.html` template in the _tweets_ app.<br>

   _twitterclone/accounts/views.py_

   ```python
    ...

    from django.contrib.auth import authenticate, login, logout # Add logout to the updated imports

    ...

    # Note: This function is not part of any class. This is a sole function view.
    def logoutUser(request):
      logout(request)
      return redirect('/')

   ```

   _twitterclone/accounts/urls.py_

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
     path('', views.Login.as_view(), name='login'),
     path('register/', views.Register.as_view(), name='register'),
     path('registration-success/', views.RegistrationSuccess.as_view(), name='registration-success'),
     path('logout/', views.logoutUser, name='logout'), # Since the view is not a class, it is not invoked with the .as_view() method.
   ]
   ```

   _twitterclone/tweets/templates/tweets/base.html_

   ```html
   ...
   <li class="nav-item">
     <a class="nav-link menuItem" href="/logout">
       <!-- The href is set to the absolute path for logout view -->
       <i class="fa fa-sign-out fa-3" aria-hidden="true"></i> Logout
     </a>
   </li>
   ...
   ```

5. While the application can now identify which user is logged in, all pages are still exposed simply by typing the exact URL. For instance, you should notice that you are still able to access `/tweets/all-tweets` despite being logged out just by going directly to http://127.0.0.1:8000/tweets/all-tweets. We can use _Django_'s built-in decorator to impose login as a requirement in order to view or send requests to certain pages. Moreover, we can also implement our own by creating a custom decorator if needed. This will be applied on each view where login is required. Proceed on importing the `login_required` decorator and add it to the methods of the _AllTweets_ view in the _tweets_ app, and the _logoutUser_ view in the _accounts_ app, with the login path (`/`) as the parameter for redirection in case the user is not logged in. You may follow the code below.<br>

   _twitterclone/tweets/views.py_

   ```python
    ...

    from django.contrib.auth.decorators import login_required
    from django.utils.decorators import method_decorator

    ...

    class AllTweets(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        tweets = Tweet.objects.all().order_by('-date_created')
        return render(request, template_name='tweets/all-tweets.html', context={'tweets': tweets})

    @method_decorator(login_required(login_url='/'))
    def post(self, request, *args, **kwargs):
        pass
   ```

   _twitterclone/accounts/views.py_

   ```python
   ...

   from django.contrib.auth.decorators import login_required

   ...

   @login_required(login_url='/') # Add it just above the view.
   def logoutUser(request):
       logout(request)
      return redirect('/')

   ```

   _Note: Class based views require an additional import of method decorator. Refer to the implementation in the AllTweets view._
   <br>

6. The functionalities should now be properly applied. Going directly to http://127.0.0.1:8000/tweets/all-tweets should result to automatic redirection to the login page if the user is not authenticated.<br>

   ```bash
   (twtclone)$ python manage.py runserver
   ```

   <br>

# Fully functional _AllTweets_ view

In this section, we will go back on building the functionalities of the _AllTweets_ view. We are now going to implement proper form submission to "post a tweet" and add the other functionalities as well such as the option to edit or delete a user-owned 'tweet'. This will now be a fully functional (create, read, update, delete) CRUD page.

1. Start by updating the _AllTweets_ view. This time around, we will be grabbing the information from the post request without the aid of using forms. We are going to get the current user profile associated to the tweet by extracting it with the request from the currently logged in user. Moreover, the field for the tweet will be added by capturing the field specified by its `name` attribute after submit (notice the `<textarea>` has an attribute `name` with a value of `tweet` in `all-tweets.html`). You may simply copy the code below. You may run the project and check the functionality afterwards.<br>

   _twitterclone/tweets/views.py_

   ```python
    from django.shortcuts import render, redirect # Add redirect among the list of imports

    ...

    class AllTweets(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        tweets = Tweet.objects.all().order_by('-date_created')
        return render(request, template_name='tweets/all-tweets.html', context={'tweets': tweets})

    @method_decorator(login_required(login_url='/'))
    def post(self, request, *args, **kwargs): # Update the post method with the following lines of code
        user = request.user.profile # Checks the user from the request and associate the profile as defined in the model
        msg = request.POST.get('tweet') # Gets the form from the request and extracts the data from an input with an attribute "name" which value is "tweet"
        tweet = Tweet(user=user, msg=msg) # Set the parameters for new entry in the Tweet model
        tweet.save() # Save the tweet
        return redirect('/tweets/all-tweets')
   ```

   _twitterclone/tweets/templates/tweets/all-tweets.py_

   ```html
   <!-- Add method attribute as "POST" -->
   <form method="POST">
     <!-- Make sure to define CSRF Token -->
     {% csrf_token %}
     <div class="form-group">
       <!-- Tweet -->
       <textarea
         required
         name="tweet"
         placeholder="What's on your mind?"
         class="form-control"
         id="createTweet"
         rows="3"
       ></textarea>
       <!-- End Tweet -->
     </div>
     <br />
     <div class="pull-right">
       <button type="submit" class="btn text-white tweetBtn">Tweet</button>
     </div>
   </form>
   ```

2. Next is setting up when the edit and delete button should appear in the page. The user must only be able to edit and delete the tweet he/she created. As such, we have to modify the part of the code in `all-tweets.html` template (check the part with a comment indicating `User only`) with a condition that checks if the assigned user profile to the tweet is the same user that is currently logged in. Do this by simply adding the conditions via _Jinja_ tempaltes. You may simply follow the code below. <br>

   ```html
   <!-- User only -->
   {% if tweet.user.id == user.profile.user.id %}
   <div class="pull-right row row-cols-auto">
     <div class="col">
       <!-- Edit -->
       <a href="#" style="background: none; border: none;">
         <i class="iconBtn fa fa-pencil-square-o fa-3" aria-hidden="true"></i>
       </a>
       <!-- End Edit -->
     </div>
     <div class="col">
       <!-- Delete -->
       <form>
         <button type="submit" style="background: none; border: none;">
           <i class="iconBtn fa fa-trash-o fa-3" aria-hidden="true"></i>
         </button>
       </form>
       <!-- End Delete -->
     </div>
   </div>
   {% else %}
   <br />
   {% endif %}
   <!-- End User only -->
   ```

3. To delete a 'tweet', each delete button must be assigned with a unique value that is equal to the ID of the 'tweet'. This way, a query to delete that entry would be possible. A new view with a dynamic URL path have to be created as well that will handle the specified endpoint with the form of the delete button to avoid conflict with the the previous form. You may follow the updated code for the files below.<br>

   _twitterclone/tweets/views.py_

   ```python
   @login_required(login_url='/')
   def deleteTweet(request, id): # The view expects to receive parameter of 'id' with the request
       if request.method == "POST":
           tweet = id # The paramater from the request is stored
           tweet_instance = Tweet.objects.filter(id=tweet) # The parameter was used to locate the entry from the database
           tweet_instance.delete() # The entry was deleted
       return redirect('/tweets/all-tweets')
   ```

   _Note: This view does is not part of any class. This is a simple functional view._<br>

   _twitterclone/tweets/views.py_

   ```python
    urlpatterns = [
        path('all-tweets', views.AllTweets.as_view(), name='all-tweets'),
        path('delete-tweet/<id>', views.deleteTweet, name='delete-tweet'), # Added this new URL path. Enclose in tags is 'id' which is a dynamic element. This is to specify to the delete endpoint a specific id as parameter.
    ]
   ```

   _twitterclone/tweets/templates/all-tweets.html_

   ```html
   <!-- Delete -->
   <!-- Specified method as POST with a defined endpoint with action attribute. This leads to the delete-tweet URL (/tweets/delete-tweet/<id>) with a specified parameter of tweet.id -->
   <form method="POST" action="{% url 'delete-tweet' tweet.id  %}">
     <!-- Like the previous forms, do not forget to include the CSRF Token declaration-->
     {% csrf_token %}
     <button
       name="deletetweet"
       value="{{ tweet.id }}"
       type="submit"
       style="background: none; border: none;"
     >
       <i class="iconBtn fa fa-trash-o fa-3" aria-hidden="true"></i>
     </button>
   </form>
   <!-- End Delete -->
   ```

4. While the delete functionality is working properly now, it is not ideal to allow users do such operations with any warning. We can use the `onsubmit` attribute of forms to display a simple alert message using an inline _Javascript_. To do this, simply update the opening tag of the form for delete button, the same as the code below.<br>

   _twitterclone/tweets/templates/all-tweets.html_

   ```html
   <!-- Notice the onsubmit attribute invokes an alert dialouge to confirm if the action is to be continued. -->
   <form
     onsubmit="return confirm('Are you sure you want to delete the tweet: {{ tweet.msg }} ?');"
     method="POST"
     action="{% url 'delete-tweet' tweet.id  %}"
   >
     {% csrf_token %}
     <button
       name="deletetweet"
       value="{{ tweet.id }}"
       type="submit"
       style="background: none; border: none;"
     >
       <i class="iconBtn fa fa-trash-o fa-3" aria-hidden="true"></i>
     </button>
   </form>
   ```
