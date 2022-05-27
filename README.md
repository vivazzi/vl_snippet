# vl_snippet

**vl_snippet** is django-cms plugin which is part of VL (Viva Library, https://vits.pro/dev/).

This plugin adds snippet (custom html, js code or prepared template) to page.


## Installation

vl_snippet requires vl_core package: https://github.com/vivazzi/vl_core

There is no vl_snippet in PyPI, so you can install this package from repository only.

```shell
$ pip install git+https://github.com/vivazzi/vl_snippet
```


## Configuration 

1. Add `vl_snippet` to `INSTALLED_APPS` after `vl_core`:

```python
INSTALLED_APPS = (
    ...
    'vl_core',
    'vl_snippet',
    ...
)
```

2. Run `python manage.py migrate` to create the vl_snippet models.


## Run tests

Run `python manage.py test vl_snippet`


# CONTRIBUTING

To reporting bugs or suggest improvements, please use the [issue tracker](https://github.com/vivazzi/vl_snippet/issues).

Thank you very much, that you would like to contribute to vl_snippet. Thanks to the [present, past and future contributors](https://github.com/vivazzi/vl_snippet/contributors).

If you think you have discovered a security issue in our code, please do not create issue or raise it in any public forum until we have had a chance to deal with it.
**For security issues use security@vuspace.pro**


# LINKS

- Project's home: https://github.com/vivazzi/vl_snippet
- Report bugs and suggest improvements: https://github.com/vivazzi/vl_snippet/issues
- Author's site, Artem Maltsev: https://vivazzi.pro

# LICENCE

Copyright © 2022 Artem Maltsev and contributors.

MIT licensed.