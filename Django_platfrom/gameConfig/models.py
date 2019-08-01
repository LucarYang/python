from django.db import models
import datetime

# Create your models here.
class gameConfig(models.Model):
    ganeID=models.IntegerField(verbose_name="游戏Id" , null=False)
    gameName=models.CharField(verbose_name="游戏名称" , max_length=50)
    gameType=models.CharField(verbose_name="游戏类型" , max_length=20)
    isFlag=models.IntegerField(verbose_name="是否有效" , default=0)
    creatTime=models.IntegerField(verbose_name="更新时间戳" , default=datetime.datetime.now)