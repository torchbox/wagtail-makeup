# Wagtail Makeup

![tests](https://github.com/kevinhowbrook/wagtail-makeup/workflows/Tests/badge.svg)
[![codecov](https://codecov.io/gh/kevinhowbrook/wagtail-makeup/branch/main/graph/badge.svg?token=A4H7PFEL9J)](https://codecov.io/gh/kevinhowbrook/wagtail-makeup)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/kevinhowbrook/wagtail-makeup.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kevinhowbrook/wagtail-makeup/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/kevinhowbrook/wagtail-makeup.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kevinhowbrook/wagtail-makeup/context:python)

Tired of having no images locally when you need them? Don't want to fill your computer up with images?
Use Wagtail Makeup ;)

## Installation

Wagail makeup depends on python unsplash:

`pip install python-unsplash wagtailmakeup`

## Configuration

Sign up for an Unsplash api key and add this to your settings:

```
# settings.py
WAGTAIL_UNSPLASH = {
    "CLIENT_ID": "",
    "CLIENT_SECRET": ""
}
```

The API is rate limited to 50 request/hour... you can apply for a [higher rate limit](https://help.unsplash.com/en/articles/3887917-when-should-i-apply-for-a-higher-rate-limit).

## Using

You probably don't want this in your production settings, so add the following to you local.py settings:

```
INSTALLED_APPS.append('wagtailmakeup')
```

Wagtail Makeup works by providing a new management command:

```
python manage.py make_up [search query] [amount of images]
```

So you want to replace all your broken images on your site with dogs (who wouldn't)
you can do it like this:

```
python manage.py make_up dogs 10
```

Note: the amount value is the number of images to download, the higher this is, the more
variance you will get.

:cool:
