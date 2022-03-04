from django.contrib import admin
from .models import SocialPost, SocialComments, Image


admin.site.register(SocialPost)
admin.site.register(SocialComments)
admin.site.register(Image)
