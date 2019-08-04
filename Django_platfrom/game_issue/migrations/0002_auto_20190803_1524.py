# Generated by Django 2.1.7 on 2019-08-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_issue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='AreaId',
            field=models.CharField(max_length=50, null=True, verbose_name='区Id'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Browser',
            field=models.CharField(max_length=50, null=True, verbose_name='浏览器'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='BrowserVersion',
            field=models.CharField(max_length=50, null=True, verbose_name='浏览器版本号'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='CPU',
            field=models.CharField(max_length=50, null=True, verbose_name='处理器型号 '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Channel',
            field=models.IntegerField(null=True, verbose_name='渠道来源'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='ChannelName',
            field=models.CharField(max_length=50, null=True, verbose_name='渠道（平台）名称 '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='CreateTime',
            field=models.DateTimeField(null=True, verbose_name='提问时间'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Crucial',
            field=models.IntegerField(null=True, verbose_name='事件类型'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='DeviceId',
            field=models.CharField(max_length=50, null=True, verbose_name='设备号 '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='DeviceModel',
            field=models.CharField(max_length=50, null=True, verbose_name='设备型号 '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='FinalReplier',
            field=models.IntegerField(null=True, verbose_name='最终处理人'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='GameId',
            field=models.CharField(max_length=50, null=True, verbose_name='游戏Id'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='GraphicLv',
            field=models.CharField(max_length=50, null=True, verbose_name='图形硬件支持的ShaderLevel '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='IsRead',
            field=models.IntegerField(null=True, verbose_name='用户是否阅读'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='IssueNum',
            field=models.IntegerField(null=True, verbose_name='问题类型编号'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='IssueRemark',
            field=models.CharField(max_length=255, null=True, verbose_name='问题备注'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='MemSize',
            field=models.CharField(max_length=50, null=True, verbose_name='内存大小 '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='NetEnv',
            field=models.CharField(max_length=50, null=True, verbose_name='网络环境(Wifi/Moblie) '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='OpenId',
            field=models.CharField(max_length=50, null=True, verbose_name='CP用户账号 '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Passport',
            field=models.CharField(max_length=50, null=True, verbose_name='用户输入账号'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='PicUrl',
            field=models.CharField(max_length=255, null=True, verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Platform',
            field=models.IntegerField(null=True, verbose_name='系统来源'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Resolution',
            field=models.CharField(max_length=50, null=True, verbose_name='屏幕分辨率 '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='RoleId',
            field=models.CharField(max_length=50, null=True, verbose_name='角色Id'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='RoleName',
            field=models.CharField(max_length=50, null=True, verbose_name='角色名称'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='SndaId',
            field=models.CharField(max_length=50, null=True, verbose_name='账号唯一标识'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='System',
            field=models.CharField(max_length=150, null=True, verbose_name='系统来源名称'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='UntiyDeviceId',
            field=models.CharField(max_length=50, null=True, verbose_name='Unity设备号 '),
        ),
        migrations.AlterField(
            model_name='issue',
            name='UpgradeRemark',
            field=models.CharField(max_length=255, null=True, verbose_name='升级备注'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='UpgradeRemark_sec',
            field=models.CharField(max_length=255, null=True, verbose_name='二次升级备注'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='UpgradeTime',
            field=models.DateTimeField(null=True, verbose_name='升级时间'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='UpgradeTime_sec',
            field=models.DateTimeField(null=True, verbose_name='二次升级时间'),
        ),
    ]