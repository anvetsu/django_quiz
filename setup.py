from setuptools import setup
from io import open

readme = open('README.rst', encoding='utf-8').read()

setup(
    name='django-quiz-app',
    version='0.6',
    packages=['quiz', 'multichoice', 'true_false', 'essay', 'quiz.templatetags'],
    include_package_data=True,
    license='MIT License',
    description='A configurable quiz app for Django.',
    long_description=readme,
    url='https://github.com/anvetsu/django_quiz',
    author='Tom Walker',
    author_email='tomwalker0472@gmail.com',
    maintainer_email='anand@anvetsu.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',        
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django-model-utils==3.1.2',
        'Django==1.11.16',
        'Pillow==5.3.0',
        'tox==3.5.3'
    ],
    test_suite='runtests.runtests'
)
