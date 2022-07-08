from django.db import models
import uuid
# Create your models here.


class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    track_no = models.CharField(max_length=20)
    weight = models.CharField(max_length=5)
    ship_date = models.DateField()
    location_code = models.CharField(max_length=10)
    del_date = models.DateField()
    ship_type = models.CharField(max_length=20)
    status = models.IntegerField(default=0)
    order_no = models.CharField(max_length=20)
    final_des = models.CharField(max_length=50)

    def __str__(self):
        return self.track_no