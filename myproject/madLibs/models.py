from django.db import models

class MadLib(models.Model):
    adjective1 = models.CharField(max_length=50, default=" ")
    place1 = models.CharField(max_length=50, default=" ")
    verb1 = models.CharField(max_length=50, default=" ")
    noun1 = models.CharField(max_length=50, default=" ")
    adjective2 = models.CharField(max_length=50, default=" ")
    verb2 = models.CharField(max_length=50, default=" ")
    noun2 = models.CharField(max_length=50, default=" ")
    story = models.TextField(default="Hi there people!")

    def __str__(self):
        return self.story