Changelog
=========

### 1.9.0 Aug 30, 2020
  - Switched to Poetry (https://python-poetry.org/) + more cleanup
  - Switched to pytest and pytest-django
  - Drop support for pre-Django 1.10 style MIDDLEWARES
  - Switch to old style url to path in urls.py
  - Added Black and re-formatted and linted all the code
  - Added isort and sorted all imports
  - Bugfix: Add rule in admin was throwing an exception
  - Handling "unknown" values in X-Forwarded-For header; introduces IPRESTRICT_USE_PROXY_IF_UNKNOWN header
  - More cleanup

### 1.8.1 Aug 24, 2020
  - General clean-up after forking the project from muccg/django-iprestrict
  - Added support for Django 3+
  - Dropped support for old releases of Django/Python

