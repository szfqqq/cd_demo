import os

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    """
    index 试图
    :param request: 包含了请求的信息
    :return: 响应对象
    """
    # 打印当前文件的根路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    return HttpResponse("hello the world!")