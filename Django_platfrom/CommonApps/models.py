from django.db import models

# Create your models here.

class department(models.Model):
    dep_code=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    introduce=models.CharField(max_length=200)

class user(models.Model):
    accountID=models.IntegerField(default=0)
    username=models.CharField(max_length=20)
    gender=models.IntegerField(default=0)
    birthday=models.DateTimeField(null=True)
    address=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=200,default="")
    depId=models.ForeignKey(department, related_name='users',on_delete=models.CASCADE,null=True)
    is_flag=models.IntegerField(default=0)
    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.accountID