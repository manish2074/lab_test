from django.contrib import admin
from .models import UserSession,Test,Subtest
# Register your models here.


admin.site.register(Test)
admin.site.register(Subtest)
admin.site.register(UserSession)