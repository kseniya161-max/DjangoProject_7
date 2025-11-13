from django.db import models

class Clients(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length = 100)
    comment = models.TextField(blank=True)


    def __str__(self):
        return self.name


class Message(models.Model):
    header = models.CharField(max_length=200)
    content = models.TextField()


    def __str__(self):
        return self.header
