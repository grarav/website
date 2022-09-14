from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    tittle=models.CharField(max_length=200)
    descriptio=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle
    class Meta:
        ordering=['complete']

class FileAdmin(models.Model):
    adminupload=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
