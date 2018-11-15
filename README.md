## Django quiz app


This is a fork of Tom Walker's [Django Quiz Project](https://github.com/tomwalker/django_quiz) with the following enhancements.

1. Make it work for latest Django 1.x (Django 1.11.16)
2. Use latest versions of `Pillow` and `django-model-utils`
3. Remove `requirements.txt` and absorb all dependencies in `setup.py`
4. Fix a bug with the need to explicitly mention the `form_class` in `quiz` app views. [Ref: https://stackoverflow.com/questions/35430637/warning-after-overwriting-get-form ]
5. Fix URL dispatching to not use `patterns`
6. Make it work with Python3, specifically tested on `Python3.6.6`
7. Modified `test_settings.py` for Django 1.11.16
8. Replaced deprecated `CommaSeparatedIntegerField` with `CharField` and the `validate_comma_separated_integer_list` validator.
9. Fixes to `urls.py`
10. Moved licensing to `LICENSE` file

## Install

For installation, just run the setup.py

    $ python setup.py

Please see the original project README for rest of the details.
