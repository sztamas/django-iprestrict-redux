django-iprestrict-redux
=======================

[![Build Status](https://travis-ci.org/sztamas/django-iprestrict-redux.png?branch=master)](https://travis-ci.org/sztamas/django-iprestrict-redux) 
[![PyPI](https://badge.fury.io/py/django-iprestrict-redux.svg)](https://pypi.python.org/pypi/django-iprestrict-redux)
[![Documentation Status](https://readthedocs.org/projects/django-iprestrict/badge/?version=latest)](http://django-iprestrict.readthedocs.org/en/latest/?badge=latest)
![GitHub](https://img.shields.io/github/license/sztamas/django-iprestrict-redux)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

___

***Note:***
This project is an effort to keep the original [django-iprestrict](https://github.com/muccg/django-iprestrict) project alive and updated.
The original project isn't maintained anymore by my previous employer, so I took on forking and maintaining the project for existing users.

See the comments on the following Pull Request and Issue for more background info:
* https://github.com/muccg/django-iprestrict/pull/57
* https://github.com/muccg/django-iprestrict/issues/60

Switching to `django-iprestrict-redux` is as easy as declaring `django-iprestrict-redux` instead of `django-iprestrict` as a dependency in whatever you use for managing dependencies. (ex. setup.py, requirements files, poetry etc.)
___

Django app + middleware to restrict access to all or sections of a Django project by client IP ranges.

For installation and usage information please Read the Docs:

  http://django-iprestrict-redux.readthedocs.org/en/latest/
