from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

class NeckOpening(models.Model):
    opt = models.CharField(max_length=255)


class Record(models.Model):
    Phone = models.IntegerField()
    Ref = models.IntegerField()
    Style = models.CharField(max_length=255)
    DateOfOrderTaken = models.DateTimeField(default=timezone.now)
    DateOfDelivery = models.DateTimeField(default=timezone.now)
    Color = models.CharField(max_length=255)
    Content_Fabric = models.CharField(max_length=255)
    DownPayment = models.FloatField()
    TotalPayment = models.FloatField()
    Check = models.IntegerField()
    BankReceipt = models.FloatField()
    Shoulder = models.CharField(max_length=255)
    ShoulderToWaist = models.CharField(max_length=255)
    Bust = models.CharField(max_length=255)
    Waist = models.CharField(max_length=255)
    WaistToHip = models.CharField(max_length=255)
    WaistToLength = models.CharField(max_length=255)
    Neck_Opening = models.ForeignKey(NeckOpening, on_delete=models.SET_NULL)
    SleeveLength = models.CharField(max_length=255)
    Cuff = models.CharField(max_length=255)
    Hip = models.CharField(max_length=255)
    Photo = models.ImageField()
    NB = models.TextField()
   
