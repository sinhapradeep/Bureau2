from django.db import models
from django.contrib.auth.models import User
import datetime

class Detail(models.Model):
    sname = models.CharField(max_length=50, default = ' ')
    board  = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    stand = models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    course = models.CharField(max_length=30)
    stand = models.CharField(max_length=10)
    amount = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    doj = models.DateField(default=datetime.datetime.today)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=40)
    otp = models.CharField(max_length=6)

class time(models.Model):
    stand = models.CharField(max_length=50, default = ' ')
    subject  = models.CharField(max_length=50)
    mon = models.CharField(max_length=10)
    tues = models.CharField(max_length=10)
    wed = models.CharField(max_length=10)
    thurs = models.CharField(max_length=10)
    fri = models.CharField(max_length=10)
    sat = models.CharField(max_length=10)
    sun = models.CharField(max_length=10)

    @staticmethod
    def get_all_times():
        times = time.objects.all()
        return (times)
