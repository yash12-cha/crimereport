from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Reports
from .models import Report
from .models import extendeduser
admin.site.register(Reports)
admin.site.register(Report)
admin.site.register(extendeduser)
