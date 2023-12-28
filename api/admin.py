from django.contrib import admin

from .models import *

admin.site.register(comments)
admin.site.register(todos)
admin.site.register(users)
admin.site.register(posts)
