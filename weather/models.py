from django.db import models

# Create your models here.


class KhRainFall(models.Model):
    value = models.FloatField()
    # year = models.PositiveIntegerField()
    # month = models.PositiveIntegerField()
    date = models.DateField()
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        year = self.date.strftime("%Y")
        month = self.date.strftime("%-m")
        return "{0}-{1}-{2}".format(self.country, month, year)

    class Meta:
        db_table = "kh_rainfall"
        verbose_name = "Rainfall"
        unique_together = (("date", "country"), )


class KhTmax(models.Model):
    value = models.FloatField()
    # year = models.PositiveIntegerField()
    # month = models.PositiveIntegerField()
    date = models.DateField()
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        year = self.date.strftime("%Y")
        month = self.date.strftime("%-m")
        return "{0}-{1}-{2}".format(self.country, month, year)

    class Meta:
        db_table = "kh_tmax"
        verbose_name = "Max Temperature"
        unique_together = (("date", "country"), )


class KhTmin(models.Model):
    value = models.FloatField()
    # year = models.PositiveIntegerField()
    # month = models.PositiveIntegerField()
    date = models.DateField()
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        year = self.date.strftime("%Y")
        month = self.date.strftime("%-m")
        return "{0}-{1}-{2}".format(self.country, month, year)

    class Meta:
        db_table = "kh_tmin"
        verbose_name = "Min Temperature"
        unique_together = (("date", "country"), )
