from django.contrib import admin
# import your models here
from .models import Game, Activity

# Register your models here.
admin.site.register(Game)
admin.site.register(Activity)