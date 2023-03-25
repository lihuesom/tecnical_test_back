from django.contrib import admin
from .models import Client,Offer,Agreement

# Register your models here.

admin.site.register(Client)
admin.site.register(Offer)
admin.site.register(Agreement)

