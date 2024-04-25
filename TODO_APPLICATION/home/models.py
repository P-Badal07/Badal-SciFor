from django.db import models

# Create your models here.
class Task(models.Model):
    tasktittle = models.CharField(max_length=50)
    taskdesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tasktittle

