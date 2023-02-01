# django-nest-multivendor-compile
Compiling the step-by-step django-nest-multivendor


## 01. SETUP AND CREATE DJANGO PROJECT AND APP


#### 01.1 Setup, create project and app, homepage with urls, views and template inheritance

        modified:   .gitignore
        modified:   README.md
        new file:   app/core/__init__.py
        new file:   app/core/admin.py
        new file:   app/core/apps.py
        new file:   app/core/migrations/__init__.py
        new file:   app/core/models.py
        new file:   app/core/tests.py
        new file:   app/core/urls.py
        new file:   app/core/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   templates/app/core/index.html
        new file:   templates/base.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/header.html
        new file:   templates/partials/modals.html
        new file:   templates/partials/nav-bar.html
        new file:   templates/partials/nav-mobile.html
        new file:   templates/partials/preloader.html
        new file:   templates/partials/quickview.html


## 02. DATABASE


#### 02.1 Create, connect, protect database

        modified:   README.md
        modified:   config/settings.py


## 03. CUSTOM USER MODEL


#### 03.1 Creating userauth app and custom user model called 'User'

        new file:   app/userauth/__init__.py
        new file:   app/userauth/admin.py
        new file:   app/userauth/apps.py
        new file:   app/userauth/migrations/0001_initial.py
        new file:   app/userauth/migrations/__init__.py
        new file:   app/userauth/models.py
        new file:   app/userauth/tests.py
        new file:   app/userauth/views.py
        modified:   config/settings.py


## 04. SETTING UP ADMIN DASHBOARD