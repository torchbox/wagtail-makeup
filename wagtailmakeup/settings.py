from django.conf import settings

DEFAULTS = {}


class WagtailMakeUpSettings:
    def __getattr__(self, attr):
        django_settings = getattr(settings, "WAGTAIL_UNSPLASH", {})

        try:
            return django_settings[attr]
        except KeyError:
            return getattr(DEFAULTS, attr, None)


wagtail_makeup_settings = WagtailMakeUpSettings()
