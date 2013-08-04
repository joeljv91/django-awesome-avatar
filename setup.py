# coding: utf8

from setuptools import setup
import os

name = 'django-awesome-avatar'
package = 'awesome_avatar'
version = '1.0'

description = 'Avatar django model field'
url = 'https://github.com/dimka665/django-awesome-avatar'
author = 'Dmitry Voronin'
author_email = 'dimka665@gmail.com'
license = 'BSD'
classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
]


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name=name,
    # version=get_version(package),
    version=version,
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=get_packages(package),
    package_data=get_package_data(package),
    # install_requires=install_requires,
    classifiers=classifiers,
)


