# Wagtail Makeup

Tired of having no images locally when you need them? Don't want to fill your computer up with images?
Use Wagtail Makeup ;)

## Installation

`pip install wagtailmakeup`

## Configuration

Sign up for an Unsplash api key and add this to your settings:

```
WAGTAIL_MAKEUP_SETTINGS = {
    "UNSPLASH_CLIENT_ID": "your api id here - access key",
}
```

## Using

You probably don't want this in your production settings, so add the following to you local.py settings:

```
INSTALLED_APPS.append('wagtailmakeup')
```

Wagtail Makeup works by providing a new management command:

```
python manage.py make_up [keyword] [amount of images]
```

So you want to replace all your broken images on your site with dogs (who wouldn't)
you can do it like this:

```
python manage.py make_up dogs 10
```

Note: the amount value is the number of images to download, the higher this is, the more
variance you will get.

:cool:
