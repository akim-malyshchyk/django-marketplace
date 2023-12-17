# Online marketplace
The project is an online store website with the ability to place orders and save the results in a database.
The project was implemented using the Django framework.

## Tech stack
Python 3.8 and Django 3.2 were used as a basis. PostgreSQL was chosen as the database.
Bootstrap and django templates were used to render frontend. Project version control was carried out using Git.

## Initial configuration of the project
### Preparation
Before you start setting up the project, you need to install
Python 3 and PostgreSQL. In postgreSQL you also need to create a database called `shop`.

### Project setup
1. Cloning a repository with code
```
git clone https://github.com/akim-malyshchyk/django-marketplace.git
```
2. Creating a virtual python environment (inside the repository folder)
```
python -m venv venv
```
3. Activation of virtual environment (Linux)
```
source venv/bin/activate
```
4. Install the necessary project dependencies
```
pip install -r requirements.txt
```
5. Applying database migrations (creating tables)
```
python manage.py migrate
```
6. Filling the database with test data
```
python manage.py create_default_data
```
As a result of executing the command, the superuser `admin` with the password `pass1234` will be created,
as well as goods for the store.

7. Launch the project on your local machine
```
python manage.py runserver localhost:8000
```
After completing the procedures, access to the website should appear in the browser at `https://localhost:8000`.


## Features
* Selecting products and adding them to cart
* Select the quantity of products
* Calculation of order cost taking into account the number of goods
* Admin panel with the ability to edit data about products, categories, orders and users
* User login and registration


## Architecture

### Database structure
In addition to the standard Django tables, 5 more were created.
The tables and relationships between them are shown in the screenshot below.

![db_architecture](screenshots/db_arch.png)


### Project structure
The project consists of two applications: `accounts` and `shop`. Each of them represents a folder in which
are located:
* models for the database (`models.py`)
* logic for working with user requests (`views.py`)
* forms (`forms.py`)
* list of used urls (`urls.py`)
* `templates` folder with html page templates
* some other supporting files

html templates were written using Django Template Language, which allows you to dynamically change templates in
depending on the data. Layout and styling were implemented using Bootstrap. To avoid code duplication in some
Template inheritance was used in some places.

The `src` folder contains a file with the main project settings (`settings.py`), and others necessary for launching
website files.

The `manage.py` script is responsible for launching the project; the project's dependencies are stored in the `requirements.txt` file.

### Result
All product categories are displayed on the main page of the store

![main page](screenshots/main_page.png)
Using the `View goods` button you can open any category. Here you can add items to your cart,
indicating the required quantity

![category goods](screenshots/goods.png)
After selecting the required products, you can go to the ordering page by clicking on the `Cart` button

![order](screenshots/order.png)
After filling out and submitting the form, an order will be generated in the database. It can be seen by the administrator on the `Admin page`.
The admin panel was implemented using Django's built-in tools

![admin panel](screenshots/admin_panel.png)
On the admin panel you can edit information about products and categories, as well as view generated orders

![edit category](screenshots/edit_category.png)
