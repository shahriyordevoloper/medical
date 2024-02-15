from django.shortcuts import render ,redirect
from .models import Sick
from django.http import HttpResponse,JsonResponse
import datetime

def home(request):
    # print('\n' , datetime.datetime.now() , 'dddddddddddddddddddddddddddd', '\n')


    if request.user.is_active:
        all_bemor = Sick.objects.all().filter(user=request.user).order_by('-date_times')
        yoq = Sick.objects.filter(is_xuruj=True,user=request.user)




        data_from =request.GET.get('date_from')
        data_to = request.GET.get('date_to')
        hurujs = Sick.objects.filter(date_times__gte='2000-02-06 00:00'  ,date_times__lt='4024-02-06 23:59',user=request.user ).order_by('-id')
        if data_from and data_to :
            hurujs = Sick.objects.filter(date_times__gte=f'{data_from} 00:00'  ,date_times__lt=f'{data_to} 23:59',user=request.user ).order_by('-id')
        else:
            hurujs = Sick.objects.filter(date_times__gte='2000-02-06 00:00'  ,date_times__lt='4024-02-06 23:59',user=request.user ).order_by('-id')





        return render(request , 'mein/index.html', {'all_bemor':all_bemor,'yoq':yoq , 'huruj':hurujs   })
    

    else:
        return redirect('accounts/login/')
   

def user_create(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if  request.GET.get('username')  and  request.GET.get('dori') and  request.GET.get('dori_miqdor'):
            print(request.GET.get('tarif'))
            Sick.objects.create(
                username=request.GET.get('username'),
                dori_name=request.GET.get('dori'),
                dori_miqdor=request.GET.get('dori_miqdor'),
                is_xuruj=request.GET.get('tarif'),
                user=request.user,
            )

            return JsonResponse({'data':'data'},safe=False)

    return render(request , 'mein/register.html')



def comingtype(request):
    all_bemor = Sick.objects.all().filter(user=request.user).order_by('-date_times')
    yoq = Sick.objects.filter(is_xuruj=True,user=request.user)




    data_from =request.GET.get('date_from')
    data_to = request.GET.get('date_to')
    hurujs = Sick.objects.filter(date_times__gte='2000-02-06 00:00'  ,date_times__lt='4024-02-06 23:59',user=request.user ).order_by('-id')
    if data_from and data_to :
        hurujs = Sick.objects.filter(date_times__gte=f'{data_from} 00:00'  ,date_times__lt=f'{data_to} 23:59',user=request.user ).order_by('-id')
    else:
        hurujs = Sick.objects.filter(date_times__gte='2000-02-06 00:00'  ,date_times__lt='4024-02-06 23:59',user=request.user ).order_by('-id')



    return render(request , 'mein/comingtype.html',{'data': hurujs.filter(is_xuruj=True)})

def tables(request):
    all_bemor = Sick.objects.all().filter(user=request.user).order_by('-date_times')
    yoq = Sick.objects.filter(is_xuruj=True,user=request.user)




    data_from =request.GET.get('date_from')
    data_to = request.GET.get('date_to')
    hurujs = Sick.objects.filter(date_times__gte='2000-02-06 00:00'  ,date_times__lt='4024-02-06 23:59',user=request.user ).order_by('-id')
    if data_from and data_to :
        hurujs = Sick.objects.filter(date_times__gte=f'{data_from} 00:00'  ,date_times__lt=f'{data_to} 23:59',user=request.user ).order_by('-id')
    else:
        hurujs = Sick.objects.filter(date_times__gte='2000-02-06 00:00'  ,date_times__lt='4024-02-06 23:59',user=request.user ).order_by('-id')





        # return render(request , 'mein/index.html', {'all_bemor':all_bemor,'yoq':yoq , 'huruj':hurujs   })
    
    return render(request , 'mein/tables-general.html',{'huruj':    hurujs })



def delete(request,id):
    d = Sick.objects.get(id=id)
    d.delete()
    return redirect('/')
def delete1(request,id):
    d = Sick.objects.get(id=id)
    d.delete()
    return redirect('tables_all')

def delete2(request,id):
    d = Sick.objects.get(id=id)
    d.delete()
    return redirect('comingtype')

def update_sick(request,id):
    sick = Sick.objects.get(id=id)
    sick.username = request.GET.get('username')
    sick.dori_name = request.GET.get('dori')
    sick.dori_miqdor = request.GET.get('dori_miqdori')
    sick.is_xuruj = request.GET.get('talvasa')
    sick.date_times = datetime.datetime.now()

    
    sick.save()
    return redirect('/')

def update_sick1(request,id):
    sick = Sick.objects.get(id=id)
    sick.username = request.GET.get('username')
    sick.dori_name = request.GET.get('dori')
    sick.dori_miqdor = request.GET.get('dori_miqdori')
    sick.is_xuruj = request.GET.get('talvasa')
    sick.date_times = datetime.datetime.now()

    
    sick.save()
    return redirect('/tables_all/')

def update_sick2(request,id):
    sick = Sick.objects.get(id=id)
    sick.username = request.GET.get('username')
    sick.dori_name = request.GET.get('dori')
    sick.dori_miqdor = request.GET.get('dori_miqdori')
    sick.is_xuruj = request.GET.get('talvasa')
    sick.date_times = datetime.datetime.now()

    
    sick.save()
    return redirect('comingtype')



def handler_404(request,exception):
    
    return render(request, "404.html")