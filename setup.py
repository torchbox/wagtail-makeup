
#!/usr/bin/env python
"""
Installs wagtailmakeup.
"""

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

testing_extras = [
    'coverage>=4.5',
]

setup(name='wagtailmakeup',
      version='0.0.3',
      description='Wagtail Makeup',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/kevinhowbrook/wagtail-makeup',
      author='Kevin Howbrook',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      install_requires=[
          'wagtail>=2.15',
          'python-unsplash>=1.1.0'
      ],
      extras_require={'testing': testing_extras},
      ),

