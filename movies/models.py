from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120)
    release_year = models.CharField(max_length=120)
    locations = models.CharField(max_length=120)
    production_company = models.CharField(max_length=120)

    def __unicode__(self):
        return u"{}".format(self.title)