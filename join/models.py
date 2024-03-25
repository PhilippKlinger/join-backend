from datetime import date
from django.conf import settings
from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=7, default="#417690")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.id}) {self.firstname} {self.lastname}"


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    # Priority choices
    LOW = "low"
    MID = "mid"
    HIGH = "high"
    PRIORITY_CHOICES = [
        (LOW, "Low"),
        (MID, "Mid"),
        (HIGH, "High"),
    ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ManyToManyField(Contact, related_name="assigned_tasks", blank=True)
    due_date = models.DateField(default=date.today)
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, default=LOW)

    def __str__(self):
        return self.title


class SubTask(models.Model):
    task = models.ForeignKey(Task, related_name="subtasks", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
