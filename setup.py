import os
import re
from setuptools import setup


def get_package_version(package):
    version = re.compile(r"(?:__)?version(?:__)?\s*=\s\"(.*)\"", re.I)
    initfile = os.path.join(os.path.dirname(__file__), package, "__init__.py")
    for line in open(initfile):
        m = version.match(line)
        if m:
            return m.group(1)
    return "UNKNOWN"


def get_package_data():
    return [
        os.path.join(root, f) for d in ('templates', 'static')
        for root, _, files in os.walk('iprestrict/{}'.format(d))
        for f in files]


setup(
    name='django-iprestrict-redux',
    version=get_package_version("iprestrict"),
    description=('Django app + middleware to restrict access to all or sections of a '
                 'Django project by client IP ranges'),
    long_description=('Django app + middleware to restrict access to all or sections of a '
                      'Django project by client IP ranges'),
    author='Tamas Szabo, CCG - Murdoch University',
    author_email='me@tamas-szabo.com',
    url='https://github.com/sztamas/django-iprestrict-redux',
    download_url='https://github.com/sztamas/django-iprestrict-redux/releases',
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    packages=[
        'iprestrict',
        'iprestrict.management',
        'iprestrict.management.commands',
        'iprestrict.migrations',
    ],
    package_data={
        'iprestrict': get_package_data()
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=2.2',
    ],
    extras_require={
        'geoip': [
            'pycountry==20.7.3',
            'geoip2==4.0.2',
            ],
        'dev': [
            'tox',
            'pep8',
            'flake8',
            'mock',
            'Sphinx',
            'django-extensions',
            'Werkzeug',
            ],
    },
    test_suite='tests.runtests.main',
)
