from django.db import models


# Create your models here.
class Todo(models.Model):
    task_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=20)
    Description = models.TextField()
    Createion = models.DateTimeField(auto_now=True)
    Due_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("open", "open"),
            ("working", "working"),
            ("done", "done"),
            ("overdue", "overdue"),
        ],
        default="open",
    )
    tags = models.CharField(max_length=250, blank=True)
