import random
import urllib

import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from wagtail.images import get_image_model

from ...settings import wagtail_makeup_settings


class Command(BaseCommand):
    """
    Make up :x
    """

    def linkFetch(self, keyword, amount):
        base_url = "https://api.unsplash.com/search/photos?"
        args = {
            "page": "1",
            "query": keyword,
            "client_id": wagtail_makeup_settings.UNSPLASH_CLIENT_ID,
            "per_page": amount,
        }
        response = requests.get(base_url + urllib.parse.urlencode(args))
        data = response.json()["results"]
        image_urls = [i["urls"]["full"] for i in data]
        print(f"Got {len(image_urls)} images")
        return image_urls

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("keyword", nargs="+", type=str)
        parser.add_argument("amount", nargs="+", type=int)

    def handle(self, *args, **options):
        if not wagtail_makeup_settings.UNSPLASH_CLIENT_ID:
            print("UNSPLASH API CLIENT ID MISSING")
            return
        # Download An image
        keyword = options.pop("keyword")
        amount = options.pop("amount")[0]
        images = self.linkFetch(keyword, amount)
        # loop the images and save'em
        for k, v in enumerate(images):
            print(f"Downloading image {k} > {settings.MEDIA_ROOT}/unsplash{k}")
            r = requests.get(v, stream=True)
            if r.status_code == 200:
                with open(settings.MEDIA_ROOT + f"/unsplash-{k}", "wb") as f:
                    for chunk in r.iter_content(1024 * 1024):  # 1mb chunk
                        f.write(chunk)

        # update all images
        i = get_image_model()
        r = range(len(images))
        for image in i.objects.all():
            print(f"updating image {image}")
            image.file = f"{settings.MEDIA_ROOT}/unsplash-{random.choice(r)}"
            image.save()
        i.get_rendition_model().objects.all().delete()
