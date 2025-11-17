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


class Mailing(models.Model):
    STATUS_CHOICES = [('created', 'создана'),
                      ('started', 'запущена'),
                      ('completed', 'завершена')]

    datetime_start = models. DateTimeField()
    datetime_end = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Clients)

    def __str__(self):
        return f'Рассылка: {self.message.header}  - Статус: {self.get_status_display()}'

