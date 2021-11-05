from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

class NeckOpening(models.Model):
    name = models.CharField(max_length=255)
   
    def __str__(self):
        return self.name

class Record(models.Model):
    Name = models.CharField(max_length=255, default='')
    Phone = models.CharField(max_length=255)
    Ref = models.IntegerField()
    Style = models.CharField(max_length=255)
    DateOfOrderTaken = models.DateField(default=timezone.now)
    DateOfDelivery = models.DateField(default=timezone.now)
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
    Neck_Opening = models.ForeignKey(NeckOpening, on_delete=models.CASCADE)
    SleeveLength = models.CharField(max_length=255)
    Cuff = models.CharField(max_length=255)
    Hip = models.CharField(max_length=255)
    Image = models.FileField(blank=True)
    NB = models.TextField()

    def __str__(self):
        return self.Name
   
class PostImage(models.Model):
    record = models.ForeignKey(Record, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')