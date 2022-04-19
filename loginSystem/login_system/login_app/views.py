from django.shortcuts import render
from login_app.models import User
# Create your views here.

def loginaction(request):
	em=''
	pwd=''
	if request.method=="POST":
		d=request.POST
		for key,value in d.items():
			if key=="email":
				em=value
			if key=="password":
				pwd=value
		
		if User.objects.filter(email = em).filter(password=pwd):
			return render(request,'welcome.html')
		else:
			return render(request,'error.html')
	return render(request,'login_page.html')
		


# Create your views here.
def signaction(request):
	nm=''
	un=''
	em=''
	pwd=''

	if request.method=="POST":
		d=request.POST
		for key,value in d.items():
			if key=="name":
				nm=value
			if key=="username":
				un=value
			if key=="email":
				em=value
			if key=="password":
				pwd=value
				
		a=User(name=nm, username=un, email=em, password=pwd)
		a.save()
		
	return render(request,'signup_page.html')