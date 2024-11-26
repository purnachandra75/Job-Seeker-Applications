from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.Education)
admin.site.register(models.Languages)
admin.site.register(models.Personalinfo)

admin.site.register(models.Skill)
admin.site.register(models.WorkExperience)


