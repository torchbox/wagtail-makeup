from django.test import TestCase

class MakeupTest(TestCase):
    def test_math(self):
        self.assertEqual(1,1)

    def test_math_wrong(self):
        self.assertEqual(2,1)


    # Test settings are defined, if not show a warning

    # Test image file is replaced

