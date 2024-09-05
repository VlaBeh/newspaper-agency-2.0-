from django.db import models
from django.contrib.auth.models import AbstractUser
from newspaper_agency import settings


class Topic(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Newspaper(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='redactors')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
