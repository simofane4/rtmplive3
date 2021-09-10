from django.contrib import admin
from .models import  Secteurs , SouSecteurs , Site ,Camera

# Register your models here.
admin.site.register(Secteurs)
admin.site.register(SouSecteurs)
admin.site.register(Site)
admin.site.register(Camera)

