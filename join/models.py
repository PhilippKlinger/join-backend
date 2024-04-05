from datetime import date
from django.conf import settings
from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=7, default="#417690")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"({self.id}) {self.firstname} {self.lastname}"


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    color = models.CharField(max_length=15, default="red")
    
    def __str__(self):
        return f"({self.id}) {self.name} {self.color}"
    
    
class SubTask(models.Model):
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("urgent", "Urgent"),
    ]

    TODO_STATE = [
        ("todo", "Todo"),
        ("awaitingFeedback", "Awaiting Feedback"),
        ("inProgress", "In Progress"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    assignedTo = models.ManyToManyField(Contact, related_name="assigned_tasks", blank=True)
    created_at = models.DateField(default=date.today)
    date = models.DateField(default=date.today)
    prio = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="low")
    subtasks = models.ManyToManyField(SubTask, related_name='tasks', blank=True)
    color = models.CharField(max_length=7, default="#417690")
    stat = models.CharField(max_length=20, choices=TODO_STATE, default="todo")

    def __str__(self):
        return self.title
    
