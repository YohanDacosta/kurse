from django.contrib import admin
from .models import Course, School

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'school', 'level', 'schedule', 'duration_course', 'quantity_persons', 'price', 'initial_date', 'final_date', 'registration_deadline']
    list_filter = ['name', 'level']
    ordering = ['id']
    
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']

admin.site.register(Course, CourseAdmin)
admin.site.register(School, SchoolAdmin)
