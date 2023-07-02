from django.shortcuts import render,redirect
from . models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
def myhome(request):
	if request.method == 'POST':
		name= request.POST.get('name')
		email= request.POST.get('email')
		mobile= request.POST.get('mobile')
		subject= request.POST.get('subject')
		message= request.POST.get('message')
		client_ip = get_client_ip(request)
		try:
			try:
				ob=enquiry.objects.get(ip=client_ip,status='Incomplete')
				status='fail'
			except:
				ob=enquiry.objects.create(name=name,email=email,mobile=mobile,subject=subject,message=message,ip=client_ip)
				status='success'
		except Exception as e:
			print(e)
			status='fail'

		return JsonResponse ({'status':status})

	return render(request, 'home.html')