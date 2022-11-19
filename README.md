
```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- endpoints/                     # Informations about the endpoints / Django REST API Information
   |    |    |-- urls.py                   # Defines routes to access the models
   |    |    |-- views.py                  # Defines how models are accessed in REST API
   |    |    |-- serializers.py            # Defines how database objects are mapped in request
   |    |    |-- models.py                 # Database models to store informtion about algorithms and requests in the database
   |    |
   |    |-- ML/                            # Storage location for all ML related code
   |    |    |-- income_classifier/            # keeps the income classifiers
   |    |    |     |-- random_forest.py        # Implement ML algorithm code here  
   |    |    |   
   |    |    |-- tests.py                  # Test case to check if RF algorithm is working as expected 
   |    |    |-- registry.py               # To connect ML code with the server code
   |    |
   |    |-- quality1/                      # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- models.py                 # D
   |    |
   |    |-- Jupyter notebook/              # Hier können Jupyter notebooks gespeichert werden 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

# Einbindung ML Modell in Endpoints

### Jupyter Notebook: 
Der ML-Algorithmus besteht nicht nur aus den Variablen rf und et (mit Modellgewichten)
- Vorverarbeitungsvariablen train_mode und encoders müssen auch gespeichert werden

- save preprocessing objects and RF algorithmen:

- pickle.dump(train_mode, "./train_mode.pkl", compress=True)
- pickle.dump(encoders, "./encoders.pkl", compress=True)
- pickle.dump(rf, "./random_forest.pkl", compress=True)
- pickle.dump(et, "./extra_trees.pkl", compress=True)

### Anpassung des ML Codes und hinzufügen der App:
- Passe apps / ML / income_classifier / random_forest.py Datei an deinen ML-Code an 
- (https://www.deploymachinelearning.com/serve-ml-models/)

- Add ML app to INSTALLED_APPS in core / settings.py

### Testen des RF Algorithmus
- Passe apps / ML / tests.py Datei an ML Modell an
- run python manage.py test apps.ml.tests

### ML Code mit Server Code verbinden
- Hierfür wird ML registry object in apps / ML / registry.py Datei erstellt
- Enthällt Informationen über verfügbare Algorithmen und deren entsprechende Endpunkte

# [Datta Able Django](https://appseed.us/product/datta-able/django/)

Open-source **Django Dashboard** generated by `AppSeed` op top of a modern design. **[Datta Able](https://appseed.us/product/datta-able/django/)** Bootstrap Lite is the most stylised Bootstrap 4 Lite Admin Template, around all other Lite/Free admin templates in the market. It comes with high feature-rich pages and components with fully developer-centric code. 

- 👉 [Datta Able Django](https://appseed.us/product/datta-able/django/) - `Product page`
- 👉 [Datta Able Django](https://django-datta-able.appseed-srv1.com/) - `LIVE demo`
- 👉 [Complete documentation](https://docs.appseed.us/products/django-dashboards/datta-able) - `Learn how to use and update the product`


<br />

> 🚀 Built with [App Generator](https://appseed.us/generator), timestamp: `2022-10-05 07:49`

- ✅ `Up-to-date dependencies`
- ✅ Database: `sqlite`
- ✅ `Authentication`, Session Based, `OAuth` via **Github**
- ✅ `Dark Mode` (persistent)
- ✅ Docker
  

<br /> 

## ✨ Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/django-datta-able.git
$ cd django-datta-able
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## ✨ Create a new `.env` file using sample `env.sample`

The meaning of each variable can be found below: 

- `DEBUG`: if `True` the app runs in develoment mode
  - For production value `False` should be used
- `ASSETS_ROOT`: used in assets management
  - default value: `/static/assets`
- `OAuth` via Github
  - `GITHUB_ID`=<GITHUB_ID_HERE>
  - `GITHUB_SECRET`=<GITHUB_SECRET_HERE> 

<br />

## ✨ How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-datta-able.git
$ cd django-datta-able
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
// OR with https
$ python manage.py runsslserver 
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented below:


<br />



---
[Datta Able Django](https://appseed.us/product/datta-able/django/) - Open-source starter generated by **[AppSeed Generator](https://appseed.us/generator/)**.
