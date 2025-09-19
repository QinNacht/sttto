from django.contrib import admin
from .models import Students, Additonal_Info, Address, Account, EducationBG
# Register your models here.
# admin.site.register(TestingDatabase)
admin.site.register(Students)
admin.site.register(Additonal_Info)
admin.site.register(Address)
admin.site.register(EducationBG)
admin.site.register(Account)
