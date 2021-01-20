from django.db import models

# Create your models here.


class User(models.Model):
    mail = models.CharField(max_length=60)
    #password = models.CharField(max_length=60)

    def __str__(self):
        return self.mail