from __future__ import unicode_literals

from django.db import models

# Create your models here.
from insurance_items.const import INSURANCE_RANGE


class InsuranceOrder(models.Model):
    range = models.CharField(choices=INSURANCE_RANGE, verbose_name="保险周期")
    start_date = models.DateField(verbose_name='起保时间')
    end_date = models.DateField(verbose_name='起保时间')
    start_time = models.CharField(max_length=5)
