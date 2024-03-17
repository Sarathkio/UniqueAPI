from django.db import models



class Api_data(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    class Meta:
        db_table="api_data"
