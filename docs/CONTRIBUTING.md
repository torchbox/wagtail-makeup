# Contributing

Contributions are welcome.

## Developer setup

### Clone the repository

```bash
git clone https://github.com/torchbox/wagtail-makeup
```

### Create a virtual environment and install the dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e ".[testing]"
```

### Pre-commit

This project uses [pre-commit](https://pre-commit.com/) to run some checks before committing code changes.

Install the pre-commit hooks:

```bash
pre-commit install
```

### Do some work

Make some changes or add new features.

### Run the tests

```bash
python runtests.py
```
