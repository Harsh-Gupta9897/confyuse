from django.shortcuts import render,HttpResponse

# Create your views here.



def home(request):
    # if request.method == 'GET':
    #     return HttpResponse(request.GET.get('token'))
    return render(request,'index.html')

