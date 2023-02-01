# django-nest-multivendor-compile
Compiling the step-by-step django-nest-multivendor


## 01. SETUP AND CREATE DJANGO PROJECT AND APP


#### 01.1 Setup, create project and app, homepage with urls, views and template inheritance

        11 Template inheritance
        10 Add and loading static files
        9 Setting up static and media files
        8 Add html template to index
        7 Hello Wordl using url, view and templates
        6 Register core app to config/settings.py, run the server
        5 Create a new app: app/core
        4 Create new project named config
        3 Activate venv3932, install django==3.2, and upgrade pip
        2 Create virtual environment
        1 Create a new Github repository
        ea38bde - I Nyoman Gurnitha : Initial commit

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

        3 Protecting project configuration files
        2 Create and connect database with the project
        1 Install psycopg2 driver: pip install psycopg2

        modified:   README.md
        modified:   config/settings.py


## 03. CUSTOM USER MODEL


#### 03.1 Creating userauth app and custom user model called 'User'

        8 Register your models here.
        7 Register User model to admin.py
        6 Create superuser, run server and login to admin
        5 Run makemigrations and migrate and runserver
        4 Add AUTH_USER_MODEL = 'userauth.User' in config/settings.py
        3 Create custom class User(AbstractUser): in userauth/models.py
        2 Register userauth app to config/settings.py
        1 Create a new app: app/userauth

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


#### 04.1 Install and configuring jazzmin for admin dashboard

        3 Configuring jazzmin for its look in admin panel
        2 Add jazzmin in config/INSTALLED_APPS and re-run the server
        1 Install django-jazzmin: pip install -U django-jazzmin

        modified:   config/settings.py


## 05. USER REGISTRATION SYSTEM


#### 05.1 Creating user registration system

        8 Configure the register page - showing error messages to register page
        7 Configure the register page - add widget in forms.py and use it in the regiter page
        6 Configure the register page-delete form inpu
        5 Add template to register page and renamed sign-up and sign-in files
        4 Redirect signed up user to login page
        3 Use UserRegisterForm in register_view method to register a new user
        2 Create form class UserRegisterForm (UserCreationForm) in: app/userauth/forms.py and reder its instances to sign-up page
        1 Create register_view method to render sign-up page

        modified:   README.md
        new file:   app/userauth/forms.py
        new file:   app/userauth/urls.py
        modified:   app/userauth/views.py
        modified:   config/urls.py
        new file:   templates/app/userauth/login.html
        new file:   templates/app/userauth/register.html


#### 05.2 Creating login system

        2 Add template to login page and login
        1 Add logic to login_view

        modified:   README.md
        modified:   app/userauth/views.py
        modified:   templates/app/userauth/login.html
        modified:   templates/app/userauth/register.html


#### 05.3 Creating logout system

        2 Hiding logout and login menu in header
        1 Logout a user

        modified:   README.md
        modified:   app/userauth/urls.py
        modified:   app/userauth/views.py
        modified:   templates/app/userauth/login.html
        modified:   templates/partials/header.html


## 06. DJANGO ALERT MESSAGES


#### 06.1 Creating django alert messages

        2 Use jQuery to make alert disappear automatically in some seconds
        1 Looping alert messages in the header

        modified:   README.md
        modified:   app/userauth/views.py
        modified:   templates/base.html
        modified:   templates/partials/header.html


## 07. DJANGO MODELS


## 07.1. Django model: Product, Category, Vendor, ProductImage, CartOrder, Wishlist

        11 Modify Product model by adding vendor field
        10 Modify Product model
        9 Modify Wishlist model
        8 Modify ProductReview model
        7 Modify CartOrderItem model
        6 Modify CartOrder model
        5 Modify ProductImage model
        4 Modify Vendor model
        3 Modify Category model
        2 Modify Product model
        1 Create django model, migrations, and admin

        app/core/migrations/0001_initial.py
        app/core/migrations/0002_vendor.py
        app/core/migrations/0003_product_tag.py
        app/core/migrations/0004_productimage.py
        app/core/migrations/0005_cartorder.py
        app/core/migrations/0006_cartorderitem.py
        app/core/migrations/0007_productreview.py
        app/core/migrations/0008_wishlist.py
        app/core/migrations/0009_address.py
        app/core/migrations/0010_auto_20230104_0821.py
        app/core/migrations/0011_auto_20230104_0827.py
        app/core/migrations/0012_auto_20230104_0829.py
        app/core/migrations/0013_auto_20230104_0831.py
        app/core/migrations/0014_auto_20230104_0834.py
        app/core/migrations/0015_auto_20230104_0836.py
        app/core/migrations/0016_auto_20230104_0851.py
        app/core/migrations/0017_auto_20230104_0859.py
        app/core/migrations/0018_auto_20230104_0901.py
        app/core/migrations/0019_product_vendor.py


## 08. LOADING DAN RENDERING PRODUCTS


