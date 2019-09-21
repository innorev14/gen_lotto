from django.contrib import admin
from .models import *

# Register your models here.
class MyLottoAdmin(admin.ModelAdmin):
    pass

class GenLottoAdmin(admin.ModelAdmin):
    pass

class WinnumAdmin(admin.ModelAdmin):
    pass