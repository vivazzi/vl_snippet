import os
from setuptools import setup, find_packages
from vl_snippet import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='vl_snippet',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    platforms=['OS Independent'],
    description='This django-cms plugin adds snippet (custom html, js code or prepared template) to page',
    long_description=README,
    url='https://vuspace.pro/',
    download_url='https://bitbucket.org/vivazzi/vl_snippet/downloads/',
    author='Artem Maltsev',
    author_email='maltsev.artjom@gmail.com',
    keywords='django django-cms vl snippet',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
