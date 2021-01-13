from unsplash.api import Api
from unsplash.auth import Auth

from .settings import wagtail_makeup_settings

api = Api(
    Auth(
        wagtail_makeup_settings.CLIENT_ID,
        wagtail_makeup_settings.CLIENT_SECRET,
        wagtail_makeup_settings.REDIRECT_URI,
        code=wagtail_makeup_settings.CODE,
    )
)
