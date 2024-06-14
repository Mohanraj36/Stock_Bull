from django.contrib import admin
from .models import Profile, Usersaved, Userprediction, Predictioncount

admin.site.site_header = 'Stock Bull'
admin.site.site_title = 'Administrator'
admin.site.index_title = 'Welcome'

# Register your models here.
admin.site.register(Profile)
admin.site.register(Usersaved)
admin.site.register(Userprediction)
admin.site.register(Predictioncount)

