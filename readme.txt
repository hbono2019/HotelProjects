########################################################
#
#     Readme.txt
########################################################
#
#
#    https://github.com/hbono2019/HotelProjects
#
#   Hotels Project
#   Description: The website will handle
#   Team Members:
#   Hector Bonilla: D18129993: D18129993@mytudublin.ie
#   Hassan Yaqoob: D18130130: D18130130@mytudublin.ie
########################################################
#
#   The project was designed in Django -Python - React - Bootstrap - Javascript - Google Apps
#   Directory Path is:
#   PycharmProjects/HotelProjects
#   after Unzip it will have the following structure:
#   .idea                -> Contains internal links to Libraries Pycharm and Github
#   __pycache__          -> Cached files for Python
#   HotelProjects        -> Main application and it has all the project settings
#   HotelsApp            -> Application for Hotels, it contains the login and authentication webpages
#   HotelsAppCRUD        -> Application for CRUD, it contains all the webpages for the CRUD the MVT (Model -View and Template)
#   static               -> Contains all the stylesheets from Royal Hotel https://colorlib.com/wp/template/royal/ but reimplemented into our Django project
#   templates            -> Contains all the main webpages for the Hotels website
#   v_env                -> All Django, Python libraries
#   manage.py            -> the manage python to configure features example MongoDB
#   master               -> created empty file and it is for internal use in Python it cannot be removed
#   Procfile             -> File that is used in Heroku for Unicorn
#   readme.txt           -> File that contains all specifications for the project
#   requirements.txt     -> Requirements file for deployment in Heroku it contains all the libraries and extras added to the proyect
#   runtime.txt          -> it sets the runtime Python to be run in Heroku
########################################################
#
# Deployment in Heroku this was the setup to be run one-off
# Heroku is now connected to GitHub: https://github.com/hbono2019/HotelProjects
# and autodeploys to the following website
#
# https://dashboard.heroku.com/apps/nameless-anchorage-46653
#
#
# Steps that were used to deploy in Heroku
# Procfile
# Content in the file added one line
# web: gunicorn HotelProjects.wsgi --log-file -
#
# Gunicorn
# Installing gunicorn to the HotelProjects environment
# pip install gunicorn
#
# Database configuration
# pip install dj-database-url to the HotelProjects environment
#
# And in the settings.py file included the following lines
# Heroku: Update database configuration from $DATABASE_URL.
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
#
# In the settings.py file included the following lines
# The absolute path to the directory where collectstatic will collect static files for deployment.
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
# ]
#
# Whitenoise
# Install whitenoise to the HotelProjects environment
# pip install whitenoise
# in the settings.py add one line
# MIDDLEWARE = [
#     ...
#    'whitenoise.middleware.WhiteNoiseMiddleware',
# ]
#
# Add one line in the settings.py see the last line
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#
# Requirements.txt File
# Run pip freeze > requirements.txt
# Add one line in the requirements.txt file
# psycopg2-binary==2.7.7
# Make sure that a psycopg2 line like the one above is present! Even if you didn't install this locally then you should still add this to the requirements.txt.
# runtime.txt file
# The runtime.txt file, if defined, tells Heroku which programming language to use
# Add one line:
# python-3.7.0
#
# Heroku is connected in GitHub to be autodeployed after the code has been pushed into GitHub
#



