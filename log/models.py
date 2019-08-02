from django.db import models
from django.utils import timezone
# Create your models here.

month_list=(
        ('1월','1월'),
        ('2월','2월'),
        ('3월','3월'),
        ('4월','4월'),
        ('5월','5월'),
        ('6월','6월'),
        ('7월','7월'),
        ('8월','8월'),
        ('9월','9월'),
        ('10월','10월'),
        ('11월','11월'),
        ('12월','12월'),
)

date_list=(
        ('1일','1일'),('2일','2일'),('3일','3일'),('4일','4일'),('5일','5일'),
        ('6일','6일'),('7일','7일'),('8일','8일'),('9일','9일'),('10일','10일'),
        ('11일','11일'),('12일','12일'),('13일','13일'),('14일','14일'),('15일','15일'),
        ('16일','16일'),('17일','17일'),('18일','18일'),('19일','19일'),('20일','20일'),
        ('21일','21일'),('22일','22일'),('23일','23일'),('24일','24일'),('25일','25일'),
        ('26일','26일'),('27일','27일'),('28일','28일'),('29일','29일'),('30일','30일'),('31일','31일'),
)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    month_list=models.CharField(choices=month_list, max_length=30,blank=True)
    date_list=models.CharField(choices=date_list, max_length=30,blank=True)
   
    def __str__(self):
        return self.title 


class Couple(models.Model):
    person1=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    person2=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    calling_name=models.CharField(max_length=200)
    start_month=models.CharField(choices=month_list, max_length=30,blank=True)
    start_Date=models.CharField(choices=date_list, max_length=30,blank=True)


class Person(User):
    profile_image=models.FileField(null=True,blank=True)

class Wise_saying(models.Model):
    saying=models.CharField(max_length=100)