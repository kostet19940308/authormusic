from django.contrib import admin
from .models import Album
from .models import Horns
from .models import Track

# Register your models here.

admin.site.register(Album)
admin.site.register(Horns)
admin.site.register(Track)