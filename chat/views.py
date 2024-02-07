from django.shortcuts import render ,redirect
from .models import Sick
from django.http import HttpResponse,JsonResponse


def home(request):

    if request.user.is_active:
        all_bemor = Sick.objects.all().order_by('-date_times')
        yoq = Sick.objects.filter(is_xuruj=True)




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
    
    return render(request , 'mein/comingtype.html',{'data':    Sick.objects.all().filter(is_xuruj=True,user=request.user).order_by('-id')
})



def tables(request):
    
    return render(request , 'mein/tables-general.html',{'data':    Sick.objects.all().filter(user=request.user).order_by('-id')
})
def handler_404(request,exception):
    
    return render(request, "404.html")