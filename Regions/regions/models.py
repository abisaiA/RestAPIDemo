from datetime import datetime
from django.db import models

class Region(models.Model):
    RegionID = models.AutoField(primary_key=True)
    RegionName = models.CharField(max_length=250)
    RegionDescription = models.CharField(max_length=500)
    DateCreated = models.DateTimeField(default=datetime.now, blank=True)
    DateModified = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.RegionName + ' ' + self.RegionDescription
