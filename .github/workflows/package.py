name: Python package

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install wagtail coverage
    - name: Test
      run: |
        pip install coverage
        coverage run ./runtests.py
        coverage report
        coverage xml
        bash <(curl -s https://codecov.io/bash) -t "9d556c62-4005-47d0-9028-74bd299624fc"

