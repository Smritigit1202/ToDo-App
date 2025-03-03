from django.db import models  # database 
from django.contrib.auth.models import User #user data base


class TODOO(models.Model):
    srno= models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=25)
    date= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


def __str__(self):
    return self.title

