# Sample config file
# This is just a sample config file.
# flask-quickstart assumes your config file is named 'config.py'.
# Rename this file or create a new one

# There are no name restrictions.
# You can choose whatever name you like, just change the same in
# the 'Production' class in flask-quickstart/config.py
# app.config.from_pyfile('new_name.py', silent=True)

# If available the values in flask-quickstart/instance/config.py
# will override any config values set in flask-quickstart/config.py
# when environment is set to 'production'.

SECRET_KEY = "my_super_secret_production_key"
TESTING = False
DEBUG = False
ENV = 'production'
