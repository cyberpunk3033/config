from django.db import models

# Create your models here.
# Import the models module from django.db
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To do'),
        ('IN_PROGRESS', 'In progress'),
        ('DONE', 'Done'),
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='TODO')
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='MEDIUM')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name  # Return the name of the task
