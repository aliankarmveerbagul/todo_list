from django.db import models

# Create your models here.
class to_data(models.Model):
    s_no =models.IntegerField()
    task_name =models.CharField(max_length=100)
    task_status= models.CharField(max_length=500)




