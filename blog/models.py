from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default="")
    content = models.CharField(max_length=500,default="")
    heading = models.CharField(max_length=50,default="")
    views = models.IntegerField(default=0)
    author = models.CharField(max_length=130,default="")
    slug = models.CharField(max_length=130,default="")
    thumbnail = models.ImageField(upload_to ="images", default="")
    punlish_date = models.DateField()
    
    def __str__(self):
        return  self.title + 'by' + self.author
    
class blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post2 = models.ForeignKey(post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return  self.comment[0:10] + "..." + 'by ' + self.user.username
    