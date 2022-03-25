from django.contrib import admin
from .models import scripture, user, favorite

admin.site.register(scripture)
admin.site.register(user)
admin.site.register(favorite)