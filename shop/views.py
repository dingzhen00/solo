import csv

from django.shortcuts import render, redirect
from shop.models import eletronics, User, eletronicsdetail, Order
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import time
import calendar
from django.http import JsonResponse

def products_list(request):
    products = eletronics.objects.all().order_by('eid')
    allproducts = []
    total = 0
    for i in products:
        num = request.session.get(str(i.eid))
        prodict = {'eid': i.eid, 'name': i.name, 'main_category': i.main_category,
                   'sub_category': i.sub_category, 'ratings': i.ratings, 'no_of_ratings': i.no_of_ratings,
                   'discount_price': i.discount_price, 'actual_price': i.actual_price}
        if num is not None:
            prodict['number'] = num
            price = str(i.actual_price).replace('₹', '').replace(',', '')
            total += int(num) * int(price)
        else:
            prodict['number'] = 0
        allproducts.append(prodict)
    page_number = request.GET.get('page')
    # ulist=p.page(pIndex)
    paginator = Paginator(allproducts, 10)

    # ulist=paginator.page(pIndex)
    # context={'products':ulist}

    try:
        # Get the Page object for the current page number
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, show the first page
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page_number is out of range (e.g. 9999), show the last page
        page_obj = paginator.get_page(paginator.num_pages)
    isLogin = False
    if request.session.get('id') is not None:
        isLogin = True
    return render(request, 'shop/products_list.html', {'page_obj': page_obj, 'isLogin': isLogin, 'total': total})


def search_results(request):
    query = request.POST.get('query')
    if query=='':
        return redirect('product_list')
    products = eletronics.objects.filter(name__icontains=query)
    allproducts = []
    for i in products:
        num = request.session.get(str(i.eid))
        prodict = {'eid': i.eid, 'name': i.name, 'main_category': i.main_category,
                   'sub_category': i.sub_category, 'ratings': i.ratings, 'no_of_ratings': i.no_of_ratings,
                   'discount_price': i.discount_price, 'actual_price': i.actual_price}
        if num is not None:
            prodict['number'] = num
            price = str(i.actual_price).replace('₹', '').replace(',', '')
        else:
            prodict['number'] = 0
        allproducts.append(prodict)
    page_number = request.GET.get('page')
    paginator = Paginator(allproducts, 10)
    try:
        # Get the Page object for the current page number
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, show the first page
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page_number is out of range (e.g. 9999), show the last page
        page_obj = paginator.get_page(paginator.num_pages)
    isLogin = False
    if request.session.get('id') is not None:
        isLogin = True
    return render(request, 'shop/search_results.html', {'page_obj': page_obj, 'query': query, 'isLogin': isLogin})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            messages.error(request, '请输入用户名和密码。')
            return render(request, 'shop/sign_in.html')
        user = User.objects.filter(username=username, password=password)
        if user:
            request.session['id'] = user.first().id
            return redirect('product_list')
        else:
            messages.error(request, '用户名或密码错误，请重新输入。')
            return render(request, 'shop/sign_in.html')

    else:
        return render(request, 'shop/sign_in.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not all([username, password1, password2]):
            messages.error(request, 'Account or password not filled in!')
            return redirect('register')

        if password1 != password2:
            messages.error(request, 'The two entered passwords do not match!')
            return render(request, 'shop/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists, please select another username.')
            return redirect('register')

        user = User.objects.create(username=username, password=password1)
        user.save()
        messages.success(request, 'Registration successful!')
        return redirect('sign_in')

    return render(request, 'shop/register.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)
        if username=='' or password=='':
            messages.error(request, '用户名或密码不能为空，请重试。')
            return render(request, 'shop/admin_login.html')
        if user:
            # 登录成功，重定向到管理员页面
            if str(user.values('identity').first()['identity']) == 'admin':
                request.session['id'] = user.first().id
                return redirect('admin_in')
        elif user:
            # 登录失败，返回错误信息
            messages.error(request, '非管理员禁止进入。')
            return render(request, 'shop/admin_login.html')
        else:
            messages.error(request, '用户名或密码错误，请重试。')
            return render(request, 'shop/admin_login.html')
    else:
        # 显示登录页面
        return render(request, 'shop/admin_login.html')

def admindetail(request):
    User.objects.create(username='admin222',password='admin222',identity='admin')
    return redirect('index')
def changecart(request):
    eid = request.GET.get('eid')
    number = request.GET.get('number')
    request.session[eid] = number
    print(str(eid) + " " + str(number))
    return redirect('product_list')


def resetcart(request):
    products = eletronics.objects.all()
    for i in products:
        if request.session.get(str(i.eid)) is not None:
            del request.session[str(i.eid)]
    return redirect('product_list')


def logout(request):
    request.session.clear()
    return redirect('index')


def index(request):
    return render(request, 'shop/index.html')

    
def detail(request):
    eid=request.GET.get('eid')
    detail=eletronicsdetail.objects.filter(eletronics__eid=eid).first()
    isLogin=False
    if request.session.get('id') is not None:
        isLogin = True
    return render(request, 'shop/detail.html',{'eletronics':detail, 'isLogin': isLogin})


def createOrder(request):
    products = eletronics.objects.all()
    Parts = []
    amount = 0
    for i in products:
        number = request.session.get(str(i.eid))
        if number is not None:
            amount += int(number) * i.actual_price
            part=Part.objects.create(eletronics=i,number=int(number))
            Parts.append(part)
    uid=request.session.get('id')
    if uid is not None:
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user=User.objects.get(id=int(uid))
        s=Order.objects.create(user=user,time=time,amount=amount)
        for i in Parts:
            s.eletronics.add(i)

    return redirect('resetcart')

def admin_in(request):
    return render(request, 'shop/admin_in.html', {'order': Order.objects.all()})

def getdata(request):
    date = []
    num = []
    day_now=time.localtime()
    wday,monthRange=calendar.monthrange(day_now.tm_year,day_now.tm_mon)
    day_end='%d-%02d-%02d' %(day_now.tm_year,day_now.tm_mon,monthRange)
    year,month,day= day_end.split('-')
    for i in range(1,int(day)+1):
        if int(i)<10:
            data=year+"-"+month+"-0"+str(i)
            data2=month+"-0"+str(i)
        else:
            data=year + "-" + month + "-" + str(i)
            data2 =month + "-" + str(i)
        orderlist = Order.objects.all()
        count = 0
        for order in orderlist:
            ordertime=order.time.split(' ')[0]
            if ordertime==data:
                for pro in order.eletronics.all():
                    count += int(pro.number)
        date.append(data2)
        num.append(count)
    legends = ['销售数量']
    x_axis = date
    series_list = [
        {
            "name": '销售数量',
            "type": 'bar',
            "data": num
        },
    ]

    result = {
        "status": True,
        "data": {
            "legends": legends,
            "series_list": series_list,
            "x_axis": x_axis,
        }
    }
    return JsonResponse(result)