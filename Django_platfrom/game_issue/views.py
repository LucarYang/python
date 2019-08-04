from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render
from django.db import transaction

from .models import issue
import xlrd
import datetime
import time
# Create your views here.
def uploadIssue(request):
    '''
    班级信息导入
    :param request:
    :return:
    '''
    if request.method == 'POST':
        f = request.FILES.get('file')
        excel_type = f.name.split('.')[1]
        if excel_type in ['xlsx','xls']:
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None,file_contents=f.read())
            table = wb.sheets()[0]
            rows = table.nrows  # 总行数
            product_list_to_insert = list()
            try:
                with transaction.atomic():  # 控制数据库事务交易
                    for i in range(1,rows):
                        rowVlaues = table.row_values(i)
                        #print(rowVlaues)
                        Area_Id=0
                        if str(rowVlaues[2])!='':
                            Area_Id=int(rowVlaues[2])
                        IssueRemark_str=str(rowVlaues[7])
                        IssueRemark_str=IssueRemark_str[5:10]
                        print('roeid:'+str(rowVlaues[0])+'   AreaId:'+str(int(Area_Id))+"  Area_Id:"+str(Area_Id))
                        issue.objects.create(GameId=int(rowVlaues[1]),
                                             AreaId=int(Area_Id),
                                             Browser='',
                                             BrowserVersion='',
                                             IssueNum=int(rowVlaues[6]),
                                             IssueRemark='IssueRemark_str',
                                             Platform=0,
                                             SndaId=rowVlaues[9],
                                             Passport=rowVlaues[10],
                                             RoleName=rowVlaues[12],
                                             PicUrl=rowVlaues[13],
                                             Crucial=rowVlaues[15],
                                             Channel=0,
                                             UpgradeRemark=rowVlaues[17],
                                             System=rowVlaues[26],
                                             DeviceModel=rowVlaues[28],
                                             OpenId=rowVlaues[29],
                                             DeviceId=rowVlaues[30],
                                             UntiyDeviceId=rowVlaues[31],
                                             )
            except Exception as e:
                print('解析excel文件或者数据插入错误---'+str(e))#return render(request,{"message","用例导入出错:" + str(e)})
            return render(request,'gameIssue/issue.html',{'message':'导入成功'})#logger.error('解析excel文件或者数据插入错误')
        else:
            print('上传文件类型错误！')#logger.error('上传文件类型错误！')
            return render(request,'gameIssue/issue.html',{'message':'导入失败'})
    elif request.method == 'GET':
        issueList=issue.objects.all()
        paginator = Paginator(issueList, 10) # 每页显示 25 条
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # 如果用户请求的页码号不是整数，显示第一页
            contacts = paginator.page(1)
        except EmptyPage:
            # 如果用户请求的页码号超过了最大页码号，显示最后一页
            contacts = paginator.page(paginator.num_pages)
        return render(request,'gameIssue/issue.html',{'issueList':contacts,'message':'hahhaha'})
    return render(request,'gameIssue/issue.html',{'message':'还没有开始呢'})
