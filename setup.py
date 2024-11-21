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
    "coverage>=7.5.2",
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
    install_requires=["wagtail>=5.2", "python-unsplash>=1.2.5"],
    extras_require={"testing": testing_extras},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 5",
        "Framework :: Wagtail :: 6",
    ],
),
