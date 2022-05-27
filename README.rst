=======
vl_snippet
=======

vl_snippet is django-cms plugin which is part of VL (Viva Library, https://vits.pro/dev/).

This plugin adds snippet (custom html, js code or prepared template) to page.


Installation
============

vl_snippet requires vl_core package: https://bitbucket.org/vivazzi/vl_core/

There is no vl_snippet in PyPI, so you can install this package from bitbucket repository only.

::
 
    $ pip install git+https://bitbucket.org/vivazzi/vl_snippet.git


Configuration 
=============

1. Add "vl_snippet" to INSTALLED_APPS after "vl_core"

::

    INSTALLED_APPS = (
        ...
        'vl_core',
        'vl_snippet',
        ...
    )

2. Run `python manage.py migrate` to create the vl_snippet models.