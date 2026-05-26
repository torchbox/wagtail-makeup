#!/usr/bin/env python

"""
Installs wagtailmakeup.
"""

from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

testing_extras = [
    "coverage>=7.0",
]

development_extras = [
    "black==26.5.1",
    "flake8==7.3.0",
    "isort==8.0.1",
]

setup(
    name="wagtailmakeup",
    version="1.1.0",
    description="Wagtail Makeup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinhowbrook/wagtail-makeup",
    author="Kevin Howbrook",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "Django>=5.2",
        "wagtail>=7.0",
        "python-unsplash>=1.1.0",
    ],
    extras_require={
        "testing": testing_extras,
        "development": development_extras,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 7",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
),
