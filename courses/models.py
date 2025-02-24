from django.db import models
from django_prose_editor.fields import ProseEditorField

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.id)
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    description = ProseEditorField()
    level = models.CharField(max_length=80)
    schedule = ProseEditorField()
    duration_course = ProseEditorField()
    quantity_persons = models.CharField(max_length=15)
    price = ProseEditorField()
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    registration_deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    goal = ProseEditorField()
    
    def __str__(self):
        return f"Name: {self.name} -> Level: {self.level}"