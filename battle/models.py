from datetime import datetime
from django.db import models
from supers.models import Supers
import random

# Create your models here.

class Battle(models.Model):
    super_one = models.ForeignKey(Supers, related_name='super_one', on_delete=models.CASCADE)
    super_two = models.ForeignKey(Supers, related_name='super_two', on_delete=models.CASCADE)
    battle_date = models.DateTimeField()