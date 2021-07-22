import random

import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand
from wagtail.images import get_image_model

from ...api import api
from ...settings import wagtail_makeup_settings

Image = get_image_model()
MEDIA_ROOT = settings.MEDIA_ROOT


class Command(BaseCommand):
    """Make up :x

    A management command which takes 2 arguments on the command line,
    and does something with each of them.

    Command line arguments:
        query: The search query for unsplash
        count: The ammount of images to download

    EG: `python manage.py ducks 4`
        Would download 4 images of ducks and replace all your images.
    """

    # Metadata about this command.
    help = "Replace local images with unsplash images"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("query", nargs="+", type=str)
        parser.add_argument("count", nargs="+", type=int)

    def save_image(self, unsplash_photo):
        """Saves an image from unsplash"""
        photo = api.photo.get(unsplash_photo.id)
        url = photo.urls.raw
        # loop the images and save'em
        print(
            f"Downloading image {photo.id} > \
            {MEDIA_ROOT}/unsplash-{photo.id}"
        )
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(MEDIA_ROOT + f"/unsplash-{photo.id}", "wb") as f:
                for chunk in r.iter_content(1024 * 1024):  # 1mb chunk
                    f.write(chunk)

    def search_for_image(self, query, count):
        # TODO, if there is no query support random images
        return api.photo.random(query=query, count=count)

    def update_wagtail_image(self, image, photos):
        """Replaces an image object with the an unsplash image

        Args:
            image (class): CustomImage objects
            photos (class): unsplash.models.ResultSet of photos
        """
        # random selection from photos
        photo = random.choice(photos).id
        image.file = f"{MEDIA_ROOT}/unsplash-{photo}"
        image.save()

    def handle(self, *args, **options):
        if (
            not wagtail_makeup_settings.CLIENT_ID
            or not wagtail_makeup_settings.CLIENT_SECRET
        ):
            raise ImproperlyConfigured('WAGTAIL_UNSPLASH SETTINGS MISSING')

        query = options.pop("query")
        count = options.pop("count")[0]

        # Search for the image
        photos = api.photo.random(query=query, count=count)

        # Save the images
        for photo in photos:
            self.save_image(photo)

        # Update all images
        for image in Image.objects.all():
            self.update_wagtail_image(image, photos)

        # Finally, delete the existing image renditions
        Image.get_rendition_model().objects.all().delete()
