Requirements and Installation
=============================

Requirements
------------

* ``Django 1.8+``

Additionally, if you would like to use country based restrictions you will need:

* ``pycountry``
* MaxMind_ ``geoip`` or ``geoip2`` libraries as described in the *Django* documentation. Links below.

.. _MaxMind: https://www.maxmind.com

In case you are on at least *Django 1.9* or newer, you should configure geoip2_, if you are on *Django 1.8* you have to use and configure geoip_.

.. _geoip: https://docs.djangoproject.com/en/1.8/ref/contrib/gis/geoip/
.. _geoip2: https://docs.djangoproject.com/en/1.10/ref/contrib/gis/geoip2/

Installation
------------

You can pip install from PyPI::

    pip install django-iprestrict

The country based lookups are optional, if you need it you can install them with::

    pip install django-iprestrict[geoip]

**Note:** if you're not using the country based lookups you will have to set the ``IPRESTRICT_GEOIP_ENABLED`` setting to ``False`` in your ``settings.py``. See: :ref:`geoip-enabled-reference-label`.

Development
^^^^^^^^^^^

For development you will need Poetry_.

.. _Poetry https://python-poetry.org


Fork the project and then:

    poetry install

To run the tests against the *python* and *Django* in your virtualenv::

    pytest

To run the tests against all combinations of supported *Python 3*, and *Django* versions::

    tox

This will also run *flake8*.
