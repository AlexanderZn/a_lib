from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Genre)

admin.site.register(Book)

admin.site.register(Comments)

admin.site.register(UserBook)