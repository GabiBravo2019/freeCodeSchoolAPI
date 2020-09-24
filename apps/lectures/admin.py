from django.contrib import admin
from .models import Lecture

# Register your models here.

class LectureteAdmin(admin.ModelAdmin):
    list_display = ('title','lecturer_name','date')
    search_fields = ('title',)

admin.site.register(Lecture,LectureteAdmin)
