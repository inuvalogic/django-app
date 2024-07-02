from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    enable = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "webapp_category"