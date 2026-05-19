from django.db import models

class Tasks(models.Model):
    task_name = models.CharField(max_length=50)
    due_date = models.DateField()
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    

