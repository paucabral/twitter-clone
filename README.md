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

# The _tweets_ app

This app is dedicated for viewing and posting tweets. Throughout this section, we will be creating a basic Create, Read, Update, and Delete (CRUD) functionality, and discuss the creation of _models_.

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
   <div class="container allTweets">
     <div>
       <div class="card shadow mb-5 rounded border-0">
         <div class="card-header">
           <h2 class="card-title">Post a tweet</h2>
         </div>
         <div class="card-body">
           <form>
             <div class="form-group">
               <textarea class="form-control" id="createTweet" rows="3">
               </textarea>
             </div>
             <br />
             <div class="pull-right">
               <a href="#" class="btn text-white btn-info">
                 <i class="fa fa-pencil-square fa-3" aria-hidden="true"></i>
                 Tweet
               </a>
             </div>
           </form>
         </div>
       </div>
     </div>
     <br />
     <div>
       <h1>Checkout the latest Tweets!</h1>
       <div class="container">
         <div class="card shadow mb-5 rounded border-0">
           <div class="card-header bg-info text-white border-0">
             <div class="row row-cols-auto">
               <div class="col my-auto">
                 <img
                   class="tweet-profile-img my-auto"
                   alt="john-doe"
                   src="https://abansfinance.lk/wp-content/uploads/2017/08/dummy-user.jpg"
                 />
               </div>
               <div class="col my-auto">
                 <h4 class="my-auto">John Doe</h4>
               </div>
             </div>
           </div>
           <div class="card-body">
             <p class="card-text text-wrap">
               Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
               eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
               enim ad minim veniam, quis nostrud exercitation ullamco laboris
               nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
               reprehenderit in voluptate velit esse cillum dolore eu fugiat
               nulla pariatur. Excepteur sint occaecat cupidatat non proident,
               sunt in culpa qui officia deserunt mollit anim id est laborum.
             </p>

             <div class="pull-right">
               <a href="#" class="btn text-white btn-primary">
                 <i class="fa fa-pencil-square-o fa-3" aria-hidden="true"></i>
               </a>
               <a href="#" class="btn text-white btn-danger">
                 <i class="fa fa-trash-o fa-3" aria-hidden="true"></i>
               </a>
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
   ```

3. Bind the `all-tweets.html` template to the _AllTweets_ view by updating the `get` function. Follow the code below:

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
