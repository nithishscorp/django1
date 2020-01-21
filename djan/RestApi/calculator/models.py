# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
      name = models.CharField(max_length=10)
      id_num = models.IntegerField()

class calc(models.Model):
      operator=models.CharField(max_length=1)
      n1=models.IntegerField()
      n2=models.IntegerField()
      total=models.IntegerField()

      def __str__(self):
         return self.total
