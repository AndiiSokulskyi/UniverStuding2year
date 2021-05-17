from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class ForeignID(models.Model):
    COUNTRY_CODES = (
        ('ukr', 'ukr'),
        ('isr', 'isr'),
        ('pol', 'pol'),
        ('swz', 'swz'),
        ('itl', 'itl'),
    )
    country_code = models.CharField(verbose_name='country code', max_length=3, choices=COUNTRY_CODES)
    passport_no = models.CharField(verbose_name='passport no', max_length=8)
    first_name = models.CharField(verbose_name='first name', max_length=64)
    last_name = models.CharField(verbose_name='last name', max_length=64)
    date_of_birth = models.DateField(verbose_name='date of birth', )
    date_of_issue = models.DateField(verbose_name='date of issue', )
    date_of_expire = models.DateField(verbose_name='date of expire', )
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)