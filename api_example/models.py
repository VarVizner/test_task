from django.db import models

class Elements(models.Model):
    section = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=19, decimal_places=5)

    def __str__(self):
        return self.name
