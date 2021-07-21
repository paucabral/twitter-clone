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
   Note: After exiting your terminal, the virtual environment would naturally be deactivated upon your next launch or another spawn of terminal. You do not need to recreate the virtual environment every project. To use the created virtual environment again, you may use the following command:\_
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

3. One great feature of **Django** is the ability to set a base template which can be inherited by other inherited HTML files. This way, particular HTML code can be reused (i.e. for headers, navbar, footers, etc.). For now, we will create a `base.html` as template all the HTML files in our _accounts_ app. Create a `base.html` file inside the `twitterclone/accounts/templates/accounts` directory. We may import within it an external CSS library as well like bootstrap. In the mean time, add the following contents inside:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
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
   h1 {
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

7. Import the `index.css` file in the `base.html` file by adding the `{% load static %}` invocation and referencing it with the `<link>` tag. You may follow the updated `base.html` code below:
   ```html
   {% load static %}
   <!-- Initiate loading of static files -->
   <!DOCTYPE html>
   <html lang="en">
     <head>
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
         src="{% static 'css/index.css' %}"
       />
       <!-- Import the created CSS file -->
     </head>
     <body>
       <div class="container">{% block content %} {% endblock %}</div>
     </body>
   </html>
   ```
8. This time, let's create a dedicated HTML file which we will bind for the _Login_ view. We will be extending the contents of `base.html` to this file so that the we do not have to rewrite the code we have written inside the `base.html`. Create `login.html` inside the accounts template directory (`twitterclone/accounts/templates/accounts/`).<br>

   _twitterclone/accounts/templates/accounts/login.html_

   ```html
   {% extends 'accounts/base.html' %} {% load static %} {% block title %}
   Twitter Clone | Login {% endblock %} {% block content %}
   <div>
     <h1>Welcome to the login page!</h1>
   </div>
   {% endblock %}
   ```

   _Note: The document title is placed in between the block title blocks and the content which was initialized at the `<body>` tag is placed in between the block content blocks._

9. We will now connect this HTML file to the _Login_ view inside the `views.py` of our _accounts_ app. Modify the `get` function and return a render instead. You may simply follow the code below.

   ```python
   from django.shortcuts import render
   from django.views import View
   from django.http import HttpResponse

   # Create your views here.


   class Login(View):
      def get(self, request, *args, **kwargs):
         return render(request, template_name='accounts/login.html', context={})

      def post(self, request, *args, **kwargs):
         pass
   ```

10. Try running the project again and visit the _Login_ page at http://127.0.0.1:8000/. We will update this page and other views for the _accounts_ app towards the latter part of the project.

    ```bash
    (twtclone)$ python manage.py runserver
    ```
