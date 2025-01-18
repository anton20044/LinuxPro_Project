from django.db import models

# Create your models here.

class accpList(models.Model):
  accp = models.IntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
        return self.name

class accpSaldo(models.Model):
  accp = models.IntegerField()
  date = models.DateField()
  summ = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
        return self.name
