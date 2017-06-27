# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import gallery


setup(
    name='gallery',
    version=gallery.__version__,
    description='',
    author='pycat',
    author_email='kkampardi@gmail.com',
    include_package_data=True,
    url='https://github.com/GoWebyCMS/gallery' % gallery.__version__,
    packages=find_packages(),
    classifiers=[
        'Development Status :: ',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI