from datetime import datetime
from django.db import models
from supers.models import Supers

# Create your models here.

class Battle(models.Model):
    super_one = models.ForeignKey(Supers, on_delete=models.CASCADE)
    super_two = models.ForeignKey(Supers, on_delete=models.CASCADE)
    battle_date = datetime