from django.contrib import admin

# Register your models here.
from .models import SampleDB # models.pyで指定したクラス名

admin.site.register(SampleDB) # models.pyで指定したクラス名