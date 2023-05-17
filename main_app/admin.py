from django.contrib import admin
# import your models here
from .models import Game, Activity, Achievement

# Register your models here.
admin.site.register(Game)
admin.site.register(Activity)
admin.site.register(Achievement)