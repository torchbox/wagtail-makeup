from io import StringIO
from django.core.management import call_command
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings
from ..settings import WagtailMakeUpSettings
from ..api import api


class MakeupTest(TestCase):

    def test_settings_missing(self):
        wagtail_makeup_settings = WagtailMakeUpSettings()
        self.assertEqual(wagtail_makeup_settings.CLIENT_ID, None)
        self.assertEqual(wagtail_makeup_settings.CLIENT_SECRET, None)

    @override_settings(WAGTAIL_UNSPLASH={'CLIENT_ID': 1234,'CLIENT_SECRET': 'shh'})
    def test_settings_defined(self):
        settings = WagtailMakeUpSettings()
        self.assertEqual(settings.CLIENT_ID, 1234)
        self.assertEqual(settings.CLIENT_SECRET, 'shh')

    # Test settings are defined, if not show a warning
    def test_call_with_no_settings(self):
        with self.assertRaises(ImproperlyConfigured, msg='WAGTAIL_UNSPLASH SETTINGS MISSING'):
            out = StringIO()
            call_command('make_up', 'cats', '1', stdout=out)
