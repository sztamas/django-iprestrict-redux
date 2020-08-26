Requirements and Installation
=============================

Requirements
------------

* ``Django 2.2+``

Additionally, if you would like to use country based restrictions you will need:

* ``pycountry``
* MaxMind_ geoip2_ libraries as described in the *Django* documentation. Links below.

.. _MaxMind: https://www.maxmind.com
.. _geoip2: https://docs.djangoproject.com/en/1.10/ref/contrib/gis/geoip2/

Installation
------------

You can pip install from PyPI::

    pip install django-iprestrict-redux

The country based lookups are optional, if you need it you can install them with::

    pip install django-iprestrict-redux[geoip]

**Note:** if you're not using the country based lookups you will have to set the ``IPRESTRICT_GEOIP_ENABLED`` setting to ``False`` in your ``settings.py``. See: :ref:`geoip-enabled-reference-label`.

Development
^^^^^^^^^^^

For development create a ``virtualenv``, activate it and then::

    pip install -e .[geoip,dev]

To run the tests against the *python* and *Django* in your virtualenv::

    ./runtests.sh

To run the tests against all combinations of *python 2*, *python 3*, and supported *Django* versions::

    tox

This will also run *flake8*.
