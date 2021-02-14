from django.db import models


class Person(models.Model):
    iin = models.CharField(max_length=12,blank=False,unique=True)
    age = models.IntegerField(blank=False)

    def __str__(self):
        return self.iin
