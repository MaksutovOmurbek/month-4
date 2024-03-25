from django.contrib import admin
from apps.kany.models import *
from django.contrib.auth.models import User, Group

admin.site.register(UserInfo)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Experience)
admin.site.register(Blog)
admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.