#### 08.1 Retrieving featured (popular) products from db and rendering them to the home page

        2 Display all products to homepage with filter
        1 Display all products to homepage without filter

        modified:   app/core/admin.py
        new file:   app/core/migrations/0020_auto_20230104_2253.py
        new file:   app/core/migrations/0021_rename_pro_status_choice_product_status_choice.py
        modified:   app/core/models.py
        modified:   app/core/views.py
        new file:   media/category/product-1-1.jpg
        ...
        new file:   media/user_directory_path/product-8-1.jpg
        new file:   media/user_directory_path/product-9-1.jpg
        new file:   media/user_directory_path/product-9-1_esaY4OO.jpg
        new file:   templates/app/core/index.html
        modified:   templates/base.html


#### 08.2 Creating product-list page and rendering featured products to it

        3 Create products list page - add logic to view and loop products to products-list
        2 Create products list page - loading static files
        1 Create products list page - add template

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/product_list.html


## 09. PRODUCTS BY CATEGORY


#### 09.1 Retrieving and rendering categories in category-list page

        6 Create category-list page - Showing all products belong to a category
        5 Create category-list page - Add logic to view and loop categories to category-list
        4 Create category-list page - Modify the template
        3 Create category-list page - Load static files
        2 Create category-list page - add template to category-list page
        1 Create category-list page - urls, views, templates

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/category_list.html


#### 09.2 Retrieving and rendering products-by-category in sidebar

        7 Create category-list page - Showing all products belong to a category in the sidebar

        modified:   README.md
        modified:   templates/app/core/category_list.html


#### 09.3 Creating Product-by category list page

        4 Create product belong to a category - dispaly all products belong to a category
        3 Create product belong to a category - load static files
        2 Create product belong to a category - add template
        1 Create product belong to a category - urls, view, templates

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        modified:   templates/app/core/category_list.html
        new file:   templates/app/core/product_by_category_list.html


## 10. DJANGO CONTEXT PROCESSORS


#### 10.1 Defining default context processors method for Category

        7 Add links to menu-related categories
        6 Add links to some category menu
        5 Load all categories page and product by category page in nav-brows-all-categories (show more ...)
        4 Load all categories page and product by category page in nav-brows-all-categories
        3 Load all categories page and product by category page in nav-mobile
        2 Load all categories page and product by category page
        1 Load category in nav-bar using context_processors

        modified:   README.md
        new file:   app/core/context_processors.py
        modified:   templates/app/core/category_list.html
        modified:   templates/app/core/index.html
        modified:   templates/app/core/product_by_category_list.html
        modified:   templates/app/core/product_list.html
        modified:   templates/partials/header.html
        modified:   templates/partials/nav-bar.html
        new file:   templates/partials/nav-brows-all-categories.html
        modified:   templates/partials/nav-mobile.html


## 11. VENDORS


#### 11.1 Creating vendor-list


        3 Add logic to vendor_list_view and render vendors to vendor's page
        2 Add template to vendors page
        1 Vendor list: urls, views, templates

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        modified:   app/core/models.py
        new file:   app/core/migrations/0023_auto_20230111_0009.py
        new file:   templates/app/core/vendor_list.html


#### 11.2. Creating vendor-detail

        6 Vendor lists - Add links in navbar
        5 Vendor detail - Part 2: Dynamic
        4 Vendor detail - Part 1: Static

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/vendor_detail.html
        modified:   templates/app/core/vendor_list.html
        modified:   templates/partials/nav-bar.html


## 12. PRODUCT DETAILS


#### 12.1 Retrieving and rendering product details

        12 Product detail - Turned off the address
        11 Product detail - Display and link product-by-category
        10 Product detail - Display Vendor information
        9 Product detail - Return & Warranty
        8 Product detail - Redering user address
        7 Product detail - Redering product description
        6 Product detail - Load product spesifications
        5 Product detail - Load product information
        4 Product detail - Loading product image and thumbnails
        3 Product detail - Loding prod_image in slider section
        2 Product detail - Add static template and load static files
        1 Product detail - Urls, Views, Template

        modified:   app/core/admin.py
        modified:   app/core/context_processors.py
        new file:   app/core/migrations/0025_alter_productimage_product.py
        new file:   app/core/migrations/0026_remove_productimage_image_productimage_thumbnail_and_more.py
        new file:   app/core/migrations/0027_product_life_product_mfd_product_stock_product_type_and_more.py
        new file:   app/core/migrations/0028_rename_stock_product_stock_status_alter_product_life.py
        new file:   app/core/migrations/0029_rename_stock_status_product_stock_count.py
        modified:   app/core/models.py
        modified:   app/core/urls.py
        modified:   app/core/views.py
        modified:   config/settings.py
        new file:   media/product-images/thumbnail-1.jpg
        new file:   media/product-images/thumbnail-2.jpg
        ...
        new file:   media/user_directory_path/cat-1.png
        new file:   media/user_directory_path/product-1-1_rNnDfBq.jpg
        new file:   media/user_directory_path/product-13-2_BCyjwCF.jpg
        modified:   templates/app/core/index.html
        new file:   templates/app/core/product_detail.html