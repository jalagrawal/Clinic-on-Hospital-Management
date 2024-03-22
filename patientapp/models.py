from django.db import models
# User Details
class UserRegister(models.Model):
    uid=models.EmailField(max_length=50,verbose_name='Email',unique="True")
    userpwd=models.CharField(max_length=20,verbose_name='Password')
    userfname=models.CharField(max_length=20,default='',verbose_name='First_Name')
    usermname=models.CharField(max_length=20,default='',verbose_name='Middle_Name')
    userlname=models.CharField(max_length=20,default='',verbose_name='Last_Name')
    n='slect gender'
    g = [
        (None, 'select gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    usergender=models.CharField(max_length=12,choices=g,default=None)
    useraddress=models.CharField(max_length=20,default='',verbose_name='Address')
    usercity=models.CharField(max_length=30,default='',verbose_name='City')
    userarea=models.CharField(max_length=20,default='',verbose_name='Area')
    userpincode=models.IntegerField(default='',verbose_name='Pincode')
    usercontactno=models.IntegerField(default='',verbose_name='Contact_No')

    def __str__(self):
        return self.uid

