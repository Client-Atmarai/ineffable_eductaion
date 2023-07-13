from django.contrib import admin
from .models import AdminLogin,ResgisterStudent,CentreRegisterStudent,Status
# Register your models here.
admin.site.register(AdminLogin)
admin.site.register(ResgisterStudent)
admin.site.register(CentreRegisterStudent)

admin.site.register(Status)

 