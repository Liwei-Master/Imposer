from django.db import models

# Create your models here
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='用户名')
    psd = models.CharField(max_length=30)
    email = models.EmailField(db_index=True)
    facebook = models.CharField(max_length=30)
    profile= models.CharField(max_length=100)
    last_login =models.DateTimeField(blank=True)
#    isonline = models.Boolean

    def __str__(self):
        return self.name

